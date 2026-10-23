# Scientific account

The story begins with a resource question: whether the infinite number of levels in one oscillator can make an arbitrary logical register arbitrarily resistant to an unobserved phase rotation. The answer is an exact phase-cell probability. Its derivation connects a universal entanglement constraint to the modular phase measured by an established number-phase code.

| Page | Scientific role |
|---|---|
| [1. Model and question](01-model-and-question.md) | Defines the memory interval, allowed operations, references, photon resources, and the two operational metrics. |
| [2. Exact benchmark](02-exact-benchmark.md) | Proves the universal converse, states the equality theorem, and identifies when the optimum is unattained. |
| [3. Constructive achievability](03-constructive-achievability.md) | Gives the finite-support encoder and gauge measurement, derives exact finite-code formulas, and proves convergence of the logical channel. |
| [4. Finite resources](04-finite-resources.md) | Quantifies finite-energy approximation, improves the envelope, and derives rigorous photon-loss robustness bounds. |
| [5. Noise laws and architecture](05-noise-laws-and-architecture.md) | Evaluates Gaussian and Cauchy laws, explains register-size and time consequences, and compares equal Ramsey coherence. |
| [6. Prior work](06-prior-work.md) | Attributes the code, statistical framework, and existing phase-tail formulas; compares the operational statement with nearby results. |

## Proof dependencies

The exact optimum uses the upper bound in page 2 and the matching sequence in page 3. Page 2 requires only the operational model, the entanglement-breaking property of uniform phase averaging, the maximally entangled overlap bound for separable states, and a scalar concentration inequality. Page 3 supplies an explicit decoder and a finite-dimensional channel limit; it does not assume that an ideal infinite-energy code is a physical state.

Page 4 provides additional finite-resource guarantees. These strengthen the practical account without entering the proof of the unrestricted optimum. Its statements under loss are bounds for explicit constructions and a universal ceiling, not a matching optimization theorem for joint noise.

Page 5 substitutes verified phase densities into the proved benchmark. The Gaussian weak-wrapping formula and limiting scalings are distinguished from exact wrapped probabilities. The comparison at equal Ramsey coherence keeps fixed dimension and fixed target error separate.

The [reproduction guide](../verification/README.md) identifies the finite identities and numerical comparisons that are checked computationally. Those checks support the derivations at their tested parameters; the written arguments establish the general claims.

[Return to the repository](../README.md).
