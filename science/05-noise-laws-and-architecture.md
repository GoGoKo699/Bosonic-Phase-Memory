# Phase noise, logical dimension, and storage time

The exact benchmark converts a probability law for the accumulated phase into a limit on the whole logical register. For one oscillator and one unobserved phase interval,

```math
F_*(d,p)=w_d(p)=\int_{-\pi/d}^{\pi/d}p(\theta)\,d\theta,
\qquad
\varepsilon_*(d,p)=1-w_d(p).
```

Here $F_*$ is the supremal entanglement fidelity and $\varepsilon_*$ is the infimal half diamond distance. The hypotheses and allowed resources are specified in [the model](01-model-and-question.md); [the theorem](02-exact-benchmark.md) proves optimality over all deterministic encoders and recoveries. The density must be symmetric and nonincreasing away from its center. This chapter verifies that hypothesis for two important noise laws, computes their exact benchmarks, and explains the architectural consequences.

The central comparison is deliberately made at **equal adjacent-Fock Ramsey coherence**. Measuring that one coherence does not determine how well a large logical register can be stored. The distribution of phase uncertainty, including its central width and its tails, matters.

## 1. One convention for comparing noise laws

For an even density, define

```math
r=\widehat p(1)=\int_{-\pi}^{\pi}p(\theta)\cos\theta\,d\theta,
\qquad
\chi=-\log r.
```

The examples below have $0<r<1$. Thus $\chi>0$ is dimensionless. It is the attenuation exponent of $|0\rangle\langle1|$, rather than an unspecified dephasing rate. Two laws with the same $\chi$ give the same Ramsey contrast in the $\{|0\rangle,|1\rangle\}$ subspace. They can act very differently on $|n\rangle\langle m|$ with larger $|n-m|$.

Use $a=\pi/d$ throughout. For $d=1$, the logical system is trivial and $F_*=1$, $\varepsilon_*=0$ for every noise strength. Statements about nontrivial error below concern $d\ge2$.

## 2. Wrapped Gaussian phase noise

### Exact density and fidelity

Let an unwrapped real phase $X$ be Gaussian with mean zero and variance $2\chi$. Reducing it modulo $2\pi$ gives

```math
p_G(\theta;\chi)
=\frac1{\sqrt{4\pi\chi}}
\sum_{m\in\mathbb Z}
\exp\!\left[-\frac{(\theta+2\pi m)^2}{4\chi}\right]
=\frac1{2\pi}\left[1+2\sum_{n=1}^{\infty}
e^{-\chi n^2}\cos(n\theta)\right].
```

Consequently $\widehat p_G(n)=e^{-\chi n^2}$ and $r=e^{-\chi}$, as required. If the phase variance is instead denoted by $\gamma$, then $\gamma=2\chi$. Keeping this factor explicit avoids confusing a variance with a Lindblad rate.

Writing $\Phi_{\mathrm N}$ for the standard normal cumulative distribution function, the exact answer is

```math
F_{*,G}(d,\chi)
=\sum_{m\in\mathbb Z}
\left[
\Phi_{\mathrm N}\!\left(\frac{2\pi m+a}{\sqrt{2\chi}}\right)
-\Phi_{\mathrm N}\!\left(\frac{2\pi m-a}{\sqrt{2\chi}}\right)
\right]
=\frac1d+\frac2\pi\sum_{n=1}^{\infty}
e^{-\chi n^2}\frac{\sin(na)}n.
```

The first expression adds the probabilities of all correct phase aliases on the real line. The second follows by integrating the Fourier series. Both include wrapping exactly. For narrow noise, the real-line interval sum is convenient; for broad noise, the Fourier series converges quickly. Tail-probability functions should be used when a numerical calculation would otherwise subtract two nearly equal numbers.

### Why the wrapped density is strictly unimodal

Evenness follows directly from either representation. Strict decrease on $(0,\pi)$ needs a justification: it does not follow just by declaring a wrapped sum to be unimodal.

Set $q=e^{-\chi}\in(0,1)$. The Jacobi product identity gives

```math
2\pi p_G(\theta;\chi)
=\vartheta_3(\theta/2,q)
=\prod_{m=1}^{\infty}(1-q^{2m})
\left(1+2q^{2m-1}\cos\theta+q^{4m-2}\right).
```

