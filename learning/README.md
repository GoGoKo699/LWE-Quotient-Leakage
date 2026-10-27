# Learning quotient leakage in Module-LWE

The learning route follows one question: how can a small disclosed value force a visible relation in an otherwise noisy algebraic sample? It connects the coefficient equations to their ring quotients, then separates the information that must remain visible from the computational uncertainty that Module-LWE can still protect.

## One educational anchor

**Chris Peikert, *A Decade of Lattice Cryptography* (2016)** is the educational anchor. Use the [ePrint 2015/939 record](https://eprint.iacr.org/2015/939), revised February 18, 2016. The published survey is in *Foundations and Trends in Theoretical Computer Science* 10(4), pp. 283–424, [DOI 10.1561/0400000074](https://doi.org/10.1561/0400000074). The inspected author manuscript is dated February 17, 2016.

The relevant foundations are lattices and discrete Gaussians in Sections 2.2–2.3, ordinary LWE in Section 4.2, ring geometry in Section 4.3, and Ring-LWE in Section 4.4. The [source-to-project bridge](PEIKERT_BRIDGE.md) identifies which parts are used, translates the notation, and supplies the steps specific to this project. Reading the whole survey is not a prerequisite for following the bridge.

Primary research citations remain in [related work](../references/RELATED_WORK.md) and the scientific chapters. They establish attribution and proof dependencies; Peikert remains the single educational anchor.

## Reading routes

| Reader's aim | Route | Result of the route |
|---|---|---|
| Understand the mechanism through an example | [Peikert bridge](PEIKERT_BRIDGE.md), then [norm parity](../science/norm_parity.md) | Follow a complete small example from ring coefficients to the public event and the exact distinguishing gap. |
| Build the whole conceptual picture | [30-milestone map](MILESTONES.md), with the bridge and linked scientific sources | Connect the background objects, exact leakage law, theorem counterexample, parity obstruction, and matching Gaussian result in dependency order. |
| Check a theorem or proof | [Model and conventions](../science/model.md), then the relevant topic in [the science route](../README.md#reading-route) | Find the canonical assumptions, statement, proof, and interpretation without taking the learning route first. |
| Reproduce a finite calculation | [Verification guide](../verification/README.md) | Run the exact finite checks and the separately identified numerical Gaussian consistency check. |

## The conceptual destination

The [milestone map](MILESTONES.md) contains exactly 30 understanding targets in two phases: background/preliminaries and narrative/innovation. Each phase moves from local objects and mechanisms to a global synthesis. Dependencies and source pointers make the map usable as a shared reading guide.

By the end of the route, the reader can explain why one coefficient and one quotient value can have different leakage effects; why bounded leakage can preserve search hardness while invalidating an independent-response decision comparison; how norm parity exposes a rank-dependent public relation; and how the Gaussian theorem preserves that relation while reducing the remaining distinguishing task to an explicit ordinary-MLWE assumption.

The route also keeps the boundaries attached to those explanations. The algebraic test's exact gap need not be the full distance for nonuniform hidden variables. The WLL counterexample is pinned to the inspected finite-batch source text. The positive Gaussian theorem covers one parity bit, with its stated source modulus, widths, samples, and smoothing conditions. The complete proofs live in the scientific account, which remains authoritative when an illustrative example uses smaller parameters.
