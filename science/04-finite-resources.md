# Finite photon resources and weak photon loss

The exact benchmark is an unrestricted-energy optimum. This chapter gives finite-support implementations, explicit approximation bounds, and a controlled addition of pure loss. It does **not** solve the globally optimal finite-energy code or the globally optimal joint loss–dephasing problem.

There are two constructive conclusions. The flat comb from [the achievability proof](03-constructive-achievability.md) approaches the phase benchmark with a computable gap of order $1/N$ for a continuously differentiable density, where $N=dM$ is the number of occupied Fock levels. Replacing its flat gauge amplitudes by the established sine envelope improves a rigorous bound to order $d/N^2$, at the same photon cutoff and mean energy. Both constructions obey the following loss guarantee after an admissible classical twirl:

```math
\varepsilon_\diamond^{\rm loss+phase}
\le 1-\eta^{(N-1)/2}F^{\rm phase},
```

where $\eta$ is photon transmissivity and $F^{\rm phase}$ is the finite code's phase-only entanglement fidelity. In particular, the limiting pure-phase answer remains a useful approximation when energy is chosen to balance phase-estimation error against loss.

All operations here are ideal. The resource ledger counts photon number and the retained classical twirl label; it does not assign preparation time, measurement bandwidth, or gate error to the encoder and decoder. The number-phase construction is inherited from the literature [1,2]. The sine envelope is a standard canonical-phase-estimation state [3]. Their role here is to give quantitative implementations of the benchmark.

## 1. Conventions and resource ledger

Take $d\ge2$, $M\ge1$, $N=dM$, and $a=\pi/d$. The trivial case $d=1$ needs no memory. For the flat comb,

```math
V_M|j\rangle=\frac1{\sqrt M}\sum_{k=0}^{M-1}|dk+j\rangle,
\qquad 0\le j\lt d.
```

For a logical state $\rho$, its encoded mean number is

```math
\mathrm{Tr}(\hat nV_M\rho V_M^\dagger)
=\frac{d(M-1)}2+\sum_{j=0}^{d-1}j\rho_{jj}.
```

The following quantities must not be interchanged:

| Resource | Flat comb and sine-envelope code |
|---|---:|
| Maximum occupied photon number | $n_{\max}=N-1$ |
| Mean number for maximally mixed logical input | $E_{\rm av}=(N-1)/2$ |
| Largest mean number over logical inputs, before randomization | $E_{\max}=(N+d-2)/2$ |
| Classical twirl label | $q\in\{0,\ldots,d-1\}$, requiring $\lceil\log_2d\rceil$ storage bits |

The uniform cyclic twirl described below makes the **unconditional** mean number equal to $E_{\rm av}$ for every logical input. The largest conditional mean in one known twirl branch remains $E_{\max}$. The hard cutoff is unchanged. Physical excitation energy is $\hbar\omega$ times the corresponding mean number.

Throughout, $p$ is normalized with respect to $d\theta$ and

```math
\widehat p(r)=\int_{-\pi}^{\pi}p(\theta)e^{-ir\theta}\,d\theta,
\qquad
w=\int_{-a}^{a}p(\theta)\,d\theta.
```

Unless explicitly broadened, $p$ is even and nonincreasing on $[0,\pi]$. Then $w$ is the optimal phase-only fidelity. Approximation statements for a general density concern the central-cell decoder's limiting value $w$; they do not assert that this value is globally optimal for a nonunimodal density.

## 2. Exact flat-comb fidelity

The gauge-phase decoder in [Chapter 3](03-constructive-achievability.md) gives

```math
F_M=\int_{-\pi}^{\pi}\frac{K_N(t)}{2\pi}H(t)\,dt,
\qquad
H(t)=\int_{-a}^{a}p(x+t)\,dx,
```

with all arguments understood periodically and

```math
K_N(t)=\frac1N\left|\sum_{n=0}^{N-1}e^{-int}\right|^2
=\frac{\sin^2(Nt/2)}{N\sin^2(t/2)}.
```

The value at $t=0$ is defined by continuity. The normalized Fejér kernel $K_N/(2\pi)$ is nonnegative and integrates to one. For an even unimodal density, a centered interval contains at least as much mass as any translate, so $H(t)\le H(0)=w$. Consequently,

