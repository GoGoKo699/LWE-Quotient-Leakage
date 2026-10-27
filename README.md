# Quotient Leakage in Module-LWE

## Decision obstructions and a matching norm-parity characterization

An exact leakage value can force a public relation in a Module-LWE transcript. When the relation survives in a small quotient of the coefficient ring, even one scalar or one bit can make the usual independent-random-response comparison distinguishable. The amount of leakage alone does not determine this effect: its algebraic support matters.

This repository gives a complete scientific account of that mechanism. It proves an affine-image law for fixed linear hints, derives an unconditional counterexample to a written finite-batch search-to-decision reduction, and identifies a norm-parity obstruction at every even modulus. For power-of-two parameters and smoothed coefficient Gaussians, a matching reduction shows that ordinary Module-LWE accounts for efficient distinguishing advantage beyond the forced parity relation, with explicit source parameters and losses.

## Main results

Here $`N`$ is the ring degree, $`k`$ the module rank, and $`m`$ the number of ring samples. Every advantage in this table is an acceptance-probability difference.

| Result | Quantitative statement | Proof and scope |
|---|---|---|
| Fixed vector-linear leakage | With $`D_A=H_S-H_EM_A`$, the public consistency test has gap $`\mathbb E_A[1-\lvert\mathrm{Im}\,D_A\rvert/\lvert\mathrm{Im}\,H\rvert]`$. | [Affine-image law](science/linear_leakage.md#theorem-a1-affine-image-law). The gap holds for every hidden law independent of the public matrix; it is the full statistical distance for uniform hidden variables. |
| Scalar hint over a prime residue field | A feasible cancellation event has probability $`p^{-kr}`$ and gap $`(1-1/p)p^{-kr}`$, where $`r`$ is the dimension of the error-hint ideal. | [Ideal-dimension law](science/linear_leakage.md#theorem-a2-scalar-ideal-dimension-law). Includes repeated-root rings; composite coefficient rings use additive image cardinalities. |
| Written finite-batch reduction | For $`N=4,q=17,k=1`$, a legal fixed hint gives decision gap $`16/289`$, while source recovery is at most $`1/4913`$, against the stated lower bound $`288/289`$. | [Counterexample](science/published_reduction.md). A growing polynomial-parameter family gives the asymptotic contradiction. The claim is pinned to the inspected April 7, 2024 full version of Wang–Lai–Liu. |
| Norm parity at even modulus | Leaking $`(\Vert S\Vert^2+\Vert E\Vert^2)\bmod2`$ gives an exact test gap $`2^{-(k+1)}`$, including $`1/4`$ at rank one. | [Norm-parity obstruction](science/norm_parity.md). No Gaussian, independence between secret and error, or small-noise hypothesis is needed. |
| Matching Gaussian reduction | Beyond the parity-preserving ideal, advantage is at most ordinary-MLWE advantage divided by $`p_k>1/4`$, plus $`2\epsilon+2\delta`$. | [Gaussian characterization](science/gaussian_characterization.md#corollary-g4-ordinary-mlwe-characterization). Source modulus $`q/2`$, source width $`t/\sqrt8`$, $`k+m`$ samples; power-of-two ring degree $`N\ge2`$ and modulus $`q\ge4`$, with explicit smoothing. |
| Short or sparse effective hints | For a nonzero effective error coefficient, support size $`u`$ gives $`ru\ge N`$; an integer lift of coefficient norm $`B`$ gives $`p^{N-r}\le B^N`$ in the cyclotomic case. | [Effective-hint bounds](science/linear_leakage.md#when-effective-hints-are-short-or-sparse). These bound the identified cancellation attack and do not prove general leakage hardness. |

The independent-response experiment retains the **genuine marginal distribution of the hint**. The exact Gaussian analysis tracks the small bias of the norm-parity bit; it does not replace that bit by a fair coin without charging the difference.

## The central example

At even modulus, evaluation at one followed by reduction modulo two is a ring homomorphism:

```math
\phi:R_q\to\mathbb F_2,\qquad \phi(f)=f(1)\bmod2.
```

For $`B=AS+E`$ and the leaked norm-parity bit $`c`$,

```math
c+\sum_{i=1}^{m}\phi(B_i)
=\sum_{j=1}^{k}
  \left(1+\sum_{i=1}^{m}\phi(A_{ij})\right)\phi(S_j).
```

All $`k`$ parenthesized coefficients vanish with probability $`2^{-k}`$. On this publicly recognizable event, the response determines the leaked bit. An independent uniform response satisfies the same bit equation with probability one half. The resulting gap is $`2^{-(k+1)}`$.

This relation also specifies the appropriate positive comparison: sample a uniform response, enforce the bit equation on that event, and use an independent fair bit elsewhere. The Gaussian theorem reduces distinguishing the real transcript from this distribution to ordinary Module-LWE at the explicitly changed parameters.

## Reading route

1. [Model and conventions](science/model.md) fixes the ring, leakage experiments, search objective, advantage convention, and computational model.
2. [Linear leakage](science/linear_leakage.md) proves the vector and scalar laws, the composite-modulus extension, and the short-hint bounds.
3. [Norm parity](science/norm_parity.md) explains the even-modulus attack and its relation to known covariance.
4. [Gaussian characterization](science/gaussian_characterization.md) proves the matching positive statement, including the convolution normalizers, normal-form conversion, and finite-precision sampling.
5. [Published-reduction analysis](science/published_reduction.md) gives the fixed-hint counterexample, finite certificate, asymptotic family, and precise source-game distinction.
6. [Interpretation and limits](science/interpretation.md) assembles the cryptographic consequences and boundaries.

[Related work](references/RELATED_WORK.md) compares the nearest results and identifies inherited ingredients. The [WLL source audit](references/wll_source_audit.md) records the inspected version and the limit of the conference-version comparison. Machine-readable citations are in [references.bib](references/references.bib).

## Learning route

The [learning entry point](learning/README.md) connects Chris Peikert's *A Decade of Lattice Cryptography* (2016) to this project. The [Peikert bridge](learning/PEIKERT_BRIDGE.md) translates its notation and assumptions, develops a complete small parity example, and explains the additional leakage and Gaussian arguments. The [30-milestone map](learning/MILESTONES.md) organizes the background and research narrative into a shared sequence of conceptual targets, dependencies, and source pointers.

The learning route complements the direct scientific route above. Exact statements and proofs remain in their topic pages under `science/`.

## Reproduce the finite checks

From the repository root, with Python 3.10 or later and no third-party dependencies:

```sh
python3 verification/run_all.py
```

The four checks cover exact finite linear-leakage distributions, the $`q=17`$ counterexample, norm-parity identities and transcript distances, and the scalar Gaussian convolution identity. They compare their results with committed expected outputs. The Gaussian check uses floating-point arithmetic with a stated tail cutoff; the other distribution checks use exact rational arithmetic. The general theorems are proved in the scientific chapters.

See [verification/README.md](verification/README.md) for the coverage and interpretation of each check.

## Scope

The attacks concern transcripts augmented with the declared leakage. The unconditional reduction counterexample uses uniform coefficient errors; the same chosen quotient hint gives a decision obstruction for arbitrary errors. The counterexample does not establish an attack on Wang–Lai–Liu's specific zero-knowledge protocol, whose hint distribution is more restricted. Its exact publication coverage is stated in the source audit.

The positive theorem concerns the single norm-parity bit. A full norm or covariance reveals that bit, so the negative result transfers to those stronger leakage models at even modulus. The positive result does not establish hardness for the full descriptor. Ordinary Module-LWE hardness, at the listed source parameters and against the chosen class of adversaries, remains an assumption.

## Purpose and contact

This repository serves as a record of the work and a guide for the author’s self-directed learning. For discussion or potential collaboration, please contact Ruge Lin at [gogoko699@gmail.com](mailto:gogoko699@gmail.com).
