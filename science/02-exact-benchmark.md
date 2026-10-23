# Exact benchmark for one-oscillator phase memory

## Statement and conventions

For one oscillator exposed to a symmetric, unimodal random phase, the best possible entanglement fidelity is the probability mass in one central phase cell. The optimum half-diamond error is the complementary probability. Both statements optimize over all deterministic encoding and recovery channels, without an energy constraint.

The oscillator, channel, and allowed information are specified in [the model](01-model-and-question.md). In particular,

```math
\mathcal H_B=\ell^2(\mathbb N_0),\qquad
U_\theta=e^{-i\theta\hat n},\qquad
\mathcal D_p(\rho)=\int_{-\pi}^{\pi}p(\theta)U_\theta\rho U_\theta^\dagger\,d\theta,
```

where the number spectrum is nondegenerate and $p\in L^1([-\pi,\pi))$ is a probability density with respect to angle measure. All oscillator states are normal, trace-class states. Encoding and recovery are completely positive trace-preserving maps on trace-class operators; their Heisenberg-picture duals are normal. Infinite mean photon number is allowed in the optimization, but an ideal, nonnormal phase eigenstate is not a state in this model.

Let $A\simeq\mathbb C^d$, and identify the recovered logical system with $A$. The ordinary model has channels

```math
\Lambda=\mathcal R\circ\mathcal D_p\circ\mathcal E,
\qquad
\mathcal E:A\longrightarrow B,\quad
\mathcal R:B\longrightarrow A.
```

A larger model permits a retained classical encoding record $x$:

```math
\Lambda=\sum_x\mathcal R_x\circ\mathcal D_p\circ\mathcal E_x,
\qquad
\mathcal E_x\text{ completely positive},\quad
\sum_x\mathcal E_x\text{ trace preserving},
```

with each $\mathcal R_x$ trace preserving. The displayed sums cover finite and countable records. The same statements hold for a measurable quantum instrument and its corresponding integral. No quantum subsystem or preshared entanglement crosses the noisy interval outside the oscillator. The record may depend on an encoding measurement, or on an independent random seed, but supplies no additional information about the realized phase. The reference in the error measures below is inaccessible to the protocol.

Write

```math
|\Phi_d\rangle=\frac1{\sqrt d}\sum_{j=0}^{d-1}|j\rangle_R|j\rangle_A,
\qquad
F_e(\Lambda)=\langle\Phi_d|(\mathrm{id}_R\otimes\Lambda)
(|\Phi_d\rangle\langle\Phi_d|)|\Phi_d\rangle.
```

This fidelity is the squared overlap with the target pure state. For an arbitrary input state $\rho_A$, let $F_e(\rho_A,\Lambda)$ be the corresponding overlap for a purification of $\rho_A$. It does not depend on the chosen purification. We will also establish the optimum of the worst-case reference-assisted fidelity

```math
F_{\mathrm{ref}}(\Lambda)
=\inf_{\rho_A}F_e(\rho_A,\Lambda)
=\inf_{|\psi\rangle_{RA}}
\langle\psi|(\mathrm{id}_R\otimes\Lambda)
(|\psi\rangle\langle\psi|)|\psi\rangle.
```

A reference of dimension $d$ suffices, since any purification of a state on $A$ has Schmidt rank at most $d$. This metric is different from minimizing fidelity over unentangled pure logical inputs. The operational distance is

```math
\varepsilon_\diamond(\Lambda)
=\frac12\|\Lambda-\mathrm{id}_d\|_\diamond.
```

### Theorem

Suppose $p$ has an even representative that is nonincreasing on $[0,\pi]$. Define

```math
a=\frac\pi d,
\qquad
w_d(p)=\int_{-a}^{a}p(\theta)\,d\theta.
```

For every integer $d\ge1$,

```math
\boxed{
\sup F_e(\Lambda)=\sup F_{\mathrm{ref}}(\Lambda)=w_d(p),
\qquad
\inf\varepsilon_\diamond(\Lambda)=1-w_d(p).
}
```

Each equality holds separately in the ordinary model and in the larger classical-record model. A sequence of isometric encoders with finite Fock support and trace-preserving recoveries, with no retained classical encoding record, approaches all three optima simultaneously. Thus normal states of infinite mean energy cannot improve the values. The theorem gives a supremum and an infimum; it does not assert that one finite-energy code attains them.

