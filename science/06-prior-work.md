# Prior work and the precise contribution

The result established in this repository is an exact optimization for **one use of one bosonic phase-noise channel**. For every logical dimension $d$ and every symmetric unimodal phase density $p$,

```math
\sup_{\mathcal E,\mathcal R}F_e(\mathcal R\mathcal D_p\mathcal E)
=\int_{-\pi/d}^{\pi/d}p(\theta)\,d\theta,
```

and the infimal half diamond distance is the complement of this probability. The optimization includes arbitrary deterministic encoders and recoveries and retained classical records, but no extra quantum memory or information about the realized phase. The [model](01-model-and-question.md) and [proof](02-exact-benchmark.md) make those qualifications explicit.

The code family that approaches the optimum, the use of phase syndromes, and the statistical interpretation of bosonic dephasing all have substantial prior literature. The scientific claim is that a known number-phase construction attains a universal single-use converse, including a worst-case operational error measure. It is not the invention of number-phase coding or of phase-estimation-based recovery.

The primary-source comparison below was checked through **23 October 2026**. No matching exact arbitrary-encoder, arbitrary-recovery single-use fidelity curve was identified in these sources. This is a bounded literature assessment, not a proof of bibliographic priority. Titles containing “exact,” “optimal,” or “one-shot” are separated by their actual operational task and optimization domain.

Machine-readable bibliographic records are collected in [references.bib](../references/references.bib). This chapter is the authoritative account of how those sources relate to the present result.

## What is inherited and what is established here

| Ingredient or conclusion | Status and closest antecedent |
|---|---|
| Shift-resistant qudit codes and oscillator lattice encodings | Established by Gottesman, Kitaev, and Preskill; an antecedent of the discrete comb used here. |
| Rotation-symmetric number-phase codes and Pegg–Barnett finite constructions | Explicitly developed by Grimsmo, Combes, and Baragiola, including the connection to the earlier qudit construction. |
| Measuring a modular phase and correcting a representative phase cell | Established number-phase recovery mechanism. |
| A Gaussian probability integrated over a phase bin | Already appears in bosonic coding and distillation analyses; the error-function expression alone is not a new result. |
| Statistical descriptions of bosonic dephasing and hypothesis-testing converses | Established tools, especially in Lami–Wilde capacity work and Huang–Lami–Wilde sensing work. |
| A dephasing no-go theorem for gapped bosonic codes | Established by Ouyang and Campbell; it includes an unrestricted-support case when the gap parameter is one. |
| Exact global single-use optimum for every $d$ and every symmetric unimodal density | The specific result proved here by matching the uniform-twirl converse to the limiting number-phase code. |
| Matching optimum in half diamond distance | Follows here from the universal fidelity bound and convergence to the explicit phase-alias channel. |
| Finite photon support approaching the ideal optimum | An inherited construction supplied here with an explicit channel-convergence argument and resource bounds. |
| Sine-envelope phase state for a smoother finite construction | An established canonical-phase-estimation state, used by Berry and Wiseman; its finite-memory bounds are derived here. |
| Dimension and storage-time consequences | Corollaries of the exact benchmark under a specified phase law and time dependence; their broad scaling is not claimed as a previously unknown capacity phenomenon. |

## Established number-phase constructions