This is [NIST DLMF, equation 20.5.3](https://dlmf.nist.gov/20.5.E3). Its factors are positive, and the logarithmic derivative converges for fixed $q<1$:

```math
\frac{\partial}{\partial\theta}\log p_G(\theta;\chi)
=-2\sin\theta\sum_{m=1}^{\infty}
\frac{q^{2m-1}}
{1+2q^{2m-1}\cos\theta+q^{4m-2}}<0,
\qquad 0<\theta<\pi.
```

The exact theorem therefore applies for every finite $\chi>0$.

### A controlled Gaussian-tail approximation

The unwrapped central interval has probability

```math
\Pr(|X|\le a)=\operatorname{erf}\!\left(\frac{a}{2\sqrt\chi}\right).
```

All additional correct intervals lie within $|X|\ge2\pi-a$. Thus

```math
0\le F_{*,G}(d,\chi)
-\operatorname{erf}\!\left(\frac{a}{2\sqrt\chi}\right)
\le \operatorname{erfc}\!\left(\frac{2\pi-a}{2\sqrt\chi}\right).
```

Equivalently, the exact error satisfies the finite wrapping bounds

```math
\operatorname{erfc}\!\left(\frac{a}{2\sqrt\chi}\right)
-\operatorname{erfc}\!\left(\frac{2\pi-a}{2\sqrt\chi}\right)
\le \varepsilon_{*,G}(d,\chi)
\le \operatorname{erfc}\!\left(\frac{a}{2\sqrt\chi}\right).
```

These inequalities state when the familiar complementary-error-function expression is accurate. They also show its direction: the unwrapped tail slightly overestimates the actual logical error, because sufficiently large phase excursions can wrap into a correct interval. The error-function expression is not the exact wrapped answer.

At fixed $d\ge2$ and $\chi\downarrow0$, the correction is exponentially smaller than the leading tail, so

```math
\varepsilon_{*,G}(d,\chi)
\sim\frac{2d\sqrt\chi}{\pi\sqrt\pi}
\exp\!\left[-\frac{\pi^2}{4d^2\chi}\right].
```

Two other limits prevent overextending that approximation:

```math
F_{*,G}(d,\chi)
\sim\frac{2\pi p_G(0;\chi)}d
\quad(d\to\infty,\ \chi>0\text{ fixed}),
```

```math
F_{*,G}(d,\chi)
=\frac1d+\frac2\pi e^{-\chi}\sin(\pi/d)+O(e^{-4\chi})
\quad(\chi\to\infty,\ d\text{ fixed}).
```

At fixed noise strength, increasing logical dimension ultimately makes the error approach one. At very large noise, the optimum approaches the fidelity $1/d$ of a completely dephased logical register.

### Exact threshold and dimension scaling

For $d\ge2$, the Gaussian optimum is strictly decreasing with $\chi$. Indeed, the wrapped heat kernel obeys $\partial_\chi p_G=\partial_\theta^2p_G$, and therefore

```math
\partial_\chi F_{*,G}(d,\chi)
=2\partial_\theta p_G(a;\chi)<0.
```

For a target $0<\varepsilon<1-1/d$, there is consequently a unique exact threshold $\chi_{G}(d,\varepsilon)$ defined by

```math
F_{*,G}(d,\chi_G)=1-\varepsilon.
```

The wrapped series above specifies it without approximation. Let $z_\varepsilon=\operatorname{erfc}^{-1}(\varepsilon)>0$. A simple sufficient noise budget is

```math
\chi\le\frac{\pi^2}{4d^2z_\varepsilon^2}.
```

The lower wrapping bound supplies the corresponding necessary test when precision beyond the leading expression matters. In the limit of large $d$ at fixed $\varepsilon\in(0,1)$,

```math
\chi_G(d,\varepsilon)
\sim\frac{\pi^2}{4d^2z_\varepsilon^2}.
```

Equivalently, define the benchmark dimension ceiling as the largest integer $d$ for which $\varepsilon_{*,G}(d,\chi)\le\varepsilon$. Then

```math
d_{\varepsilon,G}(\chi)
\sim\frac{\pi}{2z_\varepsilon\sqrt\chi}
\qquad(\chi\downarrow0,\ \varepsilon\in(0,1)\text{ fixed}).
```

For a very small target error, $z_\varepsilon^2\sim\log(1/\varepsilon)$, with smaller logarithmic corrections. This gives the familiar leading dependence $\chi_G\sim\pi^2/[4d^2\log(1/\varepsilon)]$ when $d$ is fixed and $\varepsilon\downarrow0$.

The ceiling refers to the infimum over all allowed codes. Strictly unimodal noise has no normal code attaining that infimum for $d>1$. A strict error margin above $\varepsilon_*$ is achievable with finite photon support; equality at the threshold requires the limiting construction. This distinction does not change the displayed asymptotic scalings.

## 3. Wrapped Cauchy phase noise at the same Ramsey contrast

### Exact solution

The wrapped Cauchy law with the same $r=e^{-\chi}$ is

```math
p_C(\theta;\chi)
=\frac{1-e^{-2\chi}}
{2\pi(1-2e^{-\chi}\cos\theta+e^{-2\chi})}
=\frac{\sinh\chi}{2\pi(\cosh\chi-\cos\theta)}.
```

Its Fourier coefficients are $\widehat p_C(n)=e^{-\chi|n|}$. In particular, its first coefficient agrees exactly with the Gaussian law, while higher coherences have a linear exponent in $|n|$ rather than a quadratic one. Its unwrapped Cauchy scale is $\chi$; no finite unwrapped phase variance is assigned to it.

The density is even, and

```math
\partial_\theta p_C(\theta;\chi)
=-\frac{\sinh\chi\sin\theta}
{2\pi(\cosh\chi-\cos\theta)^2}<0
\qquad(0<\theta<\pi).
```

Integrating with $u=\tan(\theta/2)$ gives the exact optimum

```math
F_{*,C}(d,\chi)
=\frac2\pi\arctan\!\left[
\coth(\chi/2)\tan\!\left(\frac\pi{2d}\right)
\right],
```

```math
\varepsilon_{*,C}(d,\chi)
=\frac2\pi\arctan\!\left[
\tanh(\chi/2)\cot\!\left(\frac\pi{2d}\right)
\right].
```

The second expression computes small errors without subtracting a fidelity close to one. For $d=1$, interpret the first formula by continuity; the second directly gives zero.

For fixed $d\ge2$ and weak noise,

```math
\varepsilon_{*,C}(d,\chi)
\sim\frac\chi\pi\cot\!\left(\frac\pi{2d}\right).
```

For large dimension at fixed positive $\chi$, and for broad noise at fixed dimension, respectively,

```math
F_{*,C}(d,\chi)\sim\frac{\coth(\chi/2)}d,
```

```math
F_{*,C}(d,\chi)
=\frac1d+\frac2\pi e^{-\chi}\sin(\pi/d)+O(e^{-2\chi}).
```

### Dimension and noise budgets

The exact condition $\varepsilon_{*,C}(d,\chi)\le\varepsilon$, for $0<\varepsilon<1$, is

```math
d\le\frac{\pi}
{2\arctan\!\left[\tanh(\chi/2)\cot(\pi\varepsilon/2)\right]}.
```

The integer benchmark ceiling is the floor of the right-hand side. At fixed target error,

```math
d_{\varepsilon,C}(\chi)
\sim\frac{\pi\tan(\pi\varepsilon/2)}\chi
\qquad(\chi\downarrow0).
```

Conversely, for $d\ge2$ and $0<\varepsilon<1-1/d$, the exact largest noise exponent is

```math
\chi_C(d,\varepsilon)
=2\operatorname{artanh}\!\left[
\tan(\pi\varepsilon/2)\tan\!\left(\frac\pi{2d}\right)
\right].
```

If $\varepsilon\ge1-1/d$, a completely dephased logical register already meets the target, and this criterion imposes no finite upper bound on $\chi$. For large $d$ and fixed $\varepsilon$,

```math
\chi_C(d,\varepsilon)
\sim\frac{\pi\tan(\pi\varepsilon/2)}d.
```

When the target error is also small, the leading coefficient becomes $\pi^2\varepsilon/(2d)$. As for the Gaussian law, finite codes attain any strict margin above the limiting optimum.

## 4. Equal Ramsey coherence does not give a universal ordering

There are two different questions, with different answers.

At **fixed logical dimension** and $\chi\downarrow0$, the Gaussian error is exponentially small in $1/\chi$, whereas the Cauchy error is proportional to $\chi$. The Gaussian memory is much better in this limit.

At **fixed nonzero target error** and $\chi\downarrow0$, the largest allowed dimension grows as $\chi^{-1/2}$ for the Gaussian law and as $\chi^{-1}$ for the Cauchy law. The Cauchy law eventually supports a larger register. At equal first Fourier coefficient it has a much narrower central peak, accompanied by heavier tails. A small fixed register is sensitive to those tails; a growing register can instead benefit from the narrower peak.

The following exact integer ceilings use target error $\varepsilon=0.01$. The Gaussian entries use the wrapped interval sum and the Cauchy entries use its exact inverse formula; these are not floors of leading asymptotic estimates.

| Equal Ramsey exponent $\chi$ | Gaussian dimension ceiling | Cauchy dimension ceiling |
|---:|---:|---:|
| $10^{-2}$ | 8 | 5 |
| $10^{-3}$ | 27 | 49 |
| $10^{-4}$ | 86 | 493 |

![Exact optimal errors for equal Ramsey contrast, with a crossover as logical dimension grows.](../figures/equal_ramsey_error.svg)

The figure fixes $\chi=0.01$. At $d=2$, the exact Gaussian and Cauchy errors are approximately $1.16\times10^{-28}$ and $0.00318$. At $d=16$, they are approximately $0.165$ and $0.0323$. Both comparisons use the same Ramsey contrast $e^{-0.01}$. The [data](../figures/equal_ramsey_error.csv) and [plotting calculation](../verification/plot_noise_comparison.py) reproduce the curves.

Noise-law dependence and Gaussian/Cauchy capacity comparisons already appear in [Lami and Wilde's capacity work](06-prior-work.md#capacities-and-one-shot-communication). The contribution here is the exact single-interval fidelity and diamond-error comparison, including its finite-$d$ crossover. A Ramsey decay constant alone cannot certify this memory benchmark, and a statement that heavier tails are always worse would be incorrect.

## 5. Translating phase uncertainty into storage time

The theorem depends on the phase distribution accumulated during an interval. It does not require that the noise be Markovian. A time law must be specified before turning a dimension constraint into a deadline.

### Exponential Ramsey decay

Suppose $r(t)=e^{-t/T_R}$, so $\chi(t)=t/T_R$. Both the wrapped Gaussian family and the wrapped Cauchy family define convolution semigroups with this first-harmonic decay, although their higher harmonics differ. For a logical register of $k$ qubits, set $d=2^k$.

At fixed target error and large $d$, the Gaussian storage threshold is

```math
t_G(d,\varepsilon)
\sim\frac{\pi^2T_R}{4z_\varepsilon^2}\,d^{-2}
=\frac{\pi^2T_R}{4z_\varepsilon^2}\,4^{-k}.
```

The exact Gaussian threshold is the root of the wrapped expression. The Cauchy threshold is elementary:

```math
t_C(d,\varepsilon)
=2T_R\operatorname{artanh}\!\left[
\tan(\pi\varepsilon/2)\tan\!\left(\frac\pi{2d}\right)
\right]
\sim\pi T_R\tan(\pi\varepsilon/2)\,2^{-k}.
```

These are thresholds for preserving the entire register, including its entanglement with a reference. They are not single-qubit error probabilities subsequently averaged over the register.

For the common master-equation convention

```math
\dot\rho=\kappa_\phi\mathcal D[\hat n](\rho),
\qquad
\mathcal D[L](\rho)=L\rho L^\dagger
-\tfrac12\{L^\dagger L,\rho\},
```

one has $\gamma(t)=\kappa_\phi t$, $\chi(t)=\kappa_\phi t/2$, and $T_R=2/\kappa_\phi$. Any numerical architecture estimate must state this convention.

### Quasistatic Gaussian frequency noise

Suppose instead that an unknown frequency offset is constant within each interval, with zero mean and variance $\sigma_\omega^2$. Then $\theta=t\,\delta\omega$ is Gaussian before wrapping, but

```math
\chi(t)=\frac{\sigma_\omega^2t^2}{2}.
```

The large-$d$ threshold becomes

```math
t_G(d,\varepsilon)
\sim\frac{\pi}{\sqrt2\,\sigma_\omega z_\varepsilon}\,d^{-1}.
```

Thus even Gaussian phase noise does not universally imply a $4^{-k}$ time law. That exponent requires phase variance proportional to time. The general prescription is to determine the interval's phase law, evaluate its exact central probability, and then invert its actual time dependence.

## 6. Architectural meaning and boundaries

### Energy, controls, and additional noise

The oscillator's infinite Hilbert space does not provide an unlimited high-fidelity quantum register for a fixed nonzero phase law. Increasing photon support improves phase estimation within a modular cell; it cannot distinguish the $d$ phase aliases that act differently on the logical register. The universal converse makes this limitation independent of a chosen code family.

Approaching the optimum still consumes a resource. The finite comb with logical dimension $d$ and gauge length $M$ occupies Fock levels up to $dM-1$. Its mean photon number is $(dM-1)/2$ on the maximally mixed logical input and at most $(dM+d-2)/2$ over all logical inputs. The [finite-resource analysis](04-finite-resources.md) treats the approximation to the ideal limit and the cost of photon loss. An arbitrarily large photon budget is allowed in the upper bound; it is not described as free in a physical implementation.

The architecture statement applies between a completed encoding and a final recovery. It does not estimate preparation time, gate throughput, syndrome-extraction bandwidth, or the quality of available controls. An architecture performing active or autonomous correction throughout the interval has changed the protocol. Such an architecture must charge its extra modes, measurements, control operations, and time; it is not constrained by simply applying this passive-interval formula to its full operating lifetime.

Appending a noise channel cannot improve the optimum, because it could be absorbed into the allowed recovery. In particular, the phase-only result remains an upper bound for phase noise followed by photon loss. Phase covariance allows pure loss and these random-phase channels to be interchanged. A matching phase-only code sequence need not remain good at a fixed nonzero loss rate as its photon support grows. No exact combined loss-and-dephasing optimum is asserted here; [the primary literature](06-prior-work.md#loss-and-dephasing-together) contains separate capacity and coding results for that problem.

### Several modes

The nondegenerate single-mode number spectrum is essential. Two modes with a common random phase have unitary

```math
e^{-i\theta(\hat n_1+\hat n_2)}.
```

For fixed total number $N$, the $N+1$ states $|n,N-n\rangle$, $0\le n\le N$, span a subspace on which every phase rotation is a scalar. A logical system of dimension at most $N+1$ is therefore perfectly protected against that collective noise. The extra mode and $N$ photons are explicit resources. Uniform averaging over the common phase is not entanglement breaking, so the single-mode converse does not apply.

For $m$ modes whose vector of individual phases has a joint integrable density on the $m$-torus, averaging independently and uniformly over all $m$ angles does dephase the nondegenerate joint Fock basis. The same converse then gives a useful upper bound: the weighted success function has uniform average at most $1/d$, so its weighted average is at most the probability mass of the densest region of phase volume $(2\pi)^m/d$. The singular common-phase distribution in the preceding example is outside this density assumption. This does not establish a matching multimode code. A central interval has no direct higher-dimensional replacement that is automatically achievable. Product codes give lower bounds, while joint coding requires a separate analysis.

### Information about the realized phase

A known constant phase offset can be removed by a known rotation. Knowledge of the random phase realization is a different resource: if a sensor reports $\theta$ exactly, applying $U_\theta^\dagger$ removes the noise and the ceiling disappears.

For an external classical observation $Y$ whose joint law with the phase is independent of the logical input, the same converse can be applied conditionally. Assume that $p(\theta\mid Y=y)$ is an integrable density for almost every $y$; exact phase reporting, which gives point masses instead, was treated separately above. If

```math
\Lambda_d(p)=\sup_{\substack{0\le f\le1\\
\int f(\theta)\,d\theta\le2\pi/d}}
\int p(\theta)f(\theta)\,d\theta,
```

then any decoder using that observation obeys $F_e\le\mathbb E_Y\Lambda_d(p(\theta\mid Y))$. This is an upper bound for general conditional densities, not an automatic achievability theorem. A phase monitor or correlated pilot must therefore be included in the resource model. The oscillator's own measured gauge degree of freedom already belongs to the allowed recovery; a separate surviving quantum memory does not.

These boundaries explain both the force and the limits of the result. It gives an exact, code-independent ceiling for one specified memory interval. Extending a device's resources or changing its phase correlations creates a new physical question, rather than a violation of that ceiling.
