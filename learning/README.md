# Learning Bosonic Phase Memory

One oscillator has infinitely many energy levels. The question here is how well those levels can preserve an arbitrary quantum register through an unknown phase rotation. Understanding the answer requires connecting three ideas: the coherence that a phase shift changes, the information that recovery can extract without measuring the register, and a bound that applies to every possible encoding.

## One anchor and a project-defined map

The single educational anchor is **Steven M. Girvin, [Introduction to Quantum Error Correction and Fault Tolerance](https://arxiv.org/html/2111.08894v4)**, *SciPost Physics Lecture Notes* 70 (2023), DOI [10.21468/SciPostPhysLectNotes.70](https://doi.org/10.21468/SciPostPhysLectNotes.70). The reading route uses arXiv version 4, dated 6 January 2023.

The [Girvin-to-project bridge](girvin-bridge.md) identifies the useful sections on quantum operations, recovery, oscillator states, photon loss, and bosonic error correction. It translates their notation and explains the additional ingredients supplied by this project. The primary research papers in the [bibliography](../references/README.md) support attribution and specialist proofs; Girvin remains the educational anchor.

The [milestone map](milestones.md) contains exactly **30 understanding targets**. Its allocation follows the scientific story:

| Phase | Milestones | What the phase connects |
|---|---|---|
| Background and preliminaries | M01–M12 | Number states, phase coherence, channels, recovery, reference-assisted errors, and resources become one precise memory problem. |
| Narrative and innovation | M13–M30 | The fidelity-response bound and modular-phase code become an exact optimum, then finite-resource guarantees and architectural consequences. |

Each phase moves from individual objects and mechanisms to a synthesis. Each milestone states its central question, understanding target, dependencies, conceptual connection, and source pointers. The map is shared scientific material; its targets do not depend on a reader's prior knowledge.

## Reading routes

| Starting point | Route |
|---|---|
| Build the physical picture | Read the [bridge](girvin-bridge.md), then follow [M01–M12](milestones.md#m01) alongside the [model](../science/01-model-and-question.md). |
| Understand why the bound is universal | Follow [M13 onward](milestones.md#m13) with the [exact benchmark](../science/02-exact-benchmark.md) and [matching construction](../science/03-constructive-achievability.md). |
| Connect the ideal limit to resources | Read [finite resources](../science/04-finite-resources.md), including the finite classical twirl and the assumptions behind the loss bounds. |
| Interpret the architectural consequences | Read [noise laws and architecture](../science/05-noise-laws-and-architecture.md), then the [prior-work comparison](../science/06-prior-work.md) and the map's final synthesis. |
| Check the numerical examples | Use the [verification guide](../verification/README.md); the general claims remain grounded in their written proofs. |

The route distinguishes three levels throughout: the exact unrestricted-energy benchmark, explicit finite codes that approach it, and the additional resources needed for a physical implementation. In particular, the derived photon-loss guarantees do not assert an exact optimum for combined loss and dephasing.

[Scientific account](../science/README.md) · [Repository overview](../README.md) · [LLM reading guide](../llms.txt)