```math
\Delta_M:=w-F_M\ge0.
```

For any real density, including a nonsymmetric one, the finite Fourier formula is

```math
F_M=\frac1d+
\frac2\pi\sum_{r=1}^{N-1}
\left(1-\frac rN\right)
\mathrm{Re}\,\widehat p(r)\frac{\sin(ra)}r.
```

This finite sum has no truncation error. It is usually the simplest numerical evaluation of the flat construction.

### 2.1 A derivative bound with an explicit constant

Suppose $p$ is periodic and continuously differentiable, and write $L=\|p'\|_\infty$. Since

```math
H'(t)=p(a+t)-p(-a+t),
\qquad |H''(t)|\le2L,
```

the symmetric part $H_{\rm e}(t)=[H(t)+H(-t)]/2$ satisfies

```math
|H_{\rm e}(t)-H(0)|\le L t^2,
\qquad |t|\le\pi.
```

The kernel is even, so only this symmetric part matters. The elementary inequality $t^2\le\pi^2\sin^2(t/2)$ gives

```math
\int_{-\pi}^{\pi}\frac{K_N(t)}{2\pi}t^2\,dt
\le\frac{\pi^2}{2N},
```

where $\int_{-\pi}^{\pi}\sin^2(Nt/2)\,dt=\pi$ was used. Thus

```math
|F_M-w|\le\frac{\pi^2\|p'\|_\infty}{2N}.
```

For the unimodal class, this is $0\le\Delta_M\le\pi^2L/(2N)$. The same proof works for a periodic Lipschitz density using its Lipschitz constant.

### 2.2 Fourier bound and the actual leading coefficient

If $p$ is absolutely continuous with $p'\in L^2$, define

```math
B_{\rm F}(p,d)=\frac2\pi\sum_{r=1}^{\infty}
|\widehat p(r)\sin(ra)|.
```

This is finite. Indeed, integration by parts, Parseval, and Cauchy–Schwarz give

```math
\sum_{r=1}^{\infty}r^2|\widehat p(r)|^2
=\pi\|p'\|_2^2,
\qquad
B_{\rm F}\le\sqrt{\frac{2\pi}{3}}\,\|p'\|_2.
```

Subtracting the finite Fourier sum from the interval mass gives

```math
w-F_M=\frac2\pi\left[
\frac1N\sum_{r=1}^{N-1}\mathrm{Re}\,\widehat p(r)\sin(ra)
+\sum_{r=N}^{\infty}\mathrm{Re}\,\widehat p(r)\frac{\sin(ra)}r
\right].
```

Since $1/r\le1/N$ in the second sum,

```math
|w-F_M|\le\frac{B_{\rm F}}N.
```

There is also an exact first-order asymptotic coefficient:

```math
A(p,d)=\frac2\pi\sum_{r=1}^{\infty}
\mathrm{Re}\,\widehat p(r)\sin(ra),
\qquad
w-F_M=\frac{A(p,d)}N+o(N^{-1}).
```

A useful certified remainder is

```math
\left|w-F_M-\frac AN\right|
\le\frac2{\pi N}\sum_{r=N}^{\infty}
\left(1-\frac Nr\right)|\widehat p(r)|.
```

For example, the right side is at most
$2\|p'\|_2/[\sqrt\pi\,N\sqrt{N-1}]$ for $N\ge2$. Faster Fourier decay gives a better explicit remainder.

For an even unimodal $C^1$ density, $A$ also has the nonnegative real-space representation

```math
A=\frac1{4\pi}\int_{-\pi}^{\pi}
\frac{w-H(t)}{\sin^2(t/2)}\,dt\ge0.
```

It follows directly from

```math
\Delta_M=\frac1{4\pi N}\int_{-\pi}^{\pi}
[1-\cos(Nt)]\frac{w-H(t)}{\sin^2(t/2)}\,dt.
```

The quotient is integrable because $w-H(t)=O(t^2)$ at zero. Therefore $\Delta_M\le2A/N$, and the Riemann–Lebesgue lemma gives the displayed asymptotic. One may use the smallest available constant

```math
B_1=\min\left\{\frac{\pi^2L}{2},\ B_{\rm F},\ 2A\right\}
\quad\Longrightarrow\quad
0\le\Delta_M\le\frac{B_1}N.
```

