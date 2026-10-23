#!/usr/bin/env python3
"""Scoped numerical checks for science/04-finite-resources.md.

Python standard library only. Run from any working directory:
    python3 verification/check_finite_resources.py

The proofs are in the science chapter. These deterministic checks compare
independent finite formulas and catch indexing/normalization mistakes; they
are not numerical substitutes for the universal converse or diamond proof.
"""

from __future__ import annotations

import cmath
import math


def envelope(m: int, kind: str) -> list[float]:
    if kind == "flat":
        return [1.0 / math.sqrt(m)] * m
    if kind == "sine":
        scale = math.sqrt(2.0 / (m + 1))
        return [scale * math.sin(math.pi * (k + 1) / (m + 1)) for k in range(m)]
    raise ValueError(kind)


def photon_coefficients(d: int, g: list[float]) -> list[float]:
    return [g[n // d] / math.sqrt(d) for n in range(d * len(g))]


def autocorrelation(v: list[float]) -> list[float]:
    return [math.fsum(v[n] * v[n + r] for n in range(len(v) - r)) for r in range(len(v))]


def fidelity_from_coefficients(d: int, v: list[float], p_hat) -> float:
    """Window integral of a possibly unnormalized amplitude polynomial."""
    c = autocorrelation(v)
    a = math.pi / d
    return c[0] / d + 2.0 / math.pi * math.fsum(
        c[r] * p_hat(r) * math.sin(r * a) / r for r in range(1, len(c))
    )


def flat_fourier(d: int, m: int, p_hat) -> float:
    n = d * m
    return 1.0 / d + 2.0 / math.pi * math.fsum(
        (1.0 - r / n) * p_hat(r) * math.sin(math.pi * r / d) / r
        for r in range(1, n)
    )


def loss_coefficients(d: int, g: list[float], eta: float, ell: int) -> list[float]:
    n = d * len(g)
    if eta == 1.0:
        return photon_coefficients(d, g) if ell == 0 else [0.0] * (n - ell)
    # The verification uses moderate cutoffs, so exact integer binomials are safe.
    return [
        g[(r + ell) // d]
        / math.sqrt(d)
        * math.sqrt(math.comb(r + ell, ell))
        * (1.0 - eta) ** (ell / 2.0)
        * eta ** (r / 2.0)
        for r in range(n - ell)
    ]


def joint_fidelity(d: int, g: list[float], eta: float, p_hat) -> float:
    """Exact autocorrelation formula, including all trace-contributing losses."""
    return math.fsum(
        fidelity_from_coefficients(d, loss_coefficients(d, g, eta, ell), p_hat)
        for ell in range(0, d * len(g), d)
    )


def sinc_pi(x: float) -> float:
    return 1.0 if x == 0.0 else math.sin(math.pi * x) / (math.pi * x)


def joint_fidelity_direct_kraus(d: int, g: list[float], eta: float, p_hat) -> float:
    """Independent double sum from the original logical Kraus traces.

    The canonical gauge-phase integral is performed as sinc((n-m)/d).
    This does not use autocorrelations or the central-window Fourier formula.
    """
    m = len(g)
    total = []
    for ell in range(d * m):
        if ell % d:
            continue  # Every logical diagonal entry is zero in this loss branch.
        amplitudes = []
        for j in range(d):
            for k in range(m):
                initial = d * k + j
                if initial < ell:
                    continue
                output = initial - ell
                amplitude = (
                    g[k]
                    * math.sqrt(math.comb(initial, ell))
                    * (1.0 - eta) ** (ell / 2.0)
                    * eta ** (output / 2.0)
                )
                amplitudes.append((output, amplitude))
        total.append(
            math.fsum(
                x * y * p_hat(abs(n - r)) * sinc_pi((n - r) / d)
                for n, x in amplitudes
                for r, y in amplitudes
            )
            / (d * d)
        )
    return math.fsum(total)


def gaussian_hat(variance: float):
    return lambda r: math.exp(-0.5 * variance * r * r)


def gaussian_mass(d: int, variance: float) -> float:
    a = math.pi / d
    scale = math.sqrt(2.0 * variance)
    # For the variances tested, omitted images are far below double precision.
    return 0.5 * math.fsum(
        math.erf((2.0 * math.pi * k + a) / scale)
        - math.erf((2.0 * math.pi * k - a) / scale)
        for k in range(-8, 9)
    )


def gaussian_derivative_bound(variance: float, cutoff: int = 200) -> float:
    # |p'| <= pi^{-1} sum_{r>=1} r exp(-variance*r^2/2).
    # Above cutoff the summand is decreasing. Its tail is bounded by the integral.
    assert cutoff >= 1.0 / math.sqrt(variance)
    finite = math.fsum(r * math.exp(-variance * r * r / 2.0) for r in range(1, cutoff + 1))
    tail = math.exp(-variance * cutoff * cutoff / 2.0) / variance
    return (finite + tail) / math.pi


def close(x: float, y: float, tol: float = 3e-12) -> None:
    if abs(x - y) > tol:
        raise AssertionError(f"{x:.17g} != {y:.17g}, difference {x-y:.3g}")


def run_checks() -> None:
    for d, m in [(2, 1), (2, 5), (3, 4), (5, 7)]:
        n = d * m
        for kind in ("flat", "sine"):
            g = envelope(m, kind)
            v = photon_coefficients(d, g)
            close(math.fsum(x * x for x in g), 1.0)
            means = [math.fsum((d * k + j) * g[k] ** 2 for k in range(m)) for j in range(d)]
            close(math.fsum(means) / d, (n - 1) / 2.0)
            close(max(means), (n + d - 2) / 2.0)
            if kind == "sine":
                c1 = math.fsum(v[k] * v[k + 1] for k in range(n - 1))
                close(1.0 - c1, (1.0 - math.cos(math.pi / (m + 1))) / d)

    variance = 0.36
    p_hat = gaussian_hat(variance)
    lipschitz = gaussian_derivative_bound(variance)
    for d in (2, 3, 5):
        w = gaussian_mass(d, variance)
        a_leading = 2.0 / math.pi * math.fsum(
            p_hat(r) * math.sin(math.pi * r / d) for r in range(1, 201)
        )
        for m in (1, 2, 5, 12, 40):
            n = d * m
            for kind in ("flat", "sine"):
                g = envelope(m, kind)
                f = fidelity_from_coefficients(d, photon_coefficients(d, g), p_hat)
                if kind == "flat":
                    close(f, flat_fourier(d, m, p_hat))
                    bound = min(math.pi**2 * lipschitz / (2.0 * n), 2.0 * a_leading / n)
                else:
                    bound = math.pi**2 * lipschitz / (2.0 * d) * (
                        1.0 - math.cos(math.pi / (m + 1))
                    )
                if not -2e-13 <= w - f <= bound + 2e-12:
                    raise AssertionError((d, m, kind, w - f, bound))

    # The leading Fejer coefficient is compared with the exact finite sum.
    d, m = 3, 100
    n = d * m
    a_leading = 2.0 / math.pi * math.fsum(
        p_hat(r) * math.sin(math.pi * r / d) for r in range(1, 201)
    )
    close(n * (gaussian_mass(d, variance) - flat_fourier(d, m, p_hat)), a_leading, 2e-11)

    # Check the polynomial radial inequality, including d>2 and M=1.
    for d, m in [(2, 1), (3, 4), (5, 7)]:
        n = d * m
        for kind in ("flat", "sine"):
            v = photon_coefficients(d, envelope(m, kind))
            for radius in (0.0, 0.3, 0.8, 0.999):
                for j in range(129):
                    angle = -math.pi + 2.0 * math.pi * j / 128.0
                    z = cmath.exp(-1j * angle)
                    p1 = sum(v[k] * z**k for k in range(n))
                    pr = sum(v[k] * (radius * z) ** k for k in range(n))
                    if abs(pr) ** 2 + 2e-11 < radius ** (n - 1) * abs(p1) ** 2:
                        raise AssertionError((d, m, kind, radius, angle))

    # Exact loss formula versus the original decoder's Kraus-trace sum.
    for d, m, eta in [(2, 3, 0.93), (3, 4, 0.8), (4, 2, 0.995)]:
        for kind in ("flat", "sine"):
            g = envelope(m, kind)
            f_phase = fidelity_from_coefficients(d, photon_coefficients(d, g), p_hat)
            f_joint = joint_fidelity(d, g, eta, p_hat)
            f_direct = joint_fidelity_direct_kraus(d, g, eta, p_hat)
            close(f_joint, f_direct)
            lower = eta ** ((d * m - 1) / 2.0) * f_phase
            if f_joint + 2e-12 < lower:
                raise AssertionError((d, m, kind, f_joint, lower))
            f_no_jump = fidelity_from_coefficients(d, loss_coefficients(d, g, eta, 0), p_hat)
            if not lower - 2e-12 <= f_no_jump <= f_joint + 2e-12:
                raise AssertionError("No-jump comparison failed")
            # Pure loss can be absorbed into recovery, so the phase converse remains.
            if f_joint > gaussian_mass(d, variance) + 2e-12:
                raise AssertionError("Phase-only converse failed")

    # First-order loss coefficient, checked at a small finite s.
    d, m = 3, 4
    s = 1e-7
    for kind in ("flat", "sine"):
        g = envelope(m, kind)
        f0 = fidelity_from_coefficients(d, photon_coefficients(d, g), p_hat)
        slope = (joint_fidelity(d, g, math.exp(-s), p_hat) - f0) / s
        close(slope, -(d * m - 1) / 2.0 * f0, 3e-6)

    # Scalar algebra behind the reference-assisted cutoff diamond bound.
    for alpha in (0.0, 0.1, 0.5, 0.9, 0.999):
        for j in range(1001):
            u = j / 1000.0
            bound = (1.0 - alpha) / 2.0 * (
                u * (1.0 + alpha)
                + math.sqrt(u * u * (1.0 + alpha) ** 2 + 4.0 * u * (1.0 - u))
            )
            if bound > 1.0 - alpha * alpha + 2e-14:
                raise AssertionError((alpha, u, bound))

    print("PASS: resource moments, Fejer bounds, sine moment, and radial loss inequality")
    print("PASS: exact loss formula versus direct Kraus sum, converse, and first-order coefficient")
    print("PASS: scalar inequality used in the reference-assisted hard-cutoff diamond proof")


def print_examples() -> None:
    d, variance, s = 4, 0.16, 1e-4
    p_hat = gaussian_hat(variance)
    w = gaussian_mass(d, variance)
    eta = math.exp(-s)
    print()
    print(f"Example: d={d}, wrapped-Gaussian variance={variance}, s=-log(eta)={s:g}")
    print(f"Universal phase-only error floor: {1.0-w:.10f}")
    print("M   N    E_av   envelope  phase_error  joint_error  product_upper")
    for m in (4, 8, 16, 32, 64):
        n = d * m
        for kind in ("flat", "sine"):
            g = envelope(m, kind)
            f_phase = fidelity_from_coefficients(d, photon_coefficients(d, g), p_hat)
            f_joint = joint_fidelity(d, g, eta, p_hat)
            upper = 1.0 - eta ** ((n - 1) / 2.0) * f_phase
            print(
                f"{m:<3} {n:<4} {(n-1)/2:<6.1f} {kind:<9} "
                f"{1-f_phase:.10f} {1-f_joint:.10f} {upper:.10f}"
            )
    print("Errors are exact half-diamond errors of the classically twirled finite protocols.")
    print("The last column is the proved analytic upper bound, not the global joint optimum.")


if __name__ == "__main__":
    run_checks()
    print_examples()
