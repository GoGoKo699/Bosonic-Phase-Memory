# One oscillator, one unobserved phase interval

## The memory task

A harmonic oscillator has infinitely many number states. This makes it tempting to regard a single oscillator as an arbitrarily large quantum memory, provided that sufficiently energetic encodings can be prepared. The relevant question is operational: **how accurately can an arbitrary logical register survive a specified noisy interval, after optimizing both its encoding and its recovery?**

This project answers that question exactly for one oscillator undergoing a symmetric, unimodal random phase rotation. The noise is known statistically; its realized phase is unobserved. Encoding takes place before the interval and recovery after it. The answer applies to all deterministic encoders and recoveries, including codes outside any particular bosonic code family.

The result is a benchmark for an isolated storage interval. It does not include the time, control accuracy, or hardware needed to prepare and recover a code. It does make the encoded photon number explicit when constructing a sequence that approaches the benchmark.

Bosonic number-phase codes and their phase-recovery mechanism are established constructions. The contribution developed here is an exact comparison between that construction and **every allowed encoding and recovery**, in two operational error measures. The [prior-work account](06-prior-work.md) separates the inherited ingredients from this claim.

## Physical channel and notation

The oscillator Hilbert space is spanned by the nondegenerate number basis:

```math
\mathcal H_B=\overline{\mathrm{span}}\{|n\rangle:n=0,1,2,\ldots\}
\simeq\ell^2(\mathbb N_0),
\qquad
\hat n=\sum_{n=0}^{\infty}n|n\rangle\langle n|.
```

The number operator is dimensionless. Physical excitation energy is $\hbar\omega\langle\hat n\rangle$ above the vacuum. A random dimensionless phase $\theta$ acts through $U_\theta=e^{-i\theta\hat n}$. Because number eigenvalues are integers, phases lie on the circle, represented by $[-\pi,\pi)$.

Let $p$ be a nonnegative, integrable probability density on this circle, normalized with respect to ordinary angle measure:

```math
\int_{-\pi}^{\pi}p(\theta)\,d\theta=1,
\qquad
\mathcal D_p(\rho)=\int_{-\pi}^{\pi}
p(\theta)U_\theta\rho U_\theta^\dagger\,d\theta.
```

In particular, the uniform density is $u(\theta)=1/(2\pi)$. Define Fourier coefficients by

```math
\widehat p(r)=\int_{-\pi}^{\pi}p(\theta)e^{-ir\theta}\,d\theta,
\qquad r\in\mathbb Z.
```

Then $\mathcal D_p(|n\rangle\langle m|)=\widehat p(n-m)|n\rangle\langle m|$. For even $p$, these coefficients are real and equal to the corresponding cosine averages. No Gaussian approximation is part of the channel definition.

The exact result assumes that $p(\theta)=p(-\theta)$ and that $p$ is nonincreasing on $[0,\pi]$, up to changes on a measure-zero set. A known shift of the symmetry center is removed by a known rotation. Wrapped Gaussian and wrapped Cauchy densities meet these assumptions; [noise laws and architecture](05-noise-laws-and-architecture.md) gives their explicit forms and consequences. The completely noiseless phase point mass is a useful limit, but is not itself an integrable density.

## Allowed operations and information

The logical system is $A\simeq\mathbb C^d$, with $d$ a positive integer. In the basic model, an arbitrary completely positive trace-preserving encoder $\mathcal E$ maps it to the oscillator, and a completely positive trace-preserving recovery $\mathcal R$ returns a system with $d$ levels:

```math
\Lambda=\mathcal R\circ\mathcal D_p\circ\mathcal E.
```

The input can be entangled with an inaccessible reference. Every phase realization is drawn from the same law $p$, independently of the input and of the encoder's local random choices. All operations are deterministic: no branch is discarded and no conditional success probability is omitted.

The same optimum holds in a larger model with a retained classical record. Write the encoder as a quantum instrument $\{\mathcal E_x\}$ and use a recovery $\mathcal R_x$ conditioned on its outcome:

```math
\Lambda=\sum_x\mathcal R_x\circ\mathcal D_p\circ\mathcal E_x,
\qquad \sum_x\mathcal E_x\text{ is trace preserving}.
```

Finite or countable classical outcomes suffice for every construction used here. Such a record may depend on an encoding measurement or on an independent random seed. It carries no coherent quantum subsystem. The proof also applies to a general classical outcome space by replacing the sum with the corresponding instrument integral.

| Resource or operation | Scope of the benchmark |
|---|---|
| Encoding and final recovery | Arbitrary deterministic quantum channels; ideal controls are allowed. |
| Recovery ancillas | Fresh ancillas and measurements are allowed. |
| Retained classical information | Allowed, provided it does not reveal additional information about the realized phase kick. |
| Quantum memory during the interval | The one oscillator is the only system carrying the encoded quantum information. |
| Preshared entanglement across the interval | Excluded; combined with classical transmission it would permit a quantum bypass. |
| External phase sensor or environment record | Excluded if it provides information about the realized kick. |
| Operations inside the interval | Excluded; continuous correction defines a different channel or protocol. |
| Photon number | No fixed bound in the universal optimum; finite constructions report their resources explicitly. |