The $2A$ option requires the nonnegative integrand, hence the unimodal hypothesis. When $A\gt 0$, the order $1/N$ is the actual convergence rate of this flat-envelope decoder. It is not a lower bound on all codes with the same energy.

### 2.3 Bounded and bounded-variation densities

Smoothness is relevant to the rate. For $p\in L^\infty$, let $\mathrm{osc}(p)=\mathrm{ess\,sup}\,p-\mathrm{ess\,inf}\,p$. The translated interval mass is Lipschitz with constant at most $\mathrm{osc}(p)$, because $H'(t)=p(a+t)-p(-a+t)$ almost everywhere. Consequently,

```math
|F_M-w|\le\mathrm{osc}(p)\,\mu_{1,N},
\qquad
\mu_{1,N}=\int_{-\pi}^{\pi}\frac{K_N(t)}{2\pi}|t|\,dt.
```

Using $K_N(t)\le\min\{N,\pi^2/(Nt^2)\}$ and splitting the integral at $\pi/N$ gives the explicit estimate

```math
\mu_{1,N}\le\frac\pi N\left(\log N+\frac12\right).
```

For a periodic density of total variation $V(p)$, $\mathrm{osc}(p)\le V(p)/2$, which gives a bounded-variation bound of order $\log N/N$.

The logarithm cannot be removed uniformly for this flat construction. For the box density $p=\mathbf1_{[-a,a]}/(2a)$, with $d\ge2$, $w=1$ and $H(t)=\max\{1-|t|/(2a),0\}$ on the principal circle. Substitution into the kernel integral yields

```math
1-F_M=\frac{\log N}{\pi aN}+O(N^{-1}).
```

This example has a jump exactly at the decision boundary. Its slower rate is compatible with the $C^1$ bounds, whose hypotheses it does not satisfy.

## 3. A sine envelope improves the smooth-density rate

Keep the same quotient/remainder decoder, but allow a common normalized real gauge envelope,

```math
V_g|j\rangle=\sum_{k=0}^{M-1}g_k|dk+j\rangle,
\qquad \sum_k g_k^2=1.
```

The logical codewords remain orthonormal because their Fock supports have distinct residues. Put

```math
v_n=\frac{g_{\lfloor n/d\rfloor}}{\sqrt d},
\qquad
P_g(z)=\sum_{n=0}^{N-1}v_nz^n,
\qquad
Q_g(t)=|P_g(e^{-it})|^2.
```

Then $\int Q_g(t)dt/(2\pi)=1$, and the same decoder calculation gives

```math
F_g=\int_{-\pi}^{\pi}\frac{Q_g(t)}{2\pi}H(t)\,dt.
```

For direct calculation, let $c_r=\sum_{n=0}^{N-1-r}v_nv_{n+r}$. Then

```math
F_g=\frac1d+\frac2\pi\sum_{r=1}^{N-1}
c_r\mathrm{Re}\,\widehat p(r)\frac{\sin(ra)}r.
```

Choose the standard sine envelope [3],

```math
g_k=\sqrt{\frac2{M+1}}\sin\left[\frac{\pi(k+1)}{M+1}\right].
```

It is symmetric about $(M-1)/2$, so every photon-number entry in the resource ledger remains unchanged. Its adjacent gauge overlap is

```math
\sum_{k=0}^{M-2}g_kg_{k+1}=\cos\frac\pi{M+1}.
```

This identity follows by viewing $g$ as the normalized first eigenvector of the path adjacency matrix. There are $d-1$ adjacent pairs within each repeated block and one pair between blocks. Hence its exact first circular moment is

```math
\int\frac{Q_g(t)}{2\pi}[1-\cos t]\,dt
=1-c_1
=\frac{1-\cos[\pi/(M+1)]}{d}.
```

Since $t^2\le(\pi^2/2)(1-\cos t)$ for $|t|\le\pi$, the derivative argument above gives

```math
0\le w-F_{\rm sine}
\le\frac{\pi^2L}{2d}
\left(1-\cos\frac\pi{M+1}\right)
\le\frac{\pi^4L}{4d(M+1)^2}.
```

The absolute-value version holds for a general Lipschitz density. At fixed $d$ and $p$, this is a rigorous $O(N^{-2})$ approximation with the same cutoff and mean energy as the flat comb. The improvement comes from the known smoother phase-reference state, not from changing the universal optimum or asserting a new code family.

