# Related work and attribution

This comparison concerns the leakage experiments and parameter regimes actually proved in the [scientific account](../science/model.md). Source versions were checked on October 27, 2026. The distinction between secret recovery and decision pseudorandomness, and between a chosen hint and a prescribed random hint, controls the comparison.

## Closest cryptographic results

| Source | Relevant model or result | Relation to this account |
|---|---|---|
| Wang–Lai–Liu, PKC 2024 / [ePrint 2023/826](https://eprint.iacr.org/2023/826), full version April 7, 2024 | Chosen coefficient-linear scalar leakage; finite-batch Definitions 3.1–3.5; search-to-decision Theorem 3.9 and Corollary 3.19. | The fixed quotient hint is legal in the written game. With uniform coefficient errors, the target is distinguishable while the source obeys an unconditional recovery bound. [The counterexample](../science/published_reduction.md) gives the full calculation. The [version audit](wll_source_audit.md) limits the claim to the inspected text. |
| Micciancio–Suhl, [IACR Communications in Cryptology 1(4)](https://cic.iacr.org/p/1/4/2), published January 13, 2025 | Section 5.3 and Definition 12 introduce the ring known-covariance assumption. Appendix B.2 studies an ordinary-LWE known-norm problem under a prime-modulus condition. | At even modulus, the covariance's constant coefficient reveals norm parity and therefore the public relation proved here. The ordinary-LWE theorem is a different, prime-modulus statement. The parity result does not establish a direct break of the full threshold-encryption construction. |
| Anis Bkakria, [ePrint 2026/2638](https://eprint.iacr.org/2026/2638), received October 25 and approved October 26, 2026 | Odd-prime decision attacks on rank-one known-covariance Ring-LWE through public Gram determinants; transfer to composite moduli with suitable odd prime divisors. Sections 6.3 and 9 exclude pure powers of two from that extension. | The augmentation test works at every even modulus and needs only one parity bit. Its module-rank law and the matching positive characterization use a different mechanism. The cited work is a preprint. |
| Lyubashevsky–Nguyen–Seiler, PKC 2021 / [ePrint 2020/1448](https://eprint.iacr.org/2020/1448) | Section 1.1 discusses one-bit leakage and search preservation. Definition 3.3 uses a prescribed sign of an integer inner product; Appendix D treats an unstructured case. | This is a close application predecessor and prior source for bounded-leakage search reasoning. Its sign predicate is different from chosen modular evaluation and norm parity. No attack on that prescribed sign-bit assumption follows from the present tests. |
| Boudgoust–Jeudy–Tairi–Wen, PKC 2026 / [ePrint 2025/1472](https://eprint.iacr.org/2025/1472), revised February 25, 2026 | General-distribution and leaky Module-LWE **search** results. Theorem 4.1 and the subsequent HNF transformation impose their own modulus, entropy, sample, and rank conditions. Section 6.2.1 discusses exact linear leakage. | These results do not give an independent-response decision theorem for the attacked even-modulus parity instance. The search/decision distinction prevents importing them as a repair of the WLL decision claim. |
| Lai–Swarnakar–Woo, [IACR Communications in Cryptology 2(3)](https://cic.iacr.org/p/2/3/21/pdf), 2025 | *Leaky LWE: Learning with Errors with Semi-Adaptive Secret- and Error-Leakage*, with discussion of WLL in Section 1.4. | A later primary comparator for leakage models and the citation history. Its discussion of a gap concerns a different paper; it does not supply the finite-batch repair examined here. |

The separate [norm-parity chapter](../science/norm_parity.md) gives the precise known-covariance projection and parameter distinction. The WLL audit records the finite-batch hint count, chosen-hint quantifier, and application boundary. Those model details are necessary for the conclusions; similarity of paper titles or use of the word “leakage” is insufficient.

## Bounded leakage and search

Guessing a leakage value from a set of size $`L`$ transfers an augmented search solver to an ordinary search solver with loss at most $`L`$. This is an elementary inherited reduction. The one-bit case is discussed in [Lyubashevsky–Nguyen–Seiler, Section 1.1](https://link.springer.com/content/pdf/10.1007/978-3-030-75245-3_9.pdf), and the field-scalar loss appears in Wang–Lai–Liu's Theorem 3.8. The repository includes the short proof to fix the success convention, not to claim that guessing reduction as new.

Search preservation alone does not imply decision pseudorandomness for an augmented transcript. The contribution here is the explicit public affine constraint, its exact module-rank and ideal-dimension dependence, the resulting theorem counterexample, and the parity-specific positive comparison. It is not the general observation that additional leakage can affect decision and search differently.

## Standard algebraic ingredients

The [affine-image theorem](../science/linear_leakage.md#theorem-a1-affine-image-law) uses the fact that a homomorphism sends a uniform element of a finite group to a uniform element of its image. The scalar formula uses coefficient duality in a negacyclic ring and the polynomial-ideal identity

```math
\dim_{\mathbb F_p}(V_1,\ldots,V_m)
=N-\deg\gcd(X^N+1,V_1,\ldots,V_m).
```

These are standard facts. CRT descriptions of ideals and related dimension/support arguments appear, for example, in Evra–Kowalski–Lubotzky's [*Good Cyclic Codes and the Uncertainty Principle*](https://arxiv.org/abs/1703.01080). The support estimate used here is a direct shift-span argument; group-algebra uncertainty results, including sharper versions, are treated by Chen–Fan–Luo in [arXiv:2211.11204v3](https://arxiv.org/abs/2211.11204v3). The coefficient-norm estimate follows from integer Smith normal form and Hadamard's determinant bound.

The specialization made here identifies the error-hint ideal that controls a fixed MLWE leakage game. Its precise finite-distribution formula remains valid in repeated-root residue rings. At composite coefficient modulus, the vector law uses additive image cardinalities and includes proper nonzero residual images. No new CRT theorem, uncertainty principle, or determinant inequality is claimed.

## Gaussian and normal-form ingredients

The positive statement is built from established Gaussian and LWE reductions. The account proves its specialized joint distribution explicitly because the output vector and the leaked parity must remain coupled.

| Ingredient | Primary source and inspected location | Use here |
|---|---|---|
| Smoothing parameter | Micciancio–Regev, [*Worst-Case to Average-Case Reductions Based on Gaussian Measures*](https://cseweb.ucsd.edu/~daniele/papers/Gaussian.pdf), SIAM Journal on Computing 37(1), 2007 | The dual Gaussian-mass definition and the smoothing framework. |
| Translated Gaussian mass | Gentry–Peikert–Vaikuntanathan, [author full version](https://people.csail.mit.edu/cpeikert/pubs/trap_lattice.pdf), Lemma 2.7 and Corollary 2.8; Peikert, [author full version](https://sites.cc.gatech.edu/fac/cpeikert/pubs/pargauss.pdf), Lemma 2.4 | The theta factor is nearly constant above smoothing. The repository derives the particular Poisson-summation and likelihood-ratio bounds used. |
| Integer-lattice smoothing bound and convolution | Peikert, *An Efficient and Parallel Gaussian Sampler for Lattices*, CRYPTO 2010; full version April 13, 2011, Lemma 2.5 and Theorem 3.1 | An explicit sufficient width and context for Gaussian convolution. The $`2U+V`$ specialization retains both normalizers. |
| One-dimensional Gaussian sampling | Gentry–Peikert–Vaikuntanathan, Section 4.1, Lemmas 4.2–4.3 | Coordinatewise finite-precision sampling. The proof accounts for the total product-sampler error $`\delta`$. |
| Normal form | Applebaum–Cash–Peikert–Sahai, [*Fast Cryptographic Primitives and Circular-Secure Encryption Based on Hard Learning Problems*](https://www.wisdom.weizmann.ac.il/~bennyap/pubs/kdm-learning.pdf), CRYPTO 2009, Lemma 2 | Eliminate a uniform secret using an invertible sample block. The local-ring specialization here proves its own invertibility probability and exact $`k`$-sample cost. |
| Modulus transformations | Brakerski–Langlois–Peikert–Regev–Stehlé, [*Classical Hardness of Learning with Errors*](https://arxiv.org/abs/1306.0281), STOC 2013, Theorem 3.1 | Prior general modulus-and-dimension machinery. The integral doubling map used here has a separately proved joint law with parity. |

The specialized conclusion is a reduction from the norm-parity transcript to its explicitly samplable parity-preserving ideal. For power-of-two parameters it uses an ordinary uniform-secret MLWE source at half the target modulus and width $`1/\sqrt8`$ of the target width. The theorem does not claim a new general convolution method, nor hardness for a full norm or covariance descriptor.

## Contribution and limits of the comparison

After the inherited ingredients are credited, the account establishes a connected set of results: the leakage-image law; the concrete and asymptotic contradiction to the inspected WLL finite-batch theorem; the even-modulus norm-parity gap and its rank dependence; and the matching Gaussian characterization with genuine-marginal and finite-sampling errors accounted for.

The exact WLL source version is pinned in [the audit](wll_source_audit.md). Full text of the proceedings chapter was unavailable, so identical wording across publication versions is not assumed. The literature comparison is scoped to these models and claims; it is not a claim to have exhausted every later citation or every possible leakage distribution.

Bibliographic metadata is collected in [references.bib](references.bib).
