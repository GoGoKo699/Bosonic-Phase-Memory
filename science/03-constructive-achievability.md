# A finite-support code that approaches the benchmark

## Construction and inherited ingredients

The [exact benchmark](02-exact-benchmark.md) is approached by a number-phase comb and a gauge phase measurement. Every member of the sequence is a normal finite-energy encoding with a completely positive trace-preserving recovery. The proof below gives the entire finite $`M`$ logical channel, then establishes diamond-norm convergence to the optimal phase Pauli channel.

The comb, its interpretation as a shift-resistant oscillator code, and phase-based recovery are established ingredients. [Gottesman, Kitaev, and Preskill (2001)](https://doi.org/10.1103/PhysRevA.64.012310) introduced oscillator shift-resistant encodings. [Grimsmo, Combes, and Baragiola (2020)](https://arxiv.org/html/1901.08071v3), particularly Section III and Appendix B.3, identify the connection between Pegg–Barnett number-phase constructions and GKP qudit codes. Canonical phase measurements of number superpositions also appear in the channel-sensing setting of [Huang, Lami, and Wilde (2024)](https://doi.org/10.1103/PRXQuantum.5.020354). The role of this page is to establish their precise performance in the present one-use memory model and match the universal converse; it does not introduce a new code family.

Use the Fourier convention of [the model](01-model-and-question.md):

```math
\widehat p(q)=\int_{-\pi}^{\pi}p(\theta)e^{-iq\theta}\,d\theta.
```

The finite-code formulas and convergence proof apply to any $`L^1`$ phase density. Symmetric unimodality is needed when identifying the resulting central-cell fidelity with the optimum over all protocols.

## Encoder and photon resources

Fix integers $`d\ge1`$ and $`M\ge1`$, set $`N=dM`$, and define

```math
V_M|j\rangle=\frac1{\sqrt M}\sum_{k=0}^{M-1}|dk+j\rangle,
\qquad j=0,\ldots,d-1.
```

Different logical basis vectors have disjoint Fock support, so $`V_M^\dagger V_M=I_d`$. The encoding channel is $`\mathcal E_M(\rho)=V_M\rho V_M^\dagger`$. With

```math
J=\sum_{j=0}^{d-1}j|j\rangle\langle j|,
```

its photon-number operator on the logical input is

```math
V_M^\dagger\hat nV_M=\frac{d(M-1)}2I_d+J.
```

Thus the resources are explicit:

| Quantity | Value |
|---|---:|
| Largest occupied photon number | $`N-1`$ |
| Mean photon number for logical $`I_d/d`$ | $`(N-1)/2`$ |
| Largest mean photon number over logical inputs | $`(N+d-2)/2`$ |

The latter two means are different resources. Entanglement-fidelity calculations use the maximally mixed logical input; an arbitrary encoded input need not have that mean energy.

## A recovery defined on the entire oscillator

### Quotient and remainder

The basis correspondence

```math
W|dk+j\rangle_B=|k\rangle_G|j\rangle_L
```

defines a unitary identification of $`\mathcal H_B`$ with $`\ell^2(\mathbb N_0)_G\otimes\mathbb C^d_L`$. The gauge label is the quotient of photon number by $`d`$, and the logical label is the remainder. This is a mathematical specification of a permitted ideal recovery operation; no additional quantum system carries information around the noisy interval.

For a logical vector $`|\psi\rangle`$ and a deterministic phase,

```math
WU_\theta V_M|\psi\rangle
=|g_M(\theta)\rangle_G\otimes e^{-i\theta J}|\psi\rangle_L,
\qquad
|g_M(\theta)\rangle
=\frac1{\sqrt M}\sum_{k=0}^{M-1}e^{-idk\theta}|k\rangle.
```

The same factorization holds when the logical input is entangled with an inaccessible reference: the gauge vector factors from the logical-reference state. It is therefore legitimate to measure the gauge without learning the logical input.

### Gauge phase POVM and correction

Let

```math
P_M=\sum_{k=0}^{M-1}|k\rangle\langle k|,
\qquad
|e_M(\phi)\rangle=\sum_{k=0}^{M-1}e^{-ik\phi}|k\rangle,
\qquad -\pi\le\phi\lt \pi.
```

The finite-dimensional canonical phase POVM is

```math
\mathsf P_M(d\phi)=|e_M(\phi)\rangle\langle e_M(\phi)|\frac{d\phi}{2\pi},
\qquad
\int_{-\pi}^{\pi}\mathsf P_M(d\phi)=P_M.
```

For outcome $`\phi`$, apply the logical correction

```math
C_\phi=e^{+i\phi J/d}.
```

The principal branch $`[-\pi,\pi)`$ matters: it determines which phase alias is treated as the identity. There are no infinite-norm phase kets in this finite $`M`$ definition.

To make the recovery trace preserving on every oscillator input, include a complementary outcome. For $`\tau=W\sigma W^\dagger`$ and a fixed logical state $`\tau_0=|0\rangle\langle0|`$, define

```math
\begin{aligned}
\mathcal R_M(\sigma)
={}&\int_{-\pi}^{\pi}\frac{d\phi}{2\pi}\,
C_\phi(\langle e_M(\phi)|\otimes I_d)\tau
(|e_M(\phi)\rangle\otimes I_d)C_\phi^\dagger\\
&+\mathrm{Tr}\left[((I_G-P_M)\otimes I_d)\tau\right]\tau_0.
\end{aligned}
```

Both terms are completely positive. The trace of the integral is $`\mathrm{Tr}[(P_M\otimes I_d)\tau]`$, and the second term supplies its complement. This proves trace preservation and defines a normal channel on the full oscillator. For encoded states subject only to phase noise, the complement has probability zero.

The continuous outcome is a convenient description of a finite-input, finite-output channel on the occupied support. That channel has a finite Kraus representation, so the notation does not require retaining an infinitely precise classical record across the storage interval. No classical encoding record is used by this recovery.

### Conditional logical rotation

Write $`D_r(t)=\sum_{k=0}^{r-1}e^{-ikt}`$. The outcome density is

```math
q_M(\phi\mid\theta)
=\frac{|D_M(d\theta-\phi)|^2}{2\pi M}.
```

Conditioned on $`\theta`$ and $`\phi`$, the logical channel is the rotation

```math
\rho\longmapsto
e^{-i(\theta-\phi/d)J}\rho e^{+i(\theta-\phi/d)J}.
```

Consequently the recovered channel $`\Lambda_M=\mathcal R_M\mathcal D_p\mathcal E_M`$ is an average of diagonal rotations. At finite $`M`$ these rotations have a continuous range; they are generally not restricted to powers of the discrete operator $`Z_d`$.

## Exact finite-M logical channel

### Schur multiplier

For $`j,h\in\{0,\ldots,d-1\}`$, define $`C^{(M)}_{jh}`$ by

```math
\Lambda_M(|j\rangle\langle h|)=C^{(M)}_{jh}|j\rangle\langle h|.
```

Directly from the outcome distribution,

```math
C^{(M)}_{jh}
=\int_{-\pi}^{\pi}p(\theta)\,d\theta
\int_{-\pi}^{\pi}\frac{d\phi}{2\pi M}
|D_M(d\theta-\phi)|^2
e^{-i(j-h)(\theta-\phi/d)}.
```

Let $`\mathrm{sinc}(x)=\sin(\pi x)/(\pi x)`$, with $`\mathrm{sinc}(0)=1`$. Expanding the squared Dirichlet sum and integrating first in $`\phi`$ gives the exact finite sums

```math
\boxed{
C^{(M)}_{jh}
=\frac1M\sum_{k,l=0}^{M-1}
\widehat p\bigl(d(k-l)+j-h\bigr)
\mathrm{sinc}\left(k-l+\frac{j-h}{d}\right)
}
```

and, equivalently,

```math
C^{(M)}_{jh}
=\sum_{r=-(M-1)}^{M-1}
\left(1-\frac{|r|}{M}\right)
\widehat p(dr+j-h)
\mathrm{sinc}\left(r+\frac{j-h}{d}\right).
```

In the expansion, the $`\theta`$ factor is $`e^{-i[d(k-l)+j-h]\theta}`$ and the $`\phi`$ factor is $`e^{i[k-l+(j-h)/d]\phi}`$, fixing the Fourier and sinc signs.

The matrix $`C^{(M)}`$ is positive semidefinite, has diagonal entries one, and satisfies $`C^{(M)}_{hj}=(C^{(M)}_{jh})^*`$. These facts also follow from its representation as an average of rank-one matrices with components $`e^{-ij(\theta-\phi/d)}`$. For even $`p`$ it is real. Its entries depend on the ordinary difference $`j-h`$, but generally not only on that difference modulo $`d`$; this is why the finite channel need not be a discrete phase Pauli channel.

Entanglement fidelity is

```math
F_M:=F_e(\Lambda_M)=\frac1{d^2}\sum_{j,h=0}^{d-1}C^{(M)}_{jh}.
```

### Fejér-kernel identity

At fixed phase $`\theta`$, the fidelity response of this decoder is

```math
f_M(\theta)
=\int_{-\pi}^{\pi}\frac{d\phi}{2\pi M}
|D_M(d\theta-\phi)|^2
\frac{|D_d(\theta-\phi/d)|^2}{d^2}.
```

Put $`a=\pi/d`$ and $`\delta=\theta-\phi/d`$. The Jacobian contributes a factor $`d`$, and

```math
D_M(d\delta)D_d(\delta)=D_{dM}(\delta)=D_N(\delta).
```

Thus, for the nonnegative Fejér kernel

```math
K_N(\delta)=\frac1N|D_N(\delta)|^2,
\qquad
\frac1{2\pi}\int_{-\pi}^{\pi}K_N(\delta)\,d\delta=1,
```

the exact response is

```math
\boxed{
f_M(\theta)=\frac1{2\pi}\int_{\theta-a}^{\theta+a}K_N(\delta)\,d\delta.
}
```

Integrals extending beyond $`[-\pi,\pi)`$ use the periodic kernel. In words, the ideal central-cell indicator is smoothed by a normalized Fejér kernel of order $`N=dM`$.

Since

```math
K_N(\delta)=\sum_{q=-(N-1)}^{N-1}
\left(1-\frac{|q|}{N}\right)e^{-iq\delta},
```

integration gives

```math
f_M(\theta)=\frac1d+
\frac2\pi\sum_{q=1}^{N-1}
\left(1-\frac qN\right)\frac{\sin(qa)}q\cos(q\theta).
```

For any real probability density,

```math
\boxed{
F_M=\frac1d+
\frac2\pi\sum_{q=1}^{N-1}
\left(1-\frac qN\right)
\mathrm{Re}\,\widehat p(q)\,\frac{\sin(q\pi/d)}q.
}
```

For the even densities of the theorem, $`\widehat p(q)`$ is real. The formula is a finite sum; no ordinary convergence of the infinite Fourier series of an arbitrary $`L^1`$ density is assumed.

For symmetric unimodal $`p`$, the universal converse ensures $`F_M\le w_d(p)`$, and the limit below gives $`F_M\to w_d(p)`$. No monotonicity in $`M`$ is required or asserted. Quantitative resource bounds and an alternative gauge envelope are treated in [finite resources](04-finite-resources.md).

## Convergence of the complete logical channel

Convergence of one fidelity alone would not establish the optimal diamond error. We therefore prove convergence of the logical channel itself.

For a fixed difference $`s=j-h`$, the conditional Schur coefficient at phase $`\theta`$ can be written as

```math
C^{(M)}_{jh}(\theta)
=e^{-is\theta}\int_{-\pi}^{\pi}
K_M(d\theta-\phi)e^{is\phi/d}\frac{d\phi}{2\pi}.
```

Interpret $`g_s(\phi)=e^{is\phi/d}`$ on $`[-\pi,\pi)`$ and extend it periodically. It is bounded and continuous except possibly at the branch cut. The kernels $`K_M`$ form a positive approximate identity: their integrals are $`2\pi`$, and for every fixed circular distance $`b\gt 0`$ from zero,

```math
K_M(t)=\frac{\sin^2(Mt/2)}{M\sin^2(t/2)}
\le\frac1{M\sin^2(b/2)}
\quad\text{when }b\le|t|\le\pi.
```

Their mass outside any fixed neighborhood of zero therefore vanishes. It follows that the integral converges to $`g_s(\mathrm{wrap}(d\theta))`$ whenever $`d\theta`$ is not at the branch cut modulo $`2\pi`$. Only finitely many $`\theta`$ in the physical circle are excluded. At every other phase,

```math
C^{(M)}_{jh}(\theta)
\longrightarrow
\exp\!\left[-\frac{2\pi i(j-h)\ell(\theta)}d\right],
\qquad
\ell(\theta)=\frac{d\theta-\mathrm{wrap}(d\theta)}{2\pi}.
```

All conditional coefficients have magnitude at most one. Since $`p\in L^1`$, dominated convergence gives

```math
C^{(M)}_{jh}\longrightarrow C^{(\infty)}_{jh}
=\sum_{r=0}^{d-1}w_r e^{-2\pi i r(j-h)/d},
```

where

```math
w_r=\int_{\{\theta:\ell(\theta)\equiv r\ (\mathrm{mod}\ d)\}}
p(\theta)\,d\theta.
```

Thus the limiting channel is

```math
\Lambda_\infty=\sum_{r=0}^{d-1}w_r\mathrm{Ad}_{Z_d^r},
\qquad
Z_d=e^{-2\pi iJ/d}.
```

Its identity probability is $`w_0=\int_{-\pi/d}^{\pi/d}p(\theta)d\theta`$. For even $`d`$, an outer cell can be represented by two intervals adjacent to the ends of $`[-\pi,\pi)`$; the definition modulo $`d`$ already combines them correctly.

Finally, each elementary multiplier $`X\mapsto|j\rangle\langle j|X|h\rangle\langle h|`$ has diamond norm at most one, because left and right multiplication by projections are contractions even with a reference. Hence

```math
\|\Lambda_M-\Lambda_\infty\|_\diamond
\le\sum_{j,h=0}^{d-1}
\left|C^{(M)}_{jh}-C^{(\infty)}_{jh}\right|
\longrightarrow0.
```

This is a fixed-dimension statement. It proves convergence against arbitrary reference-entangled inputs, with no smoothness assumption on $`p`$. The density assumption excludes point masses at the decoder's branch boundaries; a noise law with atoms at those boundaries requires a separate analysis.

The [benchmark proof](02-exact-benchmark.md) establishes

```math
F_e(\Lambda_\infty)=F_{\mathrm{ref}}(\Lambda_\infty)=w_0,
\qquad
\varepsilon_\diamond(\Lambda_\infty)=1-w_0.
```

Diamond continuity transfers these values to the limiting performance of the finite-support sequence. At finite $`M`$, $`F_M`$ is exact, while the raw channel's worst-case reference fidelity and diamond error must be evaluated as their own quantities.

## An optional classical twirl gives exact finite-M metric identities

The raw construction already proves the optimum without a retained classical encoding record. If the model also allows a classical record, an independent random cyclic shift makes the finite $`M`$ channel a phase Pauli channel. This preserves $`F_M`$ and converts it exactly to a reference-fidelity and diamond-error guarantee.

Let $`X|j\rangle=|j+1\bmod d\rangle`$. Choose $`r\in\{0,\ldots,d-1\}`$ uniformly before encoding, retain $`r`$ classically, encode $`X^r\rho X^{-r}`$ with $`V_M`$, and apply $`X^{-r}`$ after $`\mathcal R_M`$. Averaging the seed yields

```math
\widetilde\Lambda_M
=\frac1d\sum_{r=0}^{d-1}
\mathrm{Ad}_{X^{-r}}\circ\Lambda_M\circ\mathrm{Ad}_{X^r}.
```

This is a deterministic protocol in the classical-record extension: all seed values are retained and used, and no branch is discarded. It requires a record with $`d`$ possible values, or $`\lceil\log_2d\rceil`$ binary memory cells. The phase realization is independent of the seed.

Its Schur matrix is

```math
\widetilde C_{jh}
=\frac1d\sum_{r=0}^{d-1}
C^{(M)}_{j+r\bmod d,\,h+r\bmod d}.
```

This matrix is positive semidefinite, has unit diagonal, and is circulant. Define $`c_s=\widetilde C_{s,0}`$, with indices modulo $`d`$. Its Fourier coefficients

```math
\widetilde w_\ell
=\frac1d\sum_{s=0}^{d-1}c_s e^{2\pi i\ell s/d}
\ge0,
\qquad
\sum_{\ell=0}^{d-1}\widetilde w_\ell=1
```

are nonnegative because they are the eigenvalues of the circulant positive matrix divided by $`d`$. Consequently

```math
\widetilde\Lambda_M
=\sum_{\ell=0}^{d-1}\widetilde w_\ell\mathrm{Ad}_{Z_d^\ell}.
```

In particular,

```math
\widetilde w_0
=\frac1{d^2}\sum_{j,h=0}^{d-1}C^{(M)}_{jh}
=F_M.
```

Using the phase Pauli channel identities already proved for $`\Lambda_\infty`$ gives the exact finite-resource relations

```math
\boxed{
F_e(\widetilde\Lambda_M)
=F_{\mathrm{ref}}(\widetilde\Lambda_M)=F_M,
\qquad
\varepsilon_\diamond(\widetilde\Lambda_M)=1-F_M.
}
```

These identities describe this explicit twirled code. They do not assert that it is optimal at a fixed photon cutoff or mean energy. They must also not be assigned to the raw finite $`M`$ channel without an additional argument.

The hard cutoff stays $`N-1`$. For any logical input, averaging over the independent uniform seed gives

```math
\frac1d\sum_{r=0}^{d-1}
\mathrm{Tr}\left[\hat nV_MX^r\rho X^{-r}V_M^\dagger\right]
=\frac{N-1}{2}.
```

Thus the unconditional mean photon number is $`(N-1)/2`$ for every input. Conditioned on a particular seed, the largest mean over logical inputs remains $`(N+d-2)/2`$. The classical record is an explicit resource of this refinement, not a hidden coherent ancillary memory.

## Checks at the boundaries of the construction

For $`d=1`$, every residual logical rotation is trivial, the kernel window is the full circle, and all formulas give $`F_M=1`$ and zero logical error. The vacuum code with $`M=1`$ already suffices.

For a uniform density, $`\widehat p(q)=0`$ at every nonzero integer. The Schur formula gives $`C^{(M)}_{jh}=\delta_{jh}`$, so the raw channel is complete logical dephasing and $`F_M=1/d`$ for every $`M`$.

At $`M=1`$, the gauge is one dimensional and its phase outcome is uniform. The recovery as defined still applies a randomly chosen correction $`C_\phi`$. Its performance is exactly the $`N=d`$ finite-sum formula; it is not implicitly replaced by an optimized decoder for that small code. The construction is chosen for its explicit formulas and convergent sequence, with finite-resource refinements handled separately in [the resource analysis](04-finite-resources.md).