## 4. Converting finite fidelity into diamond error

The raw finite decoder is a random diagonal-rotation channel. Its half-diamond error is generally **not** $1-F_g$ for $d\gt 2$. A generic bound, if no twirl is used, is

```math
1-F_g\le\varepsilon_\diamond(\Lambda_g)
\le\min\{1,\ d\sqrt{1-F_g}\}.
```

The upper bound follows from the normalized Choi-state inequality
$\|\Lambda-\mathrm{id}\|_\diamond\le d\|J(\Lambda)-|\Phi_d\rangle\langle\Phi_d|\|_1$
and the pure-target trace-distance bound. It is conservative and need not approach the optimal phase floor at the correct rate.

The [allowed classical-record model](01-model-and-question.md) permits a sharper construction. Choose $q$ uniformly from $\{0,\ldots,d-1\}$, apply $X^q$ before encoding, retain $q$ classically, and apply $X^{-q}$ after recovery, where $X|j\rangle=|j+1\bmod d\rangle$. The resulting cyclic twirl preserves entanglement fidelity. For the phase-only Schur channel it produces a random $Z_d$ channel, and therefore

```math
\varepsilon_\diamond(\widetilde\Lambda_g)=1-F_g.
```

This is an equality for the actual finite implementation. The resource is a classical seed independent of the input and noise; there is no coherent bypass, phase side information, or postselection. Averaging the seed also makes the physical mean energy equal to $(N-1)/2$ for every input.

After adding pure loss, the raw logical channel remains covariant under $Z_d$. The encoder intertwines logical $Z_d$ with the physical rotation $e^{-2\pi i\hat n/d}$; both the loss channel and the decoder respect that covariance. The cyclic $X$ twirl is then equivalent to the full logical Weyl twirl. Its Choi state is diagonal in the generalized Bell basis, so it is a random Weyl channel and again satisfies

```math
\varepsilon_\diamond(\widetilde\Lambda_g^{\rm loss+phase})
=1-F_e(\Lambda_g^{\rm loss+phase}).
```

Thus the fidelity estimates below are diamond guarantees for a fully specified admissible implementation. They are not assertions about the untwirled channel.

## 5. Pure loss: an exact hard-cutoff distance

Write $\mathcal A_\eta$ for the quantum-limited pure-loss channel with $0\le\eta\le1$. Its standard Kraus operators [4,5] act as

```math
A_\ell|n\rangle=
\begin{cases}
\sqrt{\binom n\ell}(1-\eta)^{\ell/2}\eta^{(n-\ell)/2}|n-\ell\rangle,&n\ge\ell,\\
0,&n\lt \ell.
\end{cases}
```

In particular $A_0=\eta^{\hat n/2}$. Put $s=-\log\eta$ when $\eta\gt 0$; for Markov loss of rate $\kappa_1$ over time $\tau$, $s=\kappa_1\tau$.

On the input subspace $\mathcal H_{n_{\max}}=\mathrm{span}\{|0\rangle,\ldots,|n_{\max}\rangle\}$, the exact restricted distance is

```math
\frac12\|\mathcal A_\eta-\mathrm{id}\|_{\diamond,\mathcal H_{n_{\max}}}
=1-\eta^{n_{\max}}.
```

Here the restriction is a **hard support cutoff**, not a constraint only on mean energy. The identity has the same oscillator output space. This elementary lemma is used as a continuity estimate, not proposed as a separate novelty claim.

### Proof, including entangled inputs

It suffices to consider a pure state $|\psi\rangle$ of the cutoff system and an arbitrary reference. Let $B=A_0\otimes I_R$, $b=\langle B\rangle$, $c=\langle B^2\rangle$, and $\alpha=\eta^{n_{\max}/2}$. Then $\alpha I\le B\le I$. The output is

```math
|\phi\rangle\langle\phi|+\sigma,
\qquad |\phi\rangle=B|\psi\rangle,
\qquad \sigma\ge0,\quad\mathrm{Tr}\,\sigma=1-c.
```

The rank-two trace-norm identity and the triangle inequality give

```math
D\le\frac12\left[\sqrt{(1+c)^2-4b^2}+1-c\right].
```