The reference used to evaluate a channel is not an accessible memory resource. Likewise, measuring the oscillator's own gauge subsystem during recovery is allowed: it extracts information from the system that actually experienced the noisy interval. A separate phase pilot is a different resource.

## Error measures

Let

```math
|\Phi_d\rangle=\frac1{\sqrt d}\sum_{j=0}^{d-1}|j\rangle_R|j\rangle_A.
```

Entanglement fidelity on the maximally mixed logical input is

```math
F_e(\Lambda)=\langle\Phi_d|
(\mathrm{id}_R\otimes\Lambda)(|\Phi_d\rangle\langle\Phi_d|)
|\Phi_d\rangle.
```

This is a probability, rather than its square root. It tests preservation of the register's entanglement with a reference. The worst-case operational error is half the diamond distance,

```math
\varepsilon_\diamond(\Lambda)
=\frac12\|\Lambda-\mathrm{id}_d\|_\diamond.
```

The diamond norm maximizes distinguishability over arbitrary logical inputs together with a reference; a reference of dimension $d$ suffices here. Entanglement fidelity and diamond error are different quantities for a general channel. The exact benchmark establishes their respective optima. It does not identify them for every finite code.

Define

```math
F_*(d,p)=\sup_{\mathcal E,\mathcal R}F_e(\mathcal R\mathcal D_p\mathcal E),
\qquad
\varepsilon_*(d,p)=\inf_{\mathcal E,\mathcal R}
\varepsilon_\diamond(\mathcal R\mathcal D_p\mathcal E).
```

The values are unchanged if the optimization includes retained classical records. They are also approached by finite-support codes, so allowing normal encoded states of infinite mean energy cannot improve the result.

## Exact answer and its meaning

For the stated density class, let

```math
w_d(p)=\int_{-\pi/d}^{\pi/d}p(\theta)\,d\theta.
```

The [exact benchmark](02-exact-benchmark.md) is

```math
F_*(d,p)=w_d(p),
\qquad
\varepsilon_*(d,p)=1-w_d(p).
```

The central interval has angular width $2\pi/d$. A number-phase code resolves the phase more accurately as its photon support grows, but its syndrome identifies phase only modulo this width. The probability of the identity alias is $w_d(p)$. The converse proves that no different encoder can increase this probability when assessed through entanglement fidelity, or reduce the optimal diamond error below its complement.

This has two complementary implications. Increasing photon number can approach the optimum; it cannot remove the residual phase-alias error at fixed $d$ and $p$. Increasing logical dimension shrinks the protected phase interval. If $p$ is continuous at its peak, then

```math
F_*(d,p)=\frac{2\pi p(0)}{d}+o(d^{-1})
\quad(d\longrightarrow\infty).
```

For bounded $p$, the simpler inequality $F_*\le 2\pi\|p\|_\infty/d$ is immediate. These are statements about preserving the whole register, not the error of one selected observable or one selected logical qubit.

If $p$ is continuous and strictly decreasing on $(0,\pi)$ and $d\gt 1$, no normal code attains the optimum; the more general sufficient condition is the [strict-threshold condition](02-exact-benchmark.md#continuity-and-nonattainment). The [constructive proof](03-constructive-achievability.md) specifies a sequence with finite photon support and convergence of the complete logical channel. The [finite-resource account](04-finite-resources.md) quantifies how this sequence approaches the limit and how photon loss changes its performance.

## Why the single-mode assumption matters

Uniform phase averaging completely measures the oscillator's nondegenerate number basis and destroys entanglement with a reference. This fact drives the converse. It fails for a phase generator with degenerate eigenspaces.

For example, two modes under a common phase $e^{-i\theta(\hat n_1+\hat n_2)}$ have a fixed-total-number subspace spanned by $|n,N-n\rangle$, of dimension $N+1$. Every vector in that subspace receives the same phase. A logical register with $d\le N+1$ can therefore be stored perfectly against that collective phase noise. This is a different physical channel, with an additional oscillator and a degenerate generator.

Independent phase noise on several modes, control during the interval, extra phase information, and a fixed energy constraint likewise require distinct optimization problems. The present result gives an exact reference point for one carefully specified memory task.

## Reading route

Continue to the [universal converse and theorem](02-exact-benchmark.md), then the [matching code and decoder](03-constructive-achievability.md). The [finite-energy and loss bounds](04-finite-resources.md) connect the limiting theorem to explicit resources. The [noise-law comparison](05-noise-laws-and-architecture.md) translates it into register size, storage time, and the consequences of measuring only one Ramsey coherence. The [literature comparison](06-prior-work.md) identifies the established ingredients and the exact operational claim at issue.