The converse below applies to the larger model. The matching construction is proved in [constructive achievability](03-constructive-achievability.md). Smoothness, strict unimodality, and a finite noise variance are not required for the theorem.

## Universal converse

### 1. The protocol's phase response

Fix an admissible encoder and recovery, including any classical record. For a deterministic phase $\theta$, define the logical channel and its fidelity response by

```math
\Lambda_\theta=\sum_x\mathcal R_x\circ
\mathrm{Ad}_{U_\theta}\circ\mathcal E_x,
\qquad
f(\theta)=F_e(\Lambda_\theta),
\qquad 0\le f(\theta)\le1.
```

Here $\mathrm{Ad}_U(\rho)=U\rho U^\dagger$. Entanglement fidelity is linear in the channel, so

```math
F_e(\Lambda)=\int_{-\pi}^{\pi}p(\theta)f(\theta)\,d\theta.
```

The next step constrains $f$ independently of the choice of $p$.

### 2. Uniform phase averaging destroys the oscillator's entanglement

Uniform averaging dephases the oscillator completely in its number basis:

```math
\Delta(\tau)
=\frac1{2\pi}\int_{-\pi}^{\pi}U_\theta\tau U_\theta^\dagger\,d\theta
=\sum_{n=0}^{\infty}|n\rangle\langle n|\tau|n\rangle\langle n|.
```

The integral and sum are well defined in trace norm. For finite Fock support the identity follows by integrating $e^{-i(n-m)\theta}$; trace-class approximation extends it to every physical input. The nondegeneracy of $\hat n$ makes each surviving block one dimensional.

After a general classical-record encoder and conditional recovery, this uniform average is explicitly a measure-and-prepare channel. Set

```math
A_{x,n}=\mathcal E_x^*(|n\rangle\langle n|),
\qquad
\sigma_{x,n}=\mathcal R_x(|n\rangle\langle n|).
```

The $A_{x,n}$ are positive logical effects satisfying $\sum_{x,n}A_{x,n}=I_d$, and every $\sigma_{x,n}$ is a logical density operator. Therefore

```math
\Lambda_u(\rho)
=\sum_{x,n}\mathrm{Tr}(A_{x,n}\rho)\,\sigma_{x,n}.
```

This proves entanglement breaking even when the encoder measures the input and retains the result. It also gives the needed bound directly:

```math
\begin{aligned}
\frac1{2\pi}\int_{-\pi}^{\pi}f(\theta)\,d\theta
&=F_e(\Lambda_u)\\
&=\frac1{d^2}\sum_{x,n}\mathrm{Tr}(A_{x,n}\sigma_{x,n})\\
&\le\frac1{d^2}\sum_{x,n}\mathrm{Tr}\,A_{x,n}
=\frac1d.
\end{aligned}
```

The inequality uses $0\le\sigma_{x,n}\le I_d$. For a general outcome space, the pairs $(x,n)$ define a joint POVM, and the same calculation uses the instrument integral. Positivity and normalization justify the interchange of sums and integrals. Consequently every admissible protocol obeys

```math
\boxed{\int_{-\pi}^{\pi}f(\theta)\,d\theta\le\frac{2\pi}{d}.}
```

### 3. Unimodality puts the allowed response under the central peak

For $d\gt 1$, let $\chi(\theta)=\mathbf 1_{[-a,a]}(\theta)$. Monotonicity permits a finite $c\ge0$ between the one-sided values of $p$ at $a$, so that

```math
p(\theta)\ge c\quad\text{for }|\theta|\lt a,
\qquad
p(\theta)\le c\quad\text{for }a\lt |\theta|\lt \pi
```

almost everywhere. Integrability ensures that such a finite threshold exists at $a\gt 0$, even if $p$ is unbounded at its peak. Then

```math
\begin{aligned}
\int p(\theta)\bigl(f(\theta)-\chi(\theta)\bigr)\,d\theta
&=\int\bigl(p(\theta)-c\bigr)
\bigl(f(\theta)-\chi(\theta)\bigr)\,d\theta\\
&\quad+c\left(\int f(\theta)\,d\theta-2a\right)
\le0.
\end{aligned}
```