The scalar inequality $x^2\le(1+\alpha)x-\alpha$ for $x\in[\alpha,1]$ implies $b\ge(c+\alpha)/(1+\alpha)$. For $0\le\alpha\lt 1$, write $u=(1-c)/(1-\alpha^2)\in[0,1]$. Substitution yields

```math
D\le\frac{1-\alpha}{2}
\left[u(1+\alpha)+\sqrt{u^2(1+\alpha)^2+4u(1-u)}\right]
\le1-\alpha^2.
```

The last inequality follows by squaring the nonnegative proposed bound on the square root: the difference of the squared right and left sides is
$4(1-u)[(1+\alpha)^2-u]\ge0$. This also covers $\alpha=0$; $\alpha=1$ is the identity channel. Convexity covers mixed reference-assisted inputs. Finally, the input $|n_{\max}\rangle$ loses at least one photon with probability $1-\eta^{n_{\max}}$, and those outputs are orthogonal to the input. It attains the bound. For $n_{\max}=0$, both sides are zero, with the natural convention $\eta^0=1$.

Contractivity immediately gives, for either finite code and its chosen recovery,

```math
\varepsilon_\diamond^{\rm loss+phase}
\le\varepsilon_\diamond^{\rm phase}+1-\eta^{N-1}
\le\varepsilon_\diamond^{\rm phase}+s(N-1).
```

The following code-specific estimate improves the leading loss constant.

## 6. A stronger loss bound for both envelopes

The no-loss Kraus branch replaces $P_g(e^{-it})$ by $P_g(r e^{-it})$, where $r=\sqrt\eta$. Its contribution to entanglement fidelity is exactly

```math
F_g^{(0)}(\eta)
=\int_{-\pi}^{\pi}p(\theta)\,
\frac1{2\pi}\int_{\theta-a}^{\theta+a}
|P_g(r e^{-it})|^2\,dt\,d\theta.
```

Every other Kraus branch contributes a nonnegative amount to entanglement fidelity. Thus $F_g^{\rm loss+phase}\ge F_g^{(0)}$.

Both envelopes used here have amplitude polynomials with every zero on the unit circle. For the flat comb this is the geometric polynomial. For the sine envelope, put $t_0=\pi/(M+1)$ and use

```math
P_g(z)=\frac1{\sqrt d}\left(\sum_{j=0}^{d-1}z^j\right)
\left(\sum_{k=0}^{M-1}g_k z^{dk}\right),
```

together with

```math
\sum_{k=0}^{M-1}\sin[(k+1)t_0]y^k
=\frac{\sin t_0(1+y^{M+1})}{1-2y\cos t_0+y^2}.
```

The denominator cancels two roots of the numerator; the remaining roots have unit modulus. Taking roots of order $d$ and multiplying by the geometric factor preserves that property. The case $M=1$ is included by the cancellation identity.

For $|\zeta|=1$ and $|z|=1$,

```math
|rz-\zeta|^2=(1-r)^2+r|z-\zeta|^2\ge r|z-\zeta|^2.
```

Factoring the degree $N-1$ polynomial therefore proves the pointwise inequality

```math
|P_g(rz)|^2\ge r^{N-1}|P_g(z)|^2.
```

Integration gives the promised bound, valid for any phase density:

```math
F_g^{\rm loss+phase}\ge\eta^{(N-1)/2}F_g^{\rm phase},
\qquad
\varepsilon_\diamond(\widetilde\Lambda_g^{\rm loss+phase})
\le1-e^{-sE_{\rm av}}F_g^{\rm phase}.
```

For these symmetric envelopes, the bound is also first-order sharp in $s$ for this fixed encoder and decoder:

```math
F_g^{\rm loss+phase}(e^{-s})
=F_g^{\rm phase}-sE_{\rm av}F_g^{\rm phase}+O(s^2),
\qquad d\ge2.
```

To see this, symmetry $v_n=v_{N-1-n}$ makes the derivative of
$|P_g(e^{-s/2-it})|^2$ at $s=0$ equal to $-E_{\rm av}|P_g(e^{-it})|^2$. A one-photon-loss Kraus operator shifts the logical residue by one and has zero logical trace. More generally only losses divisible by $d$ contribute to entanglement fidelity, so no other branch contributes at first order. This sharpness is about the specified construction, not the unknown joint optimum.

