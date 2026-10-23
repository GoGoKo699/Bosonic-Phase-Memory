#!/usr/bin/env python3
"""Plot theorem-derived errors for two phase laws with equal Ramsey decay.

No measured data or fitted parameters are used. The wrapped-Gaussian interval
sum is evaluated through nonnegative tail differences; the Cauchy formula is
written without subtracting an almost-unit fidelity. See science/05.
"""

from __future__ import annotations

import argparse
import csv
import math
import os
from pathlib import Path
import tempfile


def gaussian_error(d: int, chi: float) -> float:
    """Wrapped Gaussian variance 2*chi; exact interval sum up to underflow."""
    if d < 1 or chi <= 0:
        raise ValueError("d >= 1 and chi > 0 are required")
    if d == 1:
        return 0.0
    a = math.pi / d
    scale = 2.0 * math.sqrt(chi)
    terms = []
    for k in range(10000):
        lower_tail = math.erfc((2.0 * math.pi * k + a) / scale)
        upper_tail = math.erfc((2.0 * math.pi * (k + 1) - a) / scale)
        terms.append(lower_tail - upper_tail)
        # The omitted tail is bounded by the next lower_tail. Underflow is
        # well below the plotted range for the fixed chi = 0.01 figure.
        if lower_tail == 0.0:
            return math.fsum(terms)
    raise ArithmeticError("Gaussian interval sum did not converge")


def cauchy_error(d: int, chi: float) -> float:
    """Wrapped Cauchy with first Fourier coefficient exp(-chi)."""
    if d < 1 or chi <= 0:
        raise ValueError("d >= 1 and chi > 0 are required")
    if d == 1:
        return 0.0
    return (2.0 / math.pi) * math.atan(
        math.tanh(chi / 2.0) / math.tan(math.pi / (2.0 * d))
    )


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--preview", type=Path, help="Optional PNG QA output")
    args = parser.parse_args()
    os.environ.setdefault("MPLCONFIGDIR", str(Path(tempfile.gettempdir()) / "bosonic-phase-matplotlib"))
    import matplotlib

    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    matplotlib.rcParams.update({
        "font.family": "DejaVu Sans",
        "font.size": 11,
        "axes.titlesize": 15,
        "axes.labelsize": 12,
        "svg.hashsalt": "bosonic-phase-memory-equal-ramsey-v1",
        "svg.fonttype": "none",
    })
    chi = 0.01
    ds = list(range(2, 257))
    g = [gaussian_error(d, chi) for d in ds]
    c = [cauchy_error(d, chi) for d in ds]
    root = Path(__file__).resolve().parents[1]
    dest = root / "figures"
    dest.mkdir(exist_ok=True)
    with (dest / "equal_ramsey_error.csv").open("w", newline="") as stream:
        writer = csv.writer(stream)
        writer.writerow(["logical_dimension", "chi", "gaussian_error", "cauchy_error"])
        for d, eg, ec in zip(ds, g, c):
            writer.writerow([d, f"{chi:.2f}", f"{eg:.16e}", f"{ec:.16e}"])

    fig, axes = plt.subplots(1, 2, figsize=(10.8, 4.9), layout="constrained")
    colors = {"Gaussian": "#2458A6", "Cauchy": "#B9482F"}
    for ax in axes:
        ax.plot(ds, g, color=colors["Gaussian"], linewidth=2.3, label="Wrapped Gaussian")
        ax.plot(ds, c, color=colors["Cauchy"], linewidth=2.3, label="Wrapped Cauchy")
        ax.set_xscale("log", base=2)
        ax.set_xticks([2, 4, 8, 16, 32, 64, 128, 256], labels=[2, 4, 8, 16, 32, 64, 128, 256])
        ax.set_xlim(2, 256)
        ax.set_xlabel(r"Logical dimension $d$")
        ax.grid(True, alpha=0.18, linewidth=0.7)
        ax.spines[["top", "right"]].set_visible(False)
    axes[0].set_yscale("log")
    axes[0].set_ylim(1e-29, 1.05)
    axes[0].set_ylabel(r"Optimal half-diamond error $\varepsilon_*$")
    axes[0].set_title("Errors differ at small dimensions")
    axes[0].legend(loc="lower right", frameon=False)
    axes[1].set_ylim(0, 1)
    axes[1].set_ylabel(r"Optimal half-diamond error $\varepsilon_*$")
    axes[1].set_title("The ordering reverses at larger dimensions")
    axes[1].axhline(0.1, linestyle="--", color="#66717B", linewidth=1)
    axes[1].text(6, 0.125, "10% error target", color="#54616B", fontsize=10)
    fig.suptitle(
        r"Equal adjacent-level Ramsey coherence: $\widehat p(1)=e^{-0.01}$",
        fontsize=16,
        fontweight="bold",
    )
    fig.savefig(dest / "equal_ramsey_error.svg", metadata={"Date": None, "Creator": "Bosonic-Phase-Memory / plot_noise_comparison.py"})
    if args.preview:
        fig.savefig(args.preview, dpi=160)
    plt.close(fig)

    for d in [2, 4, 8, 16, 32, 64, 128, 256]:
        print(f"d={d:3d}  Gaussian={gaussian_error(d, chi):.10e}  Cauchy={cauchy_error(d, chi):.10e}")
    print("Saved figures/equal_ramsey_error.svg and figures/equal_ramsey_error.csv")


if __name__ == "__main__":
    main()
