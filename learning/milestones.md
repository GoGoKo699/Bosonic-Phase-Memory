# Thirty milestones for understanding Bosonic Phase Memory

This map develops one scientific question: how accurately can an arbitrary logical register survive one unobserved random-phase interval in a single oscillator, after optimizing its encoding and recovery? Its destination is the exact unrestricted-energy benchmark, the finite constructions that approach it, and the physical conclusions that follow under specified noise laws.

The **12 background/preliminary milestones** build from number states and relative phase to quantum channels, reference entanglement, resource definitions, and the complete memory model. The **18 narrative/innovation milestones** then assemble the universal converse and matching construction, establish finite-resource and loss guarantees, and integrate the result's architectural meaning. This allocation gives the quantum-information and oscillator prerequisites room to connect, while placing most of the map on the project's actual argument. Each phase moves from individual objects and mechanisms toward an integrated account.

The single educational anchor is **Steven M. Girvin, _Introduction to Quantum Error Correction and Fault Tolerance_, SciPost Physics Lecture Notes 70 (2023), [arXiv:2111.08894v4][Girvin]**, [DOI](https://doi.org/10.21468/SciPostPhysLectNotes.70). The [Girvin bridge](girvin-bridge.md) provides the selective reading route and translates notation. Numbered anchor sections below refer to that version. They supply foundations and useful comparisons; the repository supplies the exact benchmark, reference-assisted metric arguments, uniform-average converse, channel-convergence proof, and finite-resource estimates. The [primary-literature account](../science/06-prior-work.md) remains separate from this educational anchor.

Dependencies refer to earlier milestone IDs. They describe the structure of the scientific explanation. Canonical definitions, proofs, and quantitative examples remain in the linked science pages; this map identifies the understanding that connects them.

## Phase I: Background and preliminaries — M01–M12

<a name="m01"></a>

### M01 — One oscillator and its number basis

**Central question.** What does it mean for a single physical oscillator to contain a many-dimensional logical register?

**Understanding target.** Distinguish the oscillator's number states $|n\rangle$, its nondegenerate number operator $\hat n$, and a logical system of dimension $d$. An infinite collection of available levels establishes a state-space possibility; it does not establish accurate storage under noise. Photon number is dimensionless, while the excitation energy above vacuum is $\hbar\omega\langle\hat n\rangle$.

**Dependencies and story role.** This is the starting point. It introduces the physical carrier and the logical object whose preservation will be optimized, before choosing a code or a noise measure.

**Conceptual connection.** The distinction between physical levels and logical information is the basis for asking whether more oscillator energy can improve a memory without limit.

**Source pointers.** Project: [Physical channel and notation](../science/01-model-and-question.md#physical-channel-and-notation), and [The memory task](../science/01-model-and-question.md#the-memory-task). Anchor: [Girvin §§6.1–6.2][Girvin].

<a name="m02"></a>

### M02 — Phase rotations and coherence

**Central question.** How can a phase rotation damage stored information while leaving every photon-number population unchanged?

**Understanding target.** Explain the action $U_\theta|n\rangle=e^{-in\theta}|n\rangle$ and distinguish a common overall phase from a relative phase between different number states. A coherence $|n\rangle\langle m|$ acquires the factor $e^{-i(n-m)\theta}$; the same phase uncertainty can therefore affect different number separations differently.

**Dependencies and story role.** Depends on [M01](#m01). It turns the number basis into a concrete error mechanism and establishes why preserving basis labels alone is insufficient.

**Conceptual connection.** Phase sensitivity is controlled by differences of number eigenvalues. This connects the register's spread in number to the difficulty of preserving its superpositions, and later to the modular phase acquired by the gauge subsystem.

**Source pointers.** Project: [Physical channel and notation](../science/01-model-and-question.md#physical-channel-and-notation). Anchor: [Girvin §3.1 and §6.3, Table 4][Girvin].

<a name="m03"></a>

### M03 — A random phase as a quantum channel

**Central question.** How does uncertainty about a phase become a deterministic map on density operators?

**Understanding target.** Interpret $\mathcal D_p(\rho)=\int p(\theta)U_\theta\rho U_\theta^\dagger d\theta$ as averaging over an unobserved classical variable. Understand the circle normalization, why a known offset can be removed, and why the Fourier coefficient $\widehat p(n-m)$ multiplies the corresponding coherence. A wrapped Gaussian phase density is a probability law; it should not be confused with the separate phase-space definition of a bosonic Gaussian channel.

**Dependencies and story role.** Depends on [M01](#m01) and [M02](#m02). It packages the physical error into the channel that every admissible protocol must use.

**Conceptual connection.** Fourier coefficients connect a statistical phase law to measurable quantum coherences, while the density itself will determine the final fidelity optimum.

**Source pointers.** Project: [Physical channel and notation](../science/01-model-and-question.md#physical-channel-and-notation), and the distinction in [Capacities and one-shot communication](../science/06-prior-work.md#capacities-and-one-shot-communication). Anchor: [Girvin §4 and §6.3][Girvin].

<a name="m04"></a>

### M04 — Entanglement with an inaccessible reference

**Central question.** What must a memory preserve when the stored register is part of a larger quantum state?

**Understanding target.** Distinguish the accessible logical register from an untouched reference that may be entangled with it. Preserving the logical register means preserving those correlations as well as its local populations. Understand why the reference used to evaluate a channel is not an extra memory available to the encoder or recovery, and why a reference of dimension $d$ suffices for an input of dimension $d$.

**Dependencies and story role.** Depends on [M03](#m03). It extends the storage task beyond individually selected pure states and prepares the operational error criteria.

**Conceptual connection.** Entanglement distinguishes a quantum memory from a device that measures a classical label and prepares a replacement. That distinction becomes the central obstruction in the converse.

**Source pointers.** Project: [Allowed operations and information](../science/01-model-and-question.md#allowed-operations-and-information), and [Statement and conventions](../science/02-exact-benchmark.md#statement-and-conventions). Anchor: [Girvin §3.2 and §4][Girvin]; the reference-assisted definitions are supplied locally.

<a name="m05"></a>

### M05 — Encoders, recovery, and deterministic channels

**Central question.** What class of physical procedures is included when a theorem optimizes over every encoder and recovery?

**Understanding target.** Read $\Lambda=\mathcal R\mathcal D_p\mathcal E$ as a composition of completely positive trace-preserving maps. Encoding and recovery may use fresh ancillas, measurements, and conditional operations. Every outcome must be included in the overall map. A normalized successful branch, considered without its probability and unsuccessful branches, is a different operational task.

**Dependencies and story role.** Depends on [M03](#m03) and [M04](#m04). It defines the mathematical competitors against which a proposed code will be compared.

**Conceptual connection.** Kraus descriptions express both noise and recovery as quantum operations. This permits a single universal bound to include procedures with very different internal implementations.

**Source pointers.** Project: [Allowed operations and information](../science/01-model-and-question.md#allowed-operations-and-information), and [Statement and conventions](../science/02-exact-benchmark.md#statement-and-conventions). Anchor: [Girvin §4, especially Eqs. (107)–(108), and §4.2][Girvin].

<a name="m06"></a>

### M06 — Learning an error without learning the state

**Central question.** How can a recovery measurement reveal useful error information without revealing the unknown logical amplitudes?

**Understanding target.** Distinguish an error syndrome from a measurement of the logical state. Understand the role of input-independent error information in a recoverable encoding, and the difference between learning a noise label and learning which codeword was present. The later gauge measurement works because its outcome distribution is independent of the logical input at fixed phase.

**Dependencies and story role.** Depends on [M04](#m04) and [M05](#m05). It supplies the conceptual requirement that a useful decoder must satisfy before its explicit oscillator realization is introduced.

**Conceptual connection.** Syndrome extraction connects the general error-correction framework to the quotient/remainder factorization: a degree of freedom can carry information about the disturbance while leaving the logical-reference state unmeasured.

**Source pointers.** Project: [Quotient and remainder](../science/03-constructive-achievability.md#quotient-and-remainder), as the later realization of this principle. Anchor: [Girvin §§4.1–4.2, especially Eqs. (126)–(140)][Girvin].

<a name="m07"></a>

### M07 — Fidelity and operational channel error

**Central question.** Which quantity answers whether the entire register has been preserved, and which answers the worst-case distinguishability question?

**Understanding target.** Distinguish maximally mixed-input entanglement fidelity $F_e$, worst-case reference-assisted fidelity $F_{\mathrm{ref}}$, and half the diamond distance $\varepsilon_\diamond$. The first two are squared pure-state overlaps after purification; the third optimizes operational distinguishability over reference-assisted inputs. Understand $F_{\mathrm{ref}}\le F_e$ and $\varepsilon_\diamond\ge1-F_e$, without assuming equality for every channel.

**Dependencies and story role.** Depends on [M04](#m04) and [M05](#m05). It fixes the success criteria before any optimum is stated.

**Conceptual connection.** One entangled test state can supply a universal lower bound on worst-case error, but matching that bound requires additional structure of the recovered channel.

**Source pointers.** Project: [Error measures](../science/01-model-and-question.md#error-measures), and [Transfer to reference fidelity and diamond error](../science/02-exact-benchmark.md#4-transfer-to-reference-fidelity-and-diamond-error). Anchor: [Girvin §4][Girvin] for quantum operations; the fidelity and diamond conventions are developed in the project.

<a name="m08"></a>

### M08 — Photon support and mean energy

**Central question.** Which resource is being bounded when a finite oscillator encoding is called low energy?

**Understanding target.** Distinguish a hard photon cutoff, the mean photon number for the maximally mixed logical state, and the largest mean over all logical inputs. A mean bound permits small high-number tails; a hard support bound excludes them. Understand why an unrestricted-energy supremum can be approached by a sequence of finite-support codes without being a theorem about the best code at any fixed energy.

**Dependencies and story role.** Depends on [M01](#m01), [M05](#m05), and [M07](#m07). It supplies the resource vocabulary needed to interpret the construction and its physical cost.

**Conceptual connection.** Hilbert-space dimension, photon number, and error suppression are different quantities. Comparing codes meaningfully requires identifying which of them is fixed.

**Source pointers.** Project: [Encoder and photon resources](../science/03-constructive-achievability.md#encoder-and-photon-resources), and [Conventions and resource ledger](../science/04-finite-resources.md#1-conventions-and-resource-ledger). Anchor: [Girvin §6.2, especially Eqs. (206)–(208), and §8.3][Girvin].

<a name="m09"></a>

### M09 — Modular error cells in bosonic codes

**Central question.** Why can a syndrome identify an error only up to a periodic ambiguity?

**Understanding target.** Understand a modular variable as a value known within a repeating cell. Different physical disturbances can produce the same measured representative while differing by a logical operation. This is the geometric idea behind the phase aliases in the number-phase code. Distinguish that angular construction from position-momentum GKP lattices: the shared modular logic does not make their noise models or formulas identical.

**Dependencies and story role.** Depends on [M02](#m02), [M06](#m06), and [M08](#m08). It introduces the ambiguity that a sharper syndrome measurement will not remove.

**Conceptual connection.** Better resolution within a cell and distinguishing different cells are separate tasks. The exact memory limit will arise from the probability of the identity cell.

**Source pointers.** Project: [Construction and inherited ingredients](../science/03-constructive-achievability.md#construction-and-inherited-ingredients), and [Matching logical channel](../science/02-exact-benchmark.md#matching-logical-channel). Anchor: [Girvin §§8.2–8.3][Girvin].

<a name="m10"></a>

### M10 — Phase diffusion and photon loss are different

**Central question.** Why does an encoding that handles phase uncertainty need a separate analysis when photons can be lost?

**Understanding target.** Phase rotations preserve number populations; pure loss transfers population toward lower number states and changes amplitudes even in its no-loss Kraus branch. Interpret transmissivity $\eta$, the no-loss operator $\eta^{\hat n/2}$, and the dependence of loss on photon number. The same added photon support that improves phase resolution can increase exposure to loss.

**Dependencies and story role.** Depends on [M02](#m02), [M03](#m03), [M05](#m05), and [M08](#m08). It identifies a second physical noise mechanism without importing it into the phase-only theorem.

**Conceptual connection.** Noise-adapted coding must account for the actual channel. A small-parameter expansion or a successful phase-only construction does not determine the optimum of the combined channel.

**Source pointers.** Project: [Pure loss: an exact hard-cutoff distance](../science/04-finite-resources.md#5-pure-loss-an-exact-hard-cutoff-distance). Anchor: [Girvin §6.4, especially Eqs. (227)–(238), and §7.2][Girvin].

<a name="m11"></a>

### M11 — A storage interval versus active fault tolerance

**Central question.** Which physical task is being studied when ideal encoding and recovery surround one noisy interval?

**Understanding target.** Distinguish the channel-coding task with ideal endpoint operations from repeated correction with imperfect sensors, ancillas, controls, and gates during storage. The present theorem allows arbitrary endpoint channels but excludes operations inside the interval. It gives neither a preparation-time estimate nor a fault-tolerance threshold for a continuously operated device.

**Dependencies and story role.** Depends on [M05](#m05), [M06](#m06), and [M10](#m10). It locates the memory problem within the broader error-correction setting and identifies which hardware costs are outside its optimization.

**Conceptual connection.** A change in the timing of correction changes the admissible channel factorization. Results for one completed storage interval cannot be assigned to an entire actively corrected lifetime without a new argument.

**Source pointers.** Project: [Allowed operations and information](../science/01-model-and-question.md#allowed-operations-and-information), and [Energy, controls, and additional noise](../science/05-noise-laws-and-architecture.md#energy-controls-and-additional-noise). Anchor: [Girvin §1, especially Fig. 1, and §8.3][Girvin].

<a name="m12"></a>

### M12 — The complete memory question

**Central question.** What precisely is held fixed, what is optimized, and what information can the protocol use?

**Understanding target.** Assemble the model: fixed $d$, fixed known even unimodal $L^1$ phase density, one oscillator with nondegenerate number spectrum, arbitrary deterministic endpoint channels, and no coherent bypass or preshared entanglement across the interval. Retained classical encoding records are allowed in an explicit extension; additional information about the realized phase is a different resource. The theorem optimizes fidelity and diamond error without imposing a photon budget.

**Dependencies and story role.** Integrates [M01–M11](#m01), particularly [M07](#m07), [M08](#m08), and [M11](#m11). It closes the background phase by forming one complete operational question from the preceding concepts.

**Conceptual connection.** The quantifiers and resource boundaries determine what an all-code converse must prove and what a matching construction must actually deliver.

**Source pointers.** Project: [Allowed operations and information](../science/01-model-and-question.md#allowed-operations-and-information), and [Statement and conventions](../science/02-exact-benchmark.md#statement-and-conventions). Anchor: [Girvin §1 and §§6.1–6.2][Girvin].

## Phase II: Narrative and innovation — M13–M30

<a name="m13"></a>

### M13 — A code's phase-response function

**Central question.** How can the performance of an arbitrarily complicated encoding and recovery be represented by one function of phase?

**Understanding target.** Fix the protocol and define $f(\theta)=F_e(\Lambda_\theta)$ for a deterministic phase. Explain why $0\le f\le1$ and why the noisy-channel fidelity is $\int p(\theta)f(\theta)d\theta$. The protocol is held fixed while the phase is varied; optimizing a separate recovery for every known phase would change the task.

**Dependencies and story role.** Depends on [M03](#m03), [M05](#m05), [M07](#m07), and [M12](#m12). It begins the narrative with the local mathematical object that makes the universal converse possible.

**Conceptual connection.** Linearity in the channel turns quantum-memory performance into a weighted response problem while retaining the restrictions that make the response physically realizable.

**Source pointers.** Project: [The protocol's phase response](../science/02-exact-benchmark.md#1-the-protocols-phase-response). Anchor: [Girvin §4][Girvin]; the response-function reduction is supplied by the local proof.

<a name="m14"></a>

### M14 — Uniform averaging and the fidelity budget

**Central question.** What constraint must every physical phase-response function obey, regardless of the chosen code?

**Understanding target.** Follow uniform averaging from $U_\theta$ to complete dephasing in the nondegenerate number basis, and then to a measure-and-prepare logical channel. Its maximally entangled overlap is at most $1/d$, giving $\int f(\theta)d\theta\le2\pi/d$. Conditional recovery from a retained classical encoding record still has this property.

**Dependencies and story role.** Depends on [M02](#m02), [M04](#m04), [M05](#m05), and [M13](#m13). It supplies the code-independent restriction that the remaining converse will exploit.

**Conceptual connection.** The oscillator's nondegenerate spectrum makes complete phase uncertainty destroy entanglement. Classical information can guide preparation afterward, but cannot turn that averaged channel into an entanglement-preserving memory.

**Source pointers.** Project: [Uniform phase averaging destroys the oscillator's entanglement](../science/02-exact-benchmark.md#2-uniform-phase-averaging-destroys-the-oscillators-entanglement). Anchor: [Girvin §3.2 and §4][Girvin] for the quantum-operation setting; the entanglement-breaking bound is proved locally.

<a name="m15"></a>

### M15 — Why unimodality selects one central cell

**Central question.** Where should a bounded response with a fixed integral budget be placed to collect the greatest probability mass?

**Understanding target.** Understand the threshold argument that compares $f$ with the indicator of $[-\pi/d,\pi/d]$. Evenness and monotonic decrease away from zero make this interval the highest-density set of the required angular measure. The argument establishes $F_e\le w_d(p)$ without assuming that the discontinuous indicator is a physical finite-code response.

**Dependencies and story role.** Depends on [M09](#m09), [M13](#m13), and [M14](#m14). It converts the uniform budget into the sharp upper bound for the stated density class.

**Conceptual connection.** A probability-mass optimization links the noise law to the geometry of a correctable phase cell. For a multimodal density the best measurable set can be disconnected, and the same converse does not automatically provide a matching code.

**Source pointers.** Project: [Unimodality puts the allowed response under the central peak](../science/02-exact-benchmark.md#3-unimodality-puts-the-allowed-response-under-the-central-peak), and [Edge cases and scope](../science/02-exact-benchmark.md#edge-cases-and-scope). Anchor: [Girvin §8.3][Girvin] for the error-cell comparison; the concentration proof is local.

<a name="m16"></a>

### M16 — From a fidelity converse to operational bounds

**Central question.** What does the fidelity ceiling imply for an arbitrary reference-assisted input or a channel-discrimination experiment?

**Understanding target.** Explain why $F_{\mathrm{ref}}\le F_e\le w_d(p)$ and why the maximally entangled input gives $\varepsilon_\diamond\ge1-F_e\ge1-w_d(p)$. These are bounds for every admissible protocol. At this stage they do not establish that any code approaches the bounds, or that fidelity and diamond error coincide for a general recovered channel.

**Dependencies and story role.** Depends on [M07](#m07) and [M15](#m15). It completes the universal converse in all three stated metrics before turning to achievability.

**Conceptual connection.** A single witness of lost entanglement can constrain the worst possible memory error. Equality requires a construction whose residual errors can be identified in the appropriate channel norm.

**Source pointers.** Project: [Transfer to reference fidelity and diamond error](../science/02-exact-benchmark.md#4-transfer-to-reference-fidelity-and-diamond-error). Anchor: [Girvin §4 and §4.2][Girvin] for the channel/recovery framework; the metric inequalities are derived locally.

<a name="m17"></a>

### M17 — The finite comb and quotient–remainder split

**Central question.** How can one oscillator carry both an unknown logical state and information useful for estimating its phase error?

**Understanding target.** Interpret $V_M|j\rangle=M^{-1/2}\sum_{k=0}^{M-1}|dk+j\rangle$ as an isometric encoding with distinct number residues. Under $|dk+j\rangle\mapsto|k\rangle_G|j\rangle_L$, a phase rotation factors into a gauge state depending on $d\theta$ and a logical rotation depending on $\theta$. This factorization also holds with an inaccessible reference. The photon cutoff is $N-1$ with $N=dM$.

**Dependencies and story role.** Depends on [M06](#m06), [M08](#m08), [M09](#m09), and [M12](#m12). It introduces the explicit finite code that will meet the converse in the limit.

**Conceptual connection.** Redundancy is stored in the quotient coordinate while logical information occupies the remainder. The number-phase construction is inherited; its comparison against every admissible code is the project's claim.

**Source pointers.** Project: [Encoder and photon resources](../science/03-constructive-achievability.md#encoder-and-photon-resources), [Quotient and remainder](../science/03-constructive-achievability.md#quotient-and-remainder), and [Established number-phase constructions](../science/06-prior-work.md#established-number-phase-constructions). Anchor: [Girvin §6.1 and §8.2][Girvin].

<a name="m18"></a>

### M18 — Gauge phase measurement and a complete recovery

**Central question.** What actual measurement and conditional operation turn the quotient coordinate into a valid decoder?

**Understanding target.** Explain the finite-support phase POVM, its principal outcome interval, and the correction $e^{+i\phi J/d}$. The gauge outcome estimates $d\theta$ modulo $2\pi$ without measuring the logical amplitudes. Understand why the recovery includes a complementary outcome outside the occupied gauge support: a channel must be trace preserving on its entire input space, even if the intended phase-noise input never reaches that outcome.

**Dependencies and story role.** Depends on [M05](#m05), [M06](#m06), [M09](#m09), and [M17](#m17). It makes the achievability protocol a complete physical quantum operation.

**Conceptual connection.** Conditional recovery connects syndrome information to an inverse operation, while the branch choice retains the unresolved modular ambiguity.

**Source pointers.** Project: [Gauge phase POVM and correction](../science/03-constructive-achievability.md#gauge-phase-povm-and-correction), and [Conditional logical rotation](../science/03-constructive-achievability.md#conditional-logical-rotation). Anchor: [Girvin §4.2 and §8.3][Girvin].

<a name="m19"></a>

### M19 — Exact finite-code channel formulas

**Central question.** How can the complete finite $M$ protocol be calculated before taking an ideal limit?

**Understanding target.** Understand the Schur coefficients $C^{(M)}_{jh}$ as the factors multiplying logical matrix elements. Their finite sums contain the phase density's Fourier coefficients and the decoder's sinc factors. The identity $D_M(d\delta)D_d(\delta)=D_{dM}(\delta)$ turns entanglement fidelity into a central-window convolution with a Fejér kernel. These formulas are exact for the specified finite code; its raw channel is generally a mixture of continuous diagonal rotations, not yet a discrete phase Pauli channel.

**Dependencies and story role.** Depends on [M03](#m03), [M07](#m07), and [M18](#m18). It provides a finite, reproducible description that will support both convergence and resource estimates.

**Conceptual connection.** Interference among a finite set of number amplitudes controls phase resolution, linking the physical decoder to positive Fourier kernels.

**Source pointers.** Project: [Schur multiplier](../science/03-constructive-achievability.md#schur-multiplier), and [Fejér-kernel identity](../science/03-constructive-achievability.md#fejér-kernel-identity). Anchor: [Girvin §4 and §8.3][Girvin]; the exact Fourier calculation is local.

<a name="m20"></a>

### M20 — Phase aliases and channel convergence

**Central question.** What remains when the gauge estimates phase with arbitrarily fine resolution inside its modular cell?

**Understanding target.** Explain the limiting residual channel $\Lambda_\infty=\sum_r w_r\mathrm{Ad}_{Z_d^r}$, with each $w_r$ equal to a phase-cell probability. Increasing $M$ sharpens the estimate of $d\theta$ modulo $2\pi$; it does not identify the missing alias. The distinct powers of $Z_d$ give orthogonal maximally entangled output states, making the identity-cell probability operationally meaningful. Understand why convergence of every Schur coefficient implies diamond-norm convergence at fixed $d$, and why an $L^1$ density makes the finitely many branch boundaries harmless.

**Dependencies and story role.** Depends on [M04](#m04), [M07](#m07), [M09](#m09), and [M19](#m19). It supplies the full-channel limit required to match the operational converse.

**Conceptual connection.** Finite phase resolution disappears in the limit, while logical ambiguity between cells persists. These are distinct contributions to memory error.

**Source pointers.** Project: [Convergence of the complete logical channel](../science/03-constructive-achievability.md#convergence-of-the-complete-logical-channel), and [Matching logical channel](../science/02-exact-benchmark.md#matching-logical-channel). Anchor: [Girvin §§8.2–8.3][Girvin] for modular errors and physical approximations.

<a name="m21"></a>

### M21 — The exact optimum and its attainment limits

**Central question.** How do a universal upper bound and a convergent physical construction establish an exact answer without an optimal finite code?

**Understanding target.** Combine the converse with the phase-alias channel to obtain $\sup F_e=\sup F_{\mathrm{ref}}=w_d(p)$ and $\inf\varepsilon_\diamond=1-w_d(p)$. Distinguish equality of these optimized values from equality for each protocol. For $d\gt 1$ under the strict threshold condition in the theorem, a normal protocol's continuous response cannot equal the required discontinuous indicator, so the optimum is unattained. The $d=1$ and uniform-density cases are attained and provide useful boundaries.

**Dependencies and story role.** Integrates [M13–M20](#m13), particularly [M16](#m16) and [M20](#m20). It completes the core theorem before introducing quantitative finite-resource refinements.

**Conceptual connection.** A supremum can be physically meaningful through a sequence of normal finite-energy states. It must not be represented by an unnormalizable ideal phase state or by an unsupported maximum claim.

**Source pointers.** Project: [Theorem](../science/02-exact-benchmark.md#theorem), [Continuity and nonattainment](../science/02-exact-benchmark.md#continuity-and-nonattainment), and [Edge cases and scope](../science/02-exact-benchmark.md#edge-cases-and-scope). Anchor: [Girvin §§8.2–8.3][Girvin] for the ideal-versus-physical code distinction.

<a name="m22"></a>

### M22 — A classical twirl converts finite fidelity to error

**Central question.** How can a finite implementation obtain an exact diamond-error guarantee from its computed entanglement fidelity?

**Understanding target.** Explain the independent random cyclic $X$ conjugation and its retained classical seed. For the phase-only Schur channel, this makes the Schur matrix circulant and the logical channel a discrete phase Pauli mixture, while preserving $F_M$. Its identity probability is then exactly $F_M$, so $F_{\mathrm{ref}}=F_M$ and $\varepsilon_\diamond=1-F_M$. These identities apply to the twirled implementation, without claiming finite-energy optimality.

**Dependencies and story role.** Depends on [M05](#m05), [M07](#m07), [M19](#m19), and [M21](#m21). It converts the exact finite-code formula into a sharp operational guarantee.

**Conceptual connection.** Classical randomization can simplify a channel without supplying a coherent bypass. The seed also makes the unconditional mean photon number input independent; conditional energy remains a different quantity.

**Source pointers.** Project: [The optional classical twirl](../science/03-constructive-achievability.md#an-optional-classical-twirl-gives-exact-finite-m-metric-identities), and [Converting finite fidelity into diamond error](../science/04-finite-resources.md#4-converting-finite-fidelity-into-diamond-error). Anchor: [Girvin §3.3, Box 6, and §4][Girvin]; the qudit twirl and metric identities are proved locally.

<a name="m23"></a>

### M23 — What controls the flat comb's convergence rate

**Central question.** How does the regularity of the phase density determine the photon support needed to approach the ideal cell probability?

**Understanding target.** Interpret $F_M$ as a positive-kernel average of the translated interval mass $H(t)$. For a smooth or Lipschitz density, cancellation of the odd part gives a phase gap of order $1/N$ for the flat comb. A jump at the cell boundary can instead produce a $\log N/N$ rate. These are properties of this specified envelope and decoder, not necessary energy requirements for every possible code.

**Dependencies and story role.** Depends on [M08](#m08), [M19](#m19), and [M22](#m22). It turns qualitative convergence into finite-resource estimates with explicit hypotheses.

**Conceptual connection.** The tail structure of a phase-resolution kernel interacts with local behavior of the noise law at the decision boundary. A broad error scaling cannot be assigned without checking both.

**Source pointers.** Project: [A derivative bound with an explicit constant](../science/04-finite-resources.md#21-a-derivative-bound-with-an-explicit-constant), [Fourier bound and the actual leading coefficient](../science/04-finite-resources.md#22-fourier-bound-and-the-actual-leading-coefficient), and [Bounded and bounded-variation densities](../science/04-finite-resources.md#23-bounded-and-bounded-variation-densities). Anchor: [Girvin §8.3][Girvin] for finite-energy approximation; the convergence rates are local.

<a name="m24"></a>

### M24 — A sine envelope improves phase resolution

**Central question.** Can changing the gauge amplitudes improve the finite-resource guarantee while keeping the same logical residues and photon support?

**Understanding target.** Explain how a common sine envelope changes the phase kernel while retaining the quotient/remainder decoder. Its first circular moment gives a phase-gap bound of order $1/[d(M+1)^2]$ for fixed density regularity, or order $d/N^2$. The symmetric envelope preserves the flat code's cutoff and mean-energy ledger. The sine phase-estimation state is inherited; the memory bounds are derived for this task.

**Dependencies and story role.** Depends on [M08](#m08), [M17](#m17), [M19](#m19), and [M23](#m23). It shows how a physically specified finite construction can improve without changing the unrestricted optimum.

**Conceptual connection.** Resource performance depends on amplitude shaping as well as support size. A better sufficient bound for one family does not prove the globally optimal energy-error frontier.

**Source pointers.** Project: [A sine envelope improves the smooth-density rate](../science/04-finite-resources.md#3-a-sine-envelope-improves-the-smooth-density-rate), and [Established number-phase constructions](../science/06-prior-work.md#established-number-phase-constructions) for envelope attribution. Anchor: [Girvin §8.3][Girvin] as a finite-envelope comparison, not as the source of the sine formula.

<a name="m25"></a>

### M25 — Photon loss under a hard cutoff

**Central question.** How much can pure loss change any input that is supported below a known photon number, including one entangled with a reference?

**Understanding target.** Understand the exact restricted half-diamond distance $1-\eta^{n_{\max}}$ and why its restriction is a hard support cutoff. The no-loss branch and the total probability of all loss branches together control the upper bound; the highest Fock state attains it. A mean photon number alone does not supply the same cutoff statement.

**Dependencies and story role.** Depends on [M07](#m07), [M08](#m08), and [M10](#m10). It provides a channel-level continuity estimate for adding physical loss to the finite phase-memory construction.

**Conceptual connection.** A resource restriction can turn an infinite-dimensional noise comparison into a uniform operational guarantee, but only when the restriction used in the proof matches the resource actually reported.

**Source pointers.** Project: [Pure loss: an exact hard-cutoff distance](../science/04-finite-resources.md#5-pure-loss-an-exact-hard-cutoff-distance), and [Proof, including entangled inputs](../science/04-finite-resources.md#proof-including-entangled-inputs). Anchor: [Girvin §6.4][Girvin]; the restricted diamond equality is proved in the project.

<a name="m26"></a>

### M26 — A controlled joint-noise implementation

**Central question.** How can photon support be chosen when better phase resolution and greater loss exposure compete?

**Understanding target.** Explain the code-specific guarantee $F_g^{\mathrm{loss+phase}}\ge\eta^{(N-1)/2}F_g^{\mathrm{phase}}$ and its conversion to a diamond bound by the admissible twirl. Phase covariance preserves the phase-only converse as an upper bound on joint-noise fidelity. Balancing the finite phase gap against loss gives constructive excess-error bounds of order $s^{1/2}$ for the flat envelope and $s^{2/3}$ for the sine envelope, with $s=-\log\eta\to0$ at fixed $d$ and Lipschitz density.

**Dependencies and story role.** Integrates [M10](#m10), [M22–M25](#m22), and the unrestricted benchmark in [M21](#m21). It connects the exact phase theorem to an explicit implementation under an additional noise mechanism.

**Conceptual connection.** The no-loss polynomial structure gives a stronger bound than a generic continuity estimate. Neither that bound nor its optimized scaling determines the globally best joint loss–dephasing code.

**Source pointers.** Project: [A stronger loss bound for both envelopes](../science/04-finite-resources.md#6-a-stronger-loss-bound-for-both-envelopes), [Explicit energy–loss tradeoffs](../science/04-finite-resources.md#7-explicit-energyloss-tradeoffs), and [A finite numerical example](../science/04-finite-resources.md#8-a-finite-numerical-example). Anchor: [Girvin §6.4 and §7.2][Girvin].

<a name="m27"></a>

### M27 — Equal Ramsey coherence, different logical memories

**Central question.** Does one measured coherence decay determine the accuracy of a many-dimensional quantum memory?

**Understanding target.** Compare wrapped Gaussian and wrapped Cauchy phase laws with the same first Fourier coefficient $r=e^{-\chi}$. Their higher coherences and central-cell probabilities differ. At fixed dimension and weak noise, the Gaussian error can be much smaller; at fixed nonzero target error, the Cauchy law can eventually support a larger dimension. Distinguish the exact wrapped formulas from the unwrapped Gaussian tail approximation and its controlled correction.

**Dependencies and story role.** Depends on [M03](#m03), [M15](#m15), and [M21](#m21). It uses the exact theorem to interpret a concrete physical noise comparison.

**Conceptual connection.** A single Ramsey contrast probes one Fourier component, while storing a whole register depends on the distribution of phase uncertainty. Central width and tails affect different operating regimes.

**Source pointers.** Project: [One convention for comparing noise laws](../science/05-noise-laws-and-architecture.md#1-one-convention-for-comparing-noise-laws), [Wrapped Gaussian phase noise](../science/05-noise-laws-and-architecture.md#2-wrapped-gaussian-phase-noise), [Wrapped Cauchy phase noise](../science/05-noise-laws-and-architecture.md#3-wrapped-cauchy-phase-noise-at-the-same-ramsey-contrast), and [Equal Ramsey coherence does not give a universal ordering](../science/05-noise-laws-and-architecture.md#4-equal-ramsey-coherence-does-not-give-a-universal-ordering). Anchor: [Girvin §3.1 and §6.2][Girvin]; both exact noise-law comparisons are local.

<a name="m28"></a>

### M28 — From phase uncertainty to register size and time

**Central question.** What additional information is needed to turn the fidelity benchmark into a storage-time or register-size constraint?

**Understanding target.** Interpret $d=2^k$ for a register of $k$ qubits and invert the central-cell probability at a specified target error. Under exponential Ramsey decay, the Gaussian and Cauchy storage thresholds scale as $d^{-2}$ and $d^{-1}$ at large $d$, respectively; quasistatic Gaussian frequency noise instead gives a $d^{-1}$ time law. The Gaussian $4^{-k}$ storage scaling requires phase variance proportional to time. These concern the whole reference-entangled register and the limiting optimum; finite implementations need a strict error margin and adequate resources.

**Dependencies and story role.** Depends on [M08](#m08), [M11](#m11), [M21](#m21), and [M27](#m27). It translates the probability benchmark into architectural quantities while keeping the dynamical assumptions visible.

**Conceptual connection.** A channel law for one interval and a physical law for how uncertainty accumulates are separate inputs. The time dependence must be supplied before interpreting a dimension penalty as a lifetime penalty.

**Source pointers.** Project: [Exact threshold and dimension scaling](../science/05-noise-laws-and-architecture.md#exact-threshold-and-dimension-scaling), [Dimension and noise budgets](../science/05-noise-laws-and-architecture.md#dimension-and-noise-budgets), and [Translating phase uncertainty into storage time](../science/05-noise-laws-and-architecture.md#5-translating-phase-uncertainty-into-storage-time). Anchor: [Girvin §6.2 and §6.4][Girvin] for oscillator resources and time-dependent noise.

<a name="m29"></a>

### M29 — Which architectural changes evade the benchmark

**Central question.** Which changes alter the problem so that the single-mode optimum no longer applies?

**Understanding target.** Identify how additional coherent modes, phase side information, or correction during the interval change the assumptions. Two modes under a common total-number phase have degenerate fixed-number subspaces and can store information perfectly against that collective noise. For a joint $L^1$ phase density, independent uniform averaging over all phase components instead yields a related probability-volume converse, with no matching general code established here. Conditional phase observations have their own density-dependent upper bound.

**Dependencies and story role.** Depends on [M11](#m11), [M12](#m12), [M14](#m14), [M21](#m21), and [M28](#m28). It locates the architectural conclusions within the exact physical resources that make them valid.

**Conceptual connection.** Nondegeneracy, access to information, and the timing of operations are mathematical premises with direct hardware meanings. Changing one of them can change what uniform averaging destroys.

**Source pointers.** Project: [Why the single-mode assumption matters](../science/01-model-and-question.md#why-the-single-mode-assumption-matters), [Several modes](../science/05-noise-laws-and-architecture.md#several-modes), and [Information about the realized phase](../science/05-noise-laws-and-architecture.md#information-about-the-realized-phase). Anchor: [Girvin §7.2, including its two-mode discussion, and §8.3][Girvin].

<a name="m30"></a>

### M30 — The full contribution and its boundaries

**Central question.** What does the project establish when its theorem, construction, resources, and physical interpretation are considered together?

**Understanding target.** Explain the connected argument: uniform phase averaging bounds every code's response, unimodality selects the central probability mass, and an inherited number-phase construction approaches a matching logical phase channel. The result is an exact unrestricted-energy, single-use optimum for specified reference-assisted metrics. Finite envelopes and loss estimates supply constructive implementations; they do not establish a global finite-energy optimum, a general joint-noise solution, an experimental advantage, or a fault-tolerance threshold.

**Dependencies and story role.** Integrates the narrative, particularly [M21](#m21), [M26](#m26), [M27](#m27), [M28](#m28), and [M29](#m29). It closes the map by connecting the proof to the physical claim and to the precise contribution relative to prior work.

**Conceptual connection.** Code-family analysis, a universal one-use optimum, and asymptotic communication capacity answer different questions. The value of this benchmark is that a known modular recovery exhausts what every allowed code can achieve in the stated memory model.

**Source pointers.** Project: [Theorem](../science/02-exact-benchmark.md#theorem), [What is inherited and what is established here](../science/06-prior-work.md#what-is-inherited-and-what-is-established-here), [Capacities and one-shot communication](../science/06-prior-work.md#capacities-and-one-shot-communication), and [Scientific significance and its limits](../science/06-prior-work.md#scientific-significance-and-its-limits). Anchor: [Girvin §1, §§6.1–6.2, and §10][Girvin] for the larger error-correction setting.

[Girvin]: https://arxiv.org/html/2111.08894v4