### Exact finite calculation with loss

The full fidelity can be evaluated without phase quadrature. For $\ell=0,d,2d,\ldots,(M-1)d$ and $0\le m\lt N-\ell$, define

```math
b_{\ell,m}=\frac{g_{\lfloor(m+\ell)/d\rfloor}}{\sqrt d}
\sqrt{\binom{m+\ell}{\ell}}
(1-\eta)^{\ell/2}\eta^{m/2},
\qquad
c_{\ell,r}=\sum_{m=0}^{N-\ell-1-r}b_{\ell,m}b_{\ell,m+r}.
```

Then, with $c_{\ell,r}=0$ outside its range,

```math
F_g^{\rm loss+phase}
=\sum_{\ell\in d\mathbb Z_{\ge0},\,\ell\lt N}
\left[
\frac{c_{\ell,0}}d+
\frac2\pi\sum_{r=1}^{N-\ell-1}
c_{\ell,r}\mathrm{Re}\,\widehat p(r)\frac{\sin(ra)}r
\right].
```

This follows by taking the logical trace of each loss-and-phase Kraus operator in the gauge decoder. A loss count not divisible by $d$ changes every logical residue and has zero trace. For a divisible count, the remaining trace is the polynomial with coefficients $\sqrt d\,b_{\ell,m}$; integrating the gauge phase gives the displayed autocorrelation sum. It is an exact formula for this finite protocol, including all loss events. It is not an optimization over other codes.

## 7. Explicit energy–loss tradeoffs

Pure loss is phase covariant and commutes with every random-rotation channel. In the Gaussian Markov case the corresponding loss and dephasing Lindbladians also commute [5]. Hence any recovery after joint noise can be regarded as a recovery after $\mathcal D_p$, with pure loss absorbed into it. The universal phase-only converse remains valid:

```math
F_*^{\rm loss+phase}(d,p,\eta)\le w,
\qquad
\varepsilon_*^{\rm loss+phase}(d,p,\eta)\ge1-w.
```

The inequalities do not assert equality at nonzero loss. Combined with the explicit twirled construction, they give the operational bracket

```math
1-w\le\varepsilon_*^{\rm loss+phase}
\le\varepsilon_\diamond(\widetilde\Lambda_g^{\rm loss+phase})
\le1-e^{-s(N-1)/2}F_g.
```

If $0\le w-F_g\le\delta_N$, then

```math
\varepsilon_\diamond(\widetilde\Lambda_g^{\rm loss+phase})
\le(1-w)+\delta_N+\frac{ws(N-1)}2.
```

The exponential form is tighter; the last expression makes resource choices transparent.

For the flat envelope, use $\delta_N=B_1/N$. Ignoring the integer constraint, the displayed upper bound is minimized at

```math
N_0=\sqrt{\frac{2B_1}{ws}},
```

and its excess above $1-w$ is at most $\sqrt{2B_1ws}$, apart from the favorable $-ws/2$ term. When $N_0\ge d$, choosing $N=d\lceil N_0/d\rceil$ adds at most $wsd/2$. This is a constructive $O(s^{1/2})$ approach to the phase benchmark as loss tends to zero.

For the sine envelope, put

```math
B_2=\frac{\pi^4Ld}{4},
\qquad
\delta_N\le\frac{B_2}{(N+d)^2}\le\frac{B_2}{N^2}.
```

The simpler last bound is minimized against the linear loss term by

```math
N_0=\left(\frac{4B_2}{ws}\right)^{1/3}.
```

Again for $N_0\ge d$, rounding upward to a multiple of $d$ proves

```math
\varepsilon_\diamond(\widetilde\Lambda_{\rm sine}^{\rm loss+phase})
\le(1-w)+
\frac3{2^{4/3}}B_2^{1/3}(ws)^{2/3}
+\frac{wsd}{2}.
```

Thus a fully specified finite-energy protocol approaches the pure-phase optimum with excess error $O(s^{2/3})$ at fixed $d$ and fixed Lipschitz density, using $N=O(s^{-1/3})$ photon levels and $E_{\rm av}=O(s^{-1/3})$. This improves the certified weak-loss tradeoff of the flat comb. Neither exponent is claimed to be optimal among all joint-noise codes. If the continuous minimizer is below $d$, set $M=1$ and use the exact finite formula instead. Uniform phase noise and other zero-constant edge cases should likewise be evaluated directly.

