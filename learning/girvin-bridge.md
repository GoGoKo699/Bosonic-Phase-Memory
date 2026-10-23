# From Girvin's lectures to the phase-memory benchmark

The educational anchor is **Steven M. Girvin, _Introduction to Quantum Error Correction and Fault Tolerance_, SciPost Physics Lecture Notes 70 (2023)**: [primary text, arXiv:2111.08894v4](https://arxiv.org/html/2111.08894v4), revised 6 January 2023; [DOI](https://doi.org/10.21468/SciPostPhysLectNotes.70). The bibliography key is `Girvin2023`.

This bridge uses selected sections to establish the language of quantum channels, recovery, and oscillator codes. It then supplies the additional reasoning needed for this project's single-interval optimization. The [30-milestone map](milestones.md) organizes the full route; the science chapters remain the authoritative statements and proofs.

## Selective reading route

The section numbers below refer to the linked version 4. The rightmost column identifies the work supplied by this project, rather than attributing its theorem to the lecture notes.

| Read in Girvin | Preparation supplied by the source | Continue locally |
|---|---|---|
| §§3.1–3.2 | Coherent errors and coupling to an unobserved bath | [M02–M04](milestones.md#m02): random phase, channel averaging, and an inaccessible reference |
| §4, then §4.1 | Kraus maps and exact Knill–Laflamme conditions | [M03–M07](milestones.md#m03): distinguish the physical channel, encoder, recovery, and approximation metric |
| §4.2 | Syndrome-dependent recovery | [M06](milestones.md#m06) and [M18](milestones.md#m18): learn phase information without measuring the logical state |
| §§6.1–6.2 | Oscillator state space and hardware tradeoffs | [M01](milestones.md#m01), [M08](milestones.md#m08), and [M12](milestones.md#m12): specify the single-mode resource model |
| §6.4, then §§7.1–7.2 | Damping and bosonic coding examples | [M10](milestones.md#m10), then [M25–M26](milestones.md#m25): keep photon loss separate from phase diffusion |
| §§8.1–8.3 | Phase-space translations, lattices, and modular correction | [M09](milestones.md#m09), then [M17–M20](milestones.md#m17): derive the number-phase comb and its aliases |

Girvin's §6.2 already discusses packing many qubits into an oscillator and the associated sensitivity to photon loss. The question developed here is the exact optimum under unobserved phase noise. Section 8 supplies lattice intuition; the number-phase construction and its universal converse are provided locally.

The proof route does not require the surface-code material in §5. That material concerns a larger fault-tolerant architecture, whereas the theorem here fixes one completed encoding, one noisy interval, and one final recovery.

## Notation and assumption translation

| Starting point | Convention in this project |
|---|---|
| Girvin uses $`\mathcal E`$ for a collection of Kraus error operators in §4. | Here $`\mathcal E`$ denotes the **encoder**, a CPTP map from a logical system into the oscillator. A set of Kraus operators is written explicitly as $`\{K_\ell\}`$. |
| A logical qubit has two orthogonal codewords. | The logical system is $`\mathbb C^d`$; its basis index is $`j=0,\ldots,d-1`$. A register of $`k`$ logical qubits has $`d=2^k`$. |
| The oscillator has annihilation operator $`a`$ and number operator $`a^\dagger a`$. | Write $`\hat n=a^\dagger a`$, with nondegenerate eigenstates $`\lvert n\rangle`$ for $`n\ge0`$. Number is dimensionless; excitation energy is $`\hbar\omega\langle\hat n\rangle`$. |
| Damping changes the oscillator excitation. | Pure loss is $`\mathcal A_\eta`$, with transmissivity $`\eta`$. Random phase is $`\mathcal D_p`$, with $`\mathcal D_p(\lvert n\rangle\langle m\rvert)=\widehat p(n-m)\lvert n\rangle\langle m\rvert`$. They are different channels. |
| Exact error correction asks whether the chosen error set can be reversed perfectly on a code. | This project fixes a channel, allows **all** deterministic encoders and recoveries, and optimizes a generally nonzero error. Exact Knill–Laflamme conditions alone do not give that optimum. |
| A syndrome helps select a recovery. | Every measurement outcome is included. Postselecting a favorable outcome changes the task unless the failure probability is included. |

Two rate conventions deserve particular care. For the Lindblad dissipator

```math
\mathfrak D[L](\rho)
=L\rho L^\dagger-\tfrac12\{L^\dagger L,\rho\},
```

the equations $`\dot\rho=\kappa\mathfrak D[a](\rho)`$ and $`\dot\rho=\kappa_\phi\mathfrak D[\hat n](\rho)`$ describe loss and Gaussian phase diffusion, respectively. Over time $`t`$, their parameters are

```math
\eta=e^{-\kappa t},
\qquad
\gamma=\kappa_\phi t,
\qquad
\chi=\gamma/2.
```

Here $`\gamma`$ is the unwrapped Gaussian phase variance and $`e^{-\chi}`$ is the adjacent-Fock coherence. The different symbol $`\mathfrak D[L]`$ in this paragraph separates a Lindblad generator from the finite-time phase channel $`\mathcal D_p`$.

The resource assumptions are as important as the symbols. The oscillator is the only system carrying coherent logical information through the interval. Fresh recovery ancillas and an encoding-time classical record are permitted. A surviving extra quantum memory, an external observation of the realized phase, or active correction inside the interval changes the problem. The [model chapter](../science/01-model-and-question.md) states the complete allowance and exclusion list.

## The additional steps supplied locally

The following steps connect the coding language to the exact theorem. They are project exposition; the linked science chapters contain the complete derivations.

### 1. Test a channel on an entangled input

Preserving a few chosen basis states does not establish that a quantum memory preserves arbitrary superpositions or their correlations with another system. Introduce an inaccessible reference $`R`$ and

```math
|\Phi_d\rangle=\frac1{\sqrt d}\sum_{j=0}^{d-1}|j\rangle_R|j\rangle_A,
\qquad
F_e(\Lambda)=\langle\Phi_d|
(\mathrm{id}_R\otimes\Lambda)(|\Phi_d\rangle\langle\Phi_d|)
|\Phi_d\rangle.
```

This is a probability, with no square root. The reference is a mathematical test system, not a memory available to the decoder. Half diamond distance asks the corresponding worst-case channel-distinguishability question, allowing an arbitrary reference-entangled input. [M04](milestones.md#m04), [M07](milestones.md#m07), and [the error-measure definitions](../science/01-model-and-question.md#error-measures) establish the distinction.

### 2. Turn every possible code into a phase-response function

For a fixed encoder and recovery, let

```math
f(\theta)=F_e(\mathcal R\circ\mathcal U_\theta\circ\mathcal E),
\qquad
\mathcal U_\theta(\rho)=e^{-i\theta\hat n}\rho e^{i\theta\hat n}.
```

Then $`0\le f\le1`$, and the actual fidelity is $`\int p(\theta)f(\theta)\,d\theta`$. This step retains the optimization over every code; it does not assume a number-phase encoder. See [M13](milestones.md#m13) and [the universal converse](../science/02-exact-benchmark.md#universal-converse).

### 3. Obtain a budget from uniform phase averaging

Uniform averaging removes every off-diagonal number-basis term:

```math
\frac1{2\pi}\int_{-\pi}^{\pi}\mathcal U_\theta(\rho)\,d\theta
=\sum_{n=0}^{\infty}|n\rangle\langle n|\rho|n\rangle\langle n|.
```

Because each number eigenspace is one-dimensional, this channel measures and prepares number states. Its output cannot remain entangled with the reference. A separable state has overlap at most $`1/d`$ with $`|\Phi_d\rangle`$, giving

```math
\frac1{2\pi}\int_{-\pi}^{\pi}f(\theta)\,d\theta\le\frac1d.
```

A classical encoding record does not restore the lost entanglement, so the same budget covers that larger model. This is the key missing link between a statement about a particular code and a universal bound. [M14](milestones.md#m14) and [the converse proof](../science/02-exact-benchmark.md#universal-converse) supply the argument, including the retained-record case.

### 4. Use the shape of the phase distribution

A function between zero and one with total angular weight at most $`2\pi/d`$ collects the most probability by placing that weight where $`p`$ is largest. For an even density nonincreasing away from zero, that region is the central interval:

```math
F_e\le w_d(p):=\int_{-\pi/d}^{\pi/d}p(\theta)\,d\theta.
```

This probability argument explains why the complete phase law matters. It does not yet establish a matching code. [M15–M16](milestones.md#m15) and [the exact-benchmark chapter](../science/02-exact-benchmark.md) separate the fidelity converse from its consequences for other error measures.

### 5. Match the bound without measuring the logical information

The finite-support encoder is

```math
V_M|j\rangle=\frac1{\sqrt M}\sum_{k=0}^{M-1}|dk+j\rangle.
```

Writing $`n=dk+j`$ separates the number label into quotient $`k`$ and remainder $`j`$. In this tensor-factor description, phase rotation acts on the logical part with phase $`\theta`$ and on the gauge part with phase $`d\theta`$. Measuring the gauge estimates the latter phase modulo $`2\pi`$ without reading $`j`$. Hence it estimates $`\theta`$ modulo $`2\pi/d`$.

Increasing $`M`$ improves precision within that modular cell. It leaves an ambiguity among $`d`$ aliases, whose residual logical operations are powers of a generalized phase operator $`Z_d`$. The central alias has probability $`w_d(p)`$. A complete recovery and convergence of the entire logical channel, including reference-entangled inputs, are proved in [M17–M20](milestones.md#m17) and [constructive achievability](../science/03-constructive-achievability.md).

### 6. Distinguish an optimum, a limiting code, and finite resources

For every logical channel,

```math
\frac12\|\Lambda-\mathrm{id}_d\|_\diamond\ge1-F_e(\Lambda).
```

For the limiting phase-Pauli channel, equality holds: its nonidentity aliases have total probability $`1-w_d(p)`$. Thus the construction matches the converse in both metrics. If $`p`$ is even, continuous, and strictly decreasing on $`(0,\pi)`$, and $`d\gt 1`$, the optimal value is approached by normal codes but is not attained by one. These qualifications appear in [M21](milestones.md#m21) and [the theorem's continuity discussion](../science/02-exact-benchmark.md#continuity-and-nonattainment).

Finite $`M`$ requires a separate calculation. The raw finite-code channel does not generally have diamond error $`1-F_e`$. The permitted classical twirl gives that equality for the twirled channel; [M22](milestones.md#m22) explains what resource is used. Photon support, convergence estimates, and additional loss are treated in [M23–M26](milestones.md#m23) and [finite resources](../science/04-finite-resources.md). None of these steps makes the joint loss-and-dephasing optimum an exact solved quantity.

## A small example that keeps the metrics honest

Encode one qubit directly as $`|0_L\rangle=|0\rangle`$, $`|1_L\rangle=|1\rangle`$. For an even phase law with real adjacent-Fock coherence $`r`$, the resulting logical channel is

```math
\Lambda(\rho)
=(1-q)\rho+qZ\rho Z,
\qquad q=\frac{1-r}{2}.
```

Both number states are preserved perfectly. Nevertheless, a superposition loses coherence, and half of a Bell pair is no longer perfectly preserved:

```math
F_e(\Lambda)=1-q,
\qquad
\frac12\|\Lambda-\mathrm{id}_2\|_\diamond=q.
```

The metric equality is justified here by the explicit Pauli mixture; it is not an identity for arbitrary channels. Under Gaussian phase noise with $`\chi=0.01`$, this simple code has $`q=(1-e^{-0.01})/2\approx0.004975`$. It is a feasible finite-energy code, not the optimized benchmark. The optimal error instead depends on the full probability outside the correct half-circle, with wrapping included.

At the uniform-noise boundary, $`r=0`$ and the same simple code attains $`F_e=1/2`$ and diamond error $`1/2`$, exactly matching $`w_2=1/2`$. This special case is attained with finite support; it should not be confused with nonattainment for a strictly peaked density.

## Where the bridge ends

The final applications use the locally derived theorem: [M27](milestones.md#m27) compares noise laws at equal Ramsey coherence, [M28](milestones.md#m28) translates phase uncertainty into register size and time, and [M29](milestones.md#m29) identifies architectural changes that alter the assumptions. The [noise-law chapter](../science/05-noise-laws-and-architecture.md) gives their exact formulas and controlled approximations.

[M30](milestones.md#m30) returns to the full contribution. Girvin is the single educational anchor. The primary research papers in [prior work](../science/06-prior-work.md) establish the inherited constructions and closest results; they remain research references, rather than additional prerequisite textbooks.
