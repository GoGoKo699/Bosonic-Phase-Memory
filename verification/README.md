# Reproducing the finite calculations

The general arguments are in the [exact benchmark](../science/02-exact-benchmark.md), [constructive achievability](../science/03-constructive-achievability.md), and [finite-resource proofs](../science/04-finite-resources.md). The scripts here check finite formulas and generate a theorem-derived comparison figure. They do not replace those proofs or optimize over all encoders numerically.

## Numerical checks

From the repository root, use Python 3.10 or later:

```sh
python3 verification/check_finite_resources.py
```

This script uses only the Python standard library. Its deterministic output is recorded in [check_finite_resources.expected.txt](check_finite_resources.expected.txt); the complete output was reproduced during preparation of this account.

| Check | What it tests |
|---|---|
| Resource moments and envelope normalization | The flat and sine constructions have the stated cutoff and photon-number moments. |
| Phase fidelity formulas | The finite Fourier expression agrees with the amplitude-polynomial autocorrelation formula. |
| Approximation estimates | Representative finite cases obey the stated flat and sine envelope bounds, including the sine circular moment. |
| Radial polynomial inequality | Finite points obey the inequality used to control the no-loss Kraus contribution. |
| Joint loss and dephasing | The autocorrelation formula agrees with an independent double sum of the original logical Kraus traces. |
| Converse and small-loss coefficient | Computed finite fidelities obey the phase-only ceiling and approach the derived first-order loss slope. |
| Cutoff diamond-distance inequality | A deterministic grid checks the scalar inequality used in the reference-assisted hard-cutoff proof. |

The final table reports exact finite-protocol formulas evaluated in floating point for a four-dimensional register, wrapped-Gaussian phase variance $`0.16`$, and $`-\log\eta=10^{-4}`$. Its errors are half-diamond errors of the classically twirled protocols. The last column is a proved upper bound for those explicit codes. Increasing photon support eventually increases the joint error in these examples, illustrating the competition between phase resolution and photon loss.

Numerical checks cover finitely many parameter values. No global finite-energy optimization, semidefinite-program certificate, device measurement, or experimental calibration is claimed.

## Rebuilding the noise-law figure

Install the plotting dependency, then run the generator from the repository root:

```sh
python3 -m pip install -r verification/plot_requirements.txt
python3 verification/plot_noise_comparison.py
```

The plotting environment uses Matplotlib 3.10.8. The generator writes [equal_ramsey_error.svg](../figures/equal_ramsey_error.svg) and its numerical data, [equal_ramsey_error.csv](../figures/equal_ramsey_error.csv). It fixes the SVG hash seed and omits timestamp metadata so the output is reproducible in the stated environment.

The figure compares the exact wrapped-Gaussian and wrapped-Cauchy benchmarks at the same adjacent-level Ramsey coherence, $`e^{-\chi}`$ with $`\chi=0.01`$, for logical dimensions $`2`$ through $`256`$. The values come from the formulas in [noise laws and architecture](../science/05-noise-laws-and-architecture.md); they are not measured data. The Gaussian calculation uses a convergent image sum, which avoids cancellation in very small tail probabilities.

The generated figure was visually inspected for legibility and clipping. The CSV records the full numerical values used in the plot.