Inside the central interval, the first integrand is nonpositive because $f-1\le0$; outside it, it is nonpositive because $f\ge0$. The last term is nonpositive by the uniform-average bound. Thus

```math
F_e(\Lambda)\le\int_{-a}^{a}p(\theta)\,d\theta=w_d(p).
```

For $d=1$, $w_1(p)=1$ and the same bound is immediate. No rearrangement regularity beyond the stated almost-everywhere monotonicity is needed.

### 4. Transfer to reference fidelity and diamond error

The maximally mixed state is one admissible input in the worst-case fidelity, hence $F_{\mathrm{ref}}(\Lambda)\le F_e(\Lambda)$. For diamond error, use the maximally entangled input and the two-outcome measurement projecting onto $|\Phi_d\rangle$:

```math
\begin{aligned}
\varepsilon_\diamond(\Lambda)
&\ge\frac12\left\|
(\mathrm{id}_R\otimes\Lambda)(\Phi_d)-\Phi_d
\right\|_1\\
&\ge1-F_e(\Lambda)
\ge1-w_d(p),
\end{aligned}
```

where $\Phi_d=|\Phi_d\rangle\langle\Phi_d|$. This uses no equivalence between fidelity and diamond error for an arbitrary channel.

## Matching logical channel

The construction uses the finite number-phase comb

```math
V_M|j\rangle=\frac1{\sqrt M}\sum_{k=0}^{M-1}|dk+j\rangle,
\qquad j=0,\ldots,d-1.
```

Its photon support ends at $dM-1$. Under the quotient/remainder identification $|dk+j\rangle\mapsto|k\rangle_G|j\rangle_L$, the noisy encoded state separates into a gauge state carrying phase $d\theta$ and a logical state rotated by $\theta$. A gauge phase measurement and a conditional logical rotation recover the phase modulo $2\pi/d$.