**Gottesman, Kitaev, and Preskill, “Encoding a qubit in an oscillator,” Physical Review A 64, 012310 (2001).** [Primary preprint](https://arxiv.org/abs/quant-ph/0008040); [DOI](https://doi.org/10.1103/PhysRevA.64.012310).

This is the foundational source for oscillator shift-resistant encoding and its discrete qudit relatives. The present construction inherits the idea of encoding logical information in a lattice while using the complementary modular variable as an error syndrome. A derivation of the comb encoder is therefore not, by itself, a novelty claim.

**Grimsmo, Combes, and Baragiola, “Quantum computing with rotation-symmetric bosonic codes,” Physical Review X 10, 011058 (2020).** [Primary full text, arXiv:1901.08071v3](https://arxiv.org/html/1901.08071v3); [DOI](https://doi.org/10.1103/PhysRevX.10.011058).

Sections III and B.3 provide the particularly close antecedent: number-phase codes, their ideal limits, phase-correctability intervals, and Pegg–Barnett constructions. Appendix B, equation B10, explicitly connects a finite construction to the earlier shift-resistant qudit codes. The encoder and modular-phase intuition in [the achievability chapter](03-constructive-achievability.md) should be read in that lineage. The additional statement here is optimality against every permitted encoder and recovery, rather than analysis within that family.

**Berry and Wiseman, “Optimal States and Almost Optimal Adaptive Measurements for Quantum Interferometry,” Physical Review Letters 85, 5098–5101 (2000).** [Primary preprint, arXiv:quant-ph/0009117v2](https://arxiv.org/abs/quant-ph/0009117); [full paper](https://arxiv.org/pdf/quant-ph/0009117); [DOI](https://doi.org/10.1103/PhysRevLett.85.5098).

Equation 10 gives the sine coefficients that maximize canonical phase sharpness under a finite number cutoff. The accompanying discussion explicitly recognizes the corresponding single-mode state as earlier work. The [finite-resource chapter](04-finite-resources.md) uses this established envelope and derives its approximation and loss bounds for the memory task. Neither the sine state nor its phase-estimation advantage is claimed as a new code family or a new phase-estimation result. The arXiv version is dated 18 September 2002; the journal publication year remains 2000.

**Jacoby, Arnon-Friedman, and Rosenblum, “Hardware-Efficient Entanglement Distillation Using Bosonic Systems,” arXiv:2503.09700v1, 12 March 2025.** [Primary full text](https://arxiv.org/html/2503.09700v1).

Appendix A.2 already integrates a Gaussian over a phase bin of width $2\pi/d$ and expresses the result with error functions. Appendix G uses Pegg–Barnett angular states and traces out the within-bin coordinate. This is a direct precedent for the phase-bin interpretation. Its discretized error model is an approximation, and its optimization concerns specified maps and states within that setting. The exact arbitrary-code converse is the distinction made in this repository; neither Gaussian bin probabilities nor angular coarse-graining are presented as new ideas.

## Closest earlier coding converse

**Ouyang and Campbell, “Trade-Offs on Number and Phase Shift Resilience in Bosonic Quantum Codes,” IEEE Transactions on Information Theory 67, 6644–6652 (2021).** [Primary author PDF](https://cdn.amazon.science/c7/73/d0e5f9054f78969ee8ea22e0f3cb/trade-offs-on-number-and-phase-shift-resilience-in-bosonic-quantum-codes.pdf); [DOI](https://doi.org/10.1109/TIT.2021.3102873).

Theorem 2 is a genuine prior no-go result for approximate correction of Gaussian dephasing by number-gapped codes, including several modes. Setting its gap parameter to one permits unrestricted Fock support, so it would be incorrect to describe earlier work as containing only code-family numerics. Its explicit lower bound becomes nontrivial beyond a gap-width threshold; Section VI identifies tighter bounds as an open direction. Its worst-case state trace-error criterion must also be distinguished from the reference-assisted criteria used here.

The present result specializes the physical setting to a single nondegenerate oscillator and obtains the exact optimum at every positive width and logical dimension, with a matching construction. It does not replace the multimode statements of Ouyang and Campbell. Nor should values under the two papers' error conventions be compared without translating the metrics.

There is a useful direct connection for a one-mode code supported on a single congruence class $n=n_0+gk$. Relabeling $k$ as the number coordinate changes a Gaussian phase variance $\gamma$ to $g^2\gamma$; the known offset $n_0$ contributes only a global phase. Applying the present benchmark to that restricted sector recovers the physical penalty from increasing number spacing, with the exact single-mode curve. This observation does not establish a result for every more general use of the phrase “gapped code.”

## Capacities and one-shot communication

**Lami and Wilde, “Exact solution for the quantum and private capacities of bosonic dephasing channels,” Nature Photonics 17, 525–530 (2023).** Published 6 April 2023. [Primary preprint](https://arxiv.org/abs/2205.05736); [main paper](https://pure.uva.nl/ws/files/179892104/Exact_solution_for_the_quantum_and_private_capacities_of_bosonic_dephasing_channels.pdf); [supplement](https://pure.uva.nl/ws/files/179892102/41566_2023_1190_MOESM1_ESM.pdf); [DOI](https://doi.org/10.1038/s41566-023-01190-4).

This is the main communication precedent. It identifies the unrestricted-energy quantum and private capacities, including two-way assisted versions, with the classical relative entropy of the phase law from the uniform distribution. With base-two logarithms,

```math
Q(\mathcal D_p)=D(p\|u)
=\int_{-\pi}^{\pi}p(\theta)\log_2[2\pi p(\theta)]\,d\theta.
```

It also supplies finite-blocklength Rényi converse bounds; main equations 30 and 33 are relevant, and the supplement defines one-shot tasks. These statements concern achievable rates over many uses or bounds on finite-use tasks. They do not state the exact single-use, fixed-dimension fidelity curve proved here. Their explicit Gaussian and Cauchy comparisons already establish that the full noise law matters. Thus a coarse logarithmic packing estimate or noise-law comparison alone would be a weak novelty claim.

**Arqand and Smith, “No advantage from classical assistance for energy-constrained bosonic dephasing channels,” arXiv:2610.13854v1, 9 October 2026.** [Primary full text](https://arxiv.org/html/2610.13854v1).

This recent work establishes energy-constrained asymptotic capacity equalities and characterizes the optimized input through Fock-diagonal coherent information. It addresses a resource constraint absent from the universal optimum here. Its asymptotic task does not yield an exact finite-energy, single-use fidelity curve. The existence of this result is a reason to avoid presenting energy-constrained capacity or absence of an asymptotic classical-assistance advantage as a new project contribution.

Two recent non-asymptotic bosonic communication papers are also close in terminology but different in channel model:

- **Mele, Barbarino, Giovannetti, and Fanizza, “Achievable rates in non-asymptotic bosonic quantum communication,” arXiv:2502.05524v2, 4 March 2025.** [Primary paper](https://arxiv.org/pdf/2502.05524). It develops achievable finite-use rates for Gaussian channels, with pure loss and amplification as applications. Its dephasing mentions are bibliographic; it does not give the phase-noise coding optimum at issue here.
- **The same authors, “Non-asymptotic quantum communication on lossy transmission lines with memory,” arXiv:2503.13207v1, 17 March 2025.** [Primary full text](https://arxiv.org/html/2503.13207v1). Its memory model extends Gaussian pure-loss transmission. Correlations between uses and finite blocklength are central there, while the present task is one random-phase interval.

The distinction between a wrapped Gaussian *phase distribution* and a bosonic *Gaussian channel* matters. Random number-generated phase diffusion need not be a Gaussian channel in the phase-space sense used by those communication papers.

## Statistical reduction and sensing

**Huang, Lami, and Wilde, “Exact Quantum Sensing Limits for Bosonic Dephasing Channels,” PRX Quantum 5, 020354 (2024).** Published 6 June 2024. [Primary preprint](https://arxiv.org/abs/2402.05793); [full paper](https://pure.uva.nl/ws/files/230546417/Exact_Quantum_Sensing_Limits_for_Bosonic_Dephasing_Channels.pdf); [DOI](https://doi.org/10.1103/PRXQuantum.5.020354).

This work reduces dephasing-channel discrimination and estimation, including adaptive strategies, to classical statistics of the phase density. Number-superposition probes and phase measurements supply the corresponding high-energy achievability. It is the closest methodological predecessor of the present classical acceptance-function argument. The fact that the converse can be written as a probability-mass optimization should not be portrayed as a new general method for bosonic channels. The coding statement requires the additional step of matching that upper bound while retaining an unknown quantum state of dimension $d$.

**Huang, Lami, Singh, and Wilde, “Efficiently Computable Strategies and Limits for Bosonic Channel Discrimination,” Physical Review A 114, 032441 (2026).** [Primary full text, arXiv:2603.19911v2, revised 21 September 2026](https://arxiv.org/html/2603.19911v2); [DOI](https://doi.org/10.1103/fypm-kjt6).

The later paper develops an energy-constrained Belavkin–Staszewski divergence chain rule and computable bounds on asymmetric discrimination error exponents, including dephasing and loss-dephasing. Its section I explicitly lists these contributions, and section II defines the discrimination task. It does not optimize the fidelity of transmitting an unknown logical register. This resolves an apparent overlap caused by “limits,” finite resources, and dephasing appearing together in the title and abstract.

## Recent number-phase optimization

**Hu, Cai, Zou, and Xiang, “Generalized number-phase lattice encoding of a bosonic mode for quantum error correction,” Nature Communications 16, 7647 (2025).** Published 16 August 2025. [Primary paper](https://www.nature.com/articles/s41467-025-62898-1); [DOI](https://doi.org/10.1038/s41467-025-62898-1).

This work develops generalized number-phase lattice families and analyzes their performance under physical noise, including the phase-sensitivity penalty from number spacing. Such a family can be compared against the present upper bound. The distinction is between improving a structured finite-energy family and proving a global optimum across all possible encoders. No claim is made here that a particular finite-energy code or recovery is numerically best among practical implementations.

**Wen, Hu, Li, and Xiang, “Estimating the performance boundary of Gottesman-Kitaev-Preskill codes and number-phase codes,” Physical Review A 114, 012450 (2026).** [Primary full text, arXiv:2602.24102v2, revised 22 July 2026](https://arxiv.org/html/2602.24102v2); [DOI](https://doi.org/10.1103/yh45-pj3r).

Its optimization varies parameters within GKP and number-phase encoding families, using numerical methods and a recovery-fidelity benchmark. A near-optimal recovery for a fixed code is not an upper bound on all encoders. The paper shows why an external, code-independent ceiling is useful: it distinguishes a family's best observed performance from the optimum of the physical channel itself.

## Loss and dephasing together

**Leviant, Xu, Jiang, and Rosenblum, “Quantum capacity and codes for the bosonic loss-dephasing channel,” Quantum 6, 821 (2022).** Published 29 September 2022. [Primary full text](https://arxiv.org/html/2205.00341v4); [DOI](https://doi.org/10.22331/q-2022-09-29-821).

This paper studies combined loss and dephasing, capacity bounds, nondegradability, and numerical code optimization under energy constraints. It provides important finite-resource context, but not an exact arbitrary-code single-use phase-only benchmark.

**Mele, Salek, Giovannetti, and Lami, “Quantum communication on the bosonic loss-dephasing channel,” Physical Review A 110, 012460 (2024).** [Primary preprint, arXiv:2401.15634v3, revised 25 July 2024](https://arxiv.org/abs/2401.15634); [DOI](https://doi.org/10.1103/PhysRevA.110.012460).

This establishes new antidegradability regions for the combined channel and contrasts unassisted with two-way assisted communication. It shows that adding dephasing can qualitatively change loss-channel communication. The present project only supplies a phase-noise upper bound and an explicit finite-code loss penalty; it does not solve that combined-channel optimization.

These sources also explain why taking photon number to infinity in a loss-free code construction does not automatically justify a practical memory claim at fixed loss. The [finite-resource chapter](04-finite-resources.md) keeps that distinction explicit.

## Scientific significance and its limits

The strongest scientific conclusion is that an oscillator's unlimited number of levels does not allow unlimited quantum memory quality at fixed phase uncertainty. There is an exact register-size/error tradeoff, and a known code family exhausts what every allowed code can do in the stated model. This changes a code-specific phase window into a physical optimum.

Three aspects make that result more informative than a scaling estimate. It gives the full fixed-dimension error curve, rather than only a rate or exponent. It identifies an optimal worst-case operational error, not just an average selected observable. It also exposes the failure of a single Ramsey contrast to certify a large register's fidelity, including the reversal between the Gaussian and Cauchy examples as the dimension changes. The proof remains short because uniform phase averaging destroys all entanglement and the optimal remaining statistical test has a simple geometry.

The proof ingredients and ideal code are established. The result does not establish an exact finite-energy optimum, an experimentally competitive implementation, or a fault-tolerance threshold. Its contribution is the global single-use optimization and the resulting physical benchmark.

The mathematical limits are also clear. Arbitrary multimodal phase densities retain the same probability-mass converse, but the present construction is not proved to attain it. Several independently noisy modes, correlated phase sensors, intermediate correction, and a fixed energy budget define further optimizations. These are scope boundaries of the established result, not assumptions that can be silently removed.