At zero loss, a target excess phase error $\delta\gt 0$ is guaranteed by $N\ge B_1/\delta$ for the flat code. For the sine code it is enough that

```math
M+1\ge\frac{\pi^2}{2}\sqrt{\frac{L}{d\delta}}.
```

These are explicit sufficient resource budgets. They do not give necessary energy requirements.

## 8. A finite numerical example

As a reproducible illustration, take $d=4$, a wrapped Gaussian of variance $0.16$, and $s=10^{-4}$, so $\eta=e^{-10^{-4}}$. These are declared channel parameters, not a forecast for a particular device. The universal phase-only error floor is $0.0495886375$. Evaluating the exact finite formulas gives:

| $M$ | $N$ | $E_{\rm av}$ | Flat code, joint error | Sine code, joint error |
|---:|---:|---:|---:|---:|
| 8 | 32 | 15.5 | 0.08202117 | 0.06540199 |
| 16 | 64 | 31.5 | 0.06803189 | 0.05658696 |
| 32 | 128 | 63.5 | 0.06330150 | 0.05666074 |
| 64 | 256 | 127.5 | 0.06543115 | 0.06188990 |

These are half-diamond errors of the classically twirled protocols, computed by their exact entanglement fidelities. The sine envelope reaches substantially closer to the universal phase floor at the same photon support. Increasing support eventually worsens the joint error because loss outweighs the remaining phase-resolution improvement. The table compares the listed finite constructions; it does not identify the optimum over all codes, or even assert an optimal integer $M$ between the displayed rows.

## 9. Verification and attribution

The standard-library script [check_finite_resources.py](../verification/check_finite_resources.py) checks the resource moments, independent Fourier/Kraus formulas, the sine circular-moment identity, both loss inequalities, and the first-order loss coefficient. It also prints finite-resource examples for both envelopes. The algebraic proofs above establish the statements; the numerical checks guard against normalization, indexing, and metric mistakes.

1. D. Gottesman, A. Kitaev, and J. Preskill, “Encoding a qubit in an oscillator,” *Physical Review A* **64**, 012310 (2001). [DOI](https://doi.org/10.1103/PhysRevA.64.012310), [arXiv](https://arxiv.org/abs/quant-ph/0008040). Shift-resistant oscillator/qudit coding is an inherited ingredient.
2. A. L. Grimsmo, J. Combes, and B. Q. Baragiola, “Quantum computing with rotation-symmetric bosonic codes,” *Physical Review X* **10**, 011058 (2020). [DOI](https://doi.org/10.1103/PhysRevX.10.011058), [full preprint](https://arxiv.org/html/1901.08071v3). Number-phase codes, Pegg–Barnett constructions, and the gauge/phase-correction viewpoint are established.
3. D. W. Berry and H. M. Wiseman, “Optimal States and Almost Optimal Adaptive Measurements for Quantum Interferometry,” *Physical Review Letters* **85**, 5098–5101 (2000). [DOI](https://doi.org/10.1103/PhysRevLett.85.5098), [primary preprint, especially Eq. (10)](https://arxiv.org/pdf/quant-ph/0009117). The sine coefficients and canonical-phase sharpness are inherited; this chapter derives their finite-memory bounds explicitly.
4. J. Solomon Ivan, K. K. Sabapathy, and R. Simon, “Operator-sum representation for bosonic Gaussian channels,” *Physical Review A* **84**, 042311 (2011). [DOI](https://doi.org/10.1103/PhysRevA.84.042311), [arXiv](https://arxiv.org/abs/1012.4266). Standard Gaussian-channel Kraus representations.
5. P. Leviant, Q. Xu, L. Jiang, and S. Rosenblum, “Quantum capacity and codes for the bosonic loss-dephasing channel,” *Quantum* **6**, 821 (2022). [DOI](https://doi.org/10.22331/q-2022-09-29-821), [full preprint, Eqs. (12)–(18)](https://arxiv.org/html/2205.00341v4). Standard loss/dephasing conventions, phase covariance, commuting Lindbladians, and the distinct joint-noise optimization problem.