These code and phase-recovery ingredients belong to the established number-phase and shift-resistant oscillator-code literature: see [Gottesman, Kitaev, and Preskill (2001)](https://doi.org/10.1103/PhysRevA.64.012310), and the number-phase discussion and Appendix B.3 of [Grimsmo, Combes, and Baragiola (2020)](https://arxiv.org/html/1901.08071v3). The [construction page](03-constructive-achievability.md) provides a trace-preserving decoder, its exact finite $M$ channel, and the convergence proof used here.

Let $\mathrm{wrap}(t)$ denote the representative of $t$ in $[-\pi,\pi)$, and set

```math
\ell(\theta)=\frac{d\theta-\mathrm{wrap}(d\theta)}{2\pi}\in\mathbb Z,
\qquad
Z_d=\sum_{j=0}^{d-1}e^{-2\pi i j/d}|j\rangle\langle j|.
```

For $r=0,\ldots,d-1$, define the phase-cell probabilities

```math
w_r=\int_{\{\theta:\ell(\theta)\equiv r\ (\mathrm{mod}\ d)\}}
p(\theta)\,d\theta.
```

Endpoints have zero probability for an $L^1$ density. The identity cell is the central interval, so $w_0=w_d(p)$. The recovered channels converge in diamond norm, at fixed $d$, to

```math
\Lambda_\infty(\rho)=\sum_{r=0}^{d-1}w_r Z_d^r\rho Z_d^{-r}.
```

For every logical density operator $\rho$,

```math
F_e(\rho,\Lambda_\infty)
=\sum_{r=0}^{d-1}w_r\left|\mathrm{Tr}(\rho Z_d^r)\right|^2
\ge w_0.
```

At $\rho=I_d/d$, all terms except $r=0$ vanish. Thus

```math
F_e(\Lambda_\infty)=F_{\mathrm{ref}}(\Lambda_\infty)=w_0.
```

The triangle inequality gives

```math
\frac12\|\Lambda_\infty-\mathrm{id}_d\|_\diamond
\le\sum_{r\ne0}w_r=1-w_0.
```

The converse bound, or the mutually orthogonal Choi vectors $(I\otimes Z_d^r)|\Phi_d\rangle$, gives equality. Entanglement fidelity and worst-case reference fidelity change by at most half the diamond distance between two channels, while diamond error is continuous by the triangle inequality. The diamond-convergent sequence therefore approaches all the stated optima. It uses no retained classical encoding record, completing the proof in both operational models.

## Continuity and nonattainment

The optimum is generally approached by increasingly large photon support. A precise sufficient condition for nonattainment is the existence, for $d\gt 1$, of a threshold $c$ satisfying

```math
p(\theta)\gt c\quad\text{for almost every }|\theta|\lt a,
\qquad
p(\theta)\lt c\quad\text{for almost every }a\lt |\theta|\lt \pi.
```

A continuous density strictly decreasing with $|\theta|$ satisfies this condition. Equality in the converse would force $f(\theta)=1$ almost everywhere inside the central interval and $f(\theta)=0$ almost everywhere outside it: each nonpositive term in the threshold argument must vanish.

Every admissible physical protocol, however, has a continuous response $f$. To see this in the ordinary model, apply the encoder to half of $\Phi_d$, obtaining a trace-class state $\tau_{RB}$. Strong continuity of $U_\theta$ implies

```math
\left\|(I_R\otimes U_\theta)\tau_{RB}(I_R\otimes U_\theta^\dagger)
-(I_R\otimes U_{\theta_0})\tau_{RB}(I_R\otimes U_{\theta_0}^\dagger)
\right\|_1\longrightarrow0
```

as $\theta\to\theta_0$. A finite-rank approximation of $\tau_{RB}$ proves this implication without any energy assumption. Recovery is trace-norm contractive on state differences, and taking the overlap with $\Phi_d$ is continuous. For a classical-record instrument, apply the same argument to its unnormalized branch states. Their traces sum or integrate to one, and each difference has norm at most twice its branch trace, so dominated convergence proves continuity after summing over the record.

A continuous function cannot equal the central interval's discontinuous indicator almost everywhere when $d\gt 1$. Under the strict threshold condition, every individual protocol therefore satisfies

```math
F_e(\Lambda)\lt w_d(p),\qquad
F_{\mathrm{ref}}(\Lambda)\lt w_d(p),\qquad
\varepsilon_\diamond(\Lambda)\gt 1-w_d(p).
```

This statement includes normal encoders with infinite mean photon number. It does not classify densities with a flat region at the threshold. In particular, the strictness assumption is essential to this nonattainment argument.

## Edge cases and scope

**One-dimensional input.** For $d=1$ the logical state space has one state. The logical channel is necessarily the identity, all fidelities are one, and diamond error is zero. A vacuum encoding attains the optimum.

**Uniform phase.** For $p=1/(2\pi)$, $w_d=1/d$. Encode $|j\rangle$ as $|j\rangle_B$ and decode the corresponding number states. The resulting logical channel is complete dephasing, with $F_e=F_{\mathrm{ref}}=1/d$ and half-diamond error $1-1/d$. Thus the benchmark is attained at finite photon support. The comb decoder also gives complete logical dephasing for this density at every $M$.

**Known displaced peak.** If the density is symmetric and unimodal about a known angle $\mu$, a known rotation removes $\mu$. The optimal fidelity is the mass of the circular interval of width $2\pi/d$ centered at $\mu$.

**Densities outside the theorem.** The uniform-average bound still holds for any density. Optimizing over functions $0\le f\le1$ of integral at most $2\pi/d$ gives the more general upper bound

```math
F_e(\Lambda)\le
\sup_{S:\,|S|\le2\pi/d}\int_Sp(\theta)\,d\theta.
```

The supremum is over measurable subsets of the circle, with $|S|$ their angular measure. A central interval is optimal for the stated unimodal class. No universal achievability claim for a disconnected maximizing set or a multimodal density follows from this argument.

**Additional quantum carriers.** The proof relies on a nondegenerate phase generator and on the absence of a coherent bypass. Two oscillators under a common total-number phase, for example, have degenerate fixed-total-number eigenspaces and can support decoherence-free encodings. The single-mode result does not constrain that different memory architecture.

**Other operational questions.** This is a one-use logical-memory benchmark. The exact asymptotic quantum and private capacities of bosonic dephasing channels were determined by [Lami and Wilde (2023)](https://doi.org/10.1038/s41566-023-01190-4); those capacities optimize coding across many independent channel uses. The distinction between that result, phase-estimation limits, inherited number-phase codes, and the present theorem is developed in [prior work](06-prior-work.md).
