# Source audit: WLL's finite-batch leakage reduction

This record identifies the exact primary text supporting [the counterexample](../science/published_reduction.md), the interpretations checked, and the limits of the publication comparison. Source status was checked on October 27, 2026.

## 1. Verified text and publication identity

| Item | Verified information |
| --- | --- |
| Authors | Zhedong Wang, Qiqi Lai, Feng-Hao Liu |
| Title | *Ring/Module Learning with Errors under Linear Leakage—Hardness and Applications* |
| Official ePrint record | <https://eprint.iacr.org/2023/826> |
| Current record's revision date | April 7, 2024; last of four revisions; received June 3, 2023 |
| Publication label on ePrint | A minor revision of an IACR publication in PKC 2024 |
| Full text inspected | 38-page PDF obtained from <https://eprint.iacr.asia/2023/826.pdf> |
| Full-text PDF metadata | Created and modified April 7, 2024, 12:29:56 AEST |
| SHA-256 of inspected PDF | e789941a4e50e126d8e91c8150dfdc4d89858be3d4e2f08b5c60ad07c080702e |
| Publisher record | <https://link.springer.com/chapter/10.1007/978-3-031-57722-2_9> |
| Published identity | PKC 2024, LNCS 14602, pp. 275–304; first online April 14, 2024 |
| Official IACR paper record | <https://iacr.org/cryptodb/data/paper.php?pubkey=33745> |
| Official conference program | <https://pkc.iacr.org/2024/program.php>; linked data at <https://pkc.iacr.org/2024/json/program.json> |

The ePrint landing record, PDF metadata, and the author's publication listing identify the inspected full version with the April 7 revision. Direct retrieval of the official ePrint PDF returned HTTP 403; therefore an official-versus-mirror byte comparison was not performed. The hash above pins the exact text that was audited.

The publisher's public page confirms the authors, title, publication, and broad standard-search-to-leaky-decision claim. Its PDF endpoint redirected to a subscription preview. The official conference program lists paper 110, CryptoDB key 33745, and author slides, but no paper-download URL. CryptoDB likewise offers an ePrint search and the slides rather than a full conference PDF. These sources do **not** establish page-by-page identity of the 30-page conference chapter and the 38-page full version.

Accordingly, the mathematical finding is stated against **the April 7, 2024 full ePrint text as inspected**, not against unverified wording in every publication version. Page numbers below are the printed page numbers of that full text, which also agree with its PDF page positions.

## 2. Hypothesis and quantifier audit

| Point | Primary-text location | Consequence for the counterexample |
| --- | --- | --- |
| Security parameter | §2, p. 9 | The parameter is implicit in algorithms; the construction supplies a uniform growing family. |
| Ring convention | §2.1, p. 10 | Power-of-two cyclotomic rings are explicitly in scope. |
| Module rank one | §2.3, p. 11; introductory Theorem 1.1, p. 3 | Rank one is explicitly identified with Ring-LWE; no positive rank lower bound excludes it. |
| Error distributions | Definitions 2.6–2.8, p. 11; Definitions 3.2–3.5, pp. 12–14 | The formal games allow an error distribution over the ring; no general smallness condition is imposed. |
| Gaussian discussion | §1.2, p. 4 | Gaussian secret/error sampling is motivated by the application; it is not added to Theorem 3.9's hypotheses. |
| Leakage syntax | Definition 3.1, p. 12 | Arbitrary ring vectors and multipliers; one scalar in the base field. Choosing one multiplier equal to one permits any coefficient-linear functional. |
| Choice timing | Definitions 3.2–3.5, pp. 12–14 | Hint vectors are chosen before the random matrix. The evaluation hint satisfies this order. |
| Total leakage | Definitions 3.1, 3.4, 3.5 | The sum of several inner products remains one scalar for the entire batch. |
| Source secret | Definition 3.4, p. 13 | The standard finite-ring uniform-secret interpretation is used. |
| Prime and splitting conditions | Theorem 3.9, p. 15 | Prime modulus, distinct prime-ideal factors, constant residue degree, and modulus at least the square of the factor count. The fully split family meets all four. |
| Automorphism condition | Theorem 3.9, p. 15 | The centered uniform coefficient cube is preserved exactly by the signed-permutation action. |
| Matrix distribution | Definitions 3.4–3.5 | The matrix is uniform, without conditioning away the public cancellation event. |
| Advantage convention | Definitions 3.3 and 3.5, pp. 13–14 | Decision advantage is guessing success minus one half; the chapter explicitly divides its probability gap by two. |
| Search guarantee | Theorem 3.9, p. 15 | The source recovery bound is one minus epsilon divided by eight. The rendered page was inspected. |
| Application congruence | §4.1, p. 23; Gen in §4.2, p. 29 | The additional modulus congruence belongs to the application, not the broad Theorem 3.9 statement. |

The sentence in Lemma 3.14's proof identifying a residue-field size as polynomial in the module rank is not an additional global theorem hypothesis. Reading it as a rank restriction would exclude the growing-dimensional rank-one setting that the introduction expressly claims to cover. The counterexample instead satisfies the conventional requirement that all public parameters, inverse distinguishing advantage, and the stated sample count be polynomial in the security parameter.

## 3. Notation issues do not create the counterexample

Several displayed expressions have notation inconsistencies. The analysis uses their natural finite-ring interpretation and also checks the material alternatives.

| Inconsistency | Interpretation used and robustness |
| --- | --- |
| Definitions 2.6, 3.4, and 3.5 write a uniform draw from the infinite integer ring at places where a finite residue-ring secret is intended. | Use a uniform secret modulo the modulus, represented by centered coefficients. The attack does not rely on an undefined uniform distribution on an infinite set. |
| Definition 3.4's introductory label says secret leakage while the heading, input length, final hardness formula, and surrounding reduction say error leakage. | Use the explicitly described error-only scalar. The information bound also holds for one scalar combining secret and error. |
| Definition 3.5 writes its hint at an undefined x rather than the error vector. | Use the error vector as specified by the game's heading and chosen input dimension. |
| Theorem 3.9 names an error-leakage target but once labels its decision solver with the secret-and-error abbreviation. | The same chosen evaluation hint is legal in either target. With uniform coefficient errors, both relevant secret laws are uniform modulo the modulus. |
| PDF text extraction can flatten the fraction in the recovery bound. | The page image confirms one minus epsilon divided by eight. Even one minus eight epsilon would remain incompatible with the asymptotic source bound; the audited claim is the actual fraction. |

The result is therefore about the stated mathematical resource, not a literal reading of a typographical impossibility.

## 4. The asymptotic prime family has a primary proof

The chapter chooses the least prime congruent to one modulo twice the square of the ring degree. It is larger than twice the square of the degree and splits the power-of-two cyclotomic polynomial completely.

The needed polynomial upper bound follows from:

**Triantafyllos Xylouris, *On Linnik's constant*, arXiv:0906.2749v1.**

- Versioned landing: <https://arxiv.org/abs/0906.2749v1>.
- Versioned full text: <https://arxiv.org/pdf/0906.2749v1>.
- Submitted June 15, 2009; the inspected PDF states June 12, 2009 as its internal revision date.
- The maximum least-prime function is defined on printed p. 6.
- Theorem 1.1 on printed p. 9 gives a power bound with exponent 5.2 and an effective absolute implicit constant.

Only the existence of an absolute polynomial exponent is needed. No unproved prime-distribution heuristic, unproved special sequence of primes, or claim about the latest best exponent is used.

The modulus and a root can be found by enumeration in time polynomial in the security parameter because their numerical values are polynomial in that parameter. The construction is intended to certify an asymptotic family, not efficient practical parameter selection.

## 5. Proof-resource diagnosis

The information-theoretic source upper bound is decisive on its own. The following source observations explain a resource discrepancy without attributing more defects than were checked.

1. **Lemma 3.14, pp. 17–18:** its enlarged sample budget is consumed by many separate decision inputs. A single aggregate source hint does not supply the scalar hint for each input block. The argument does not give a simulator for that missing information under Definition 3.4.
2. **Lemma 3.18, pp. 20–21, including footnote 8:** the proof explicitly obtains multiple tuples with separately selected hint vectors and their individual scalar values. Its appeal to adversarial hint choice does not, under the finite-batch definition, grant multiple scalar responses. This later normal-form step is separate from the direct Theorem 3.9 contradiction.
3. **Lemma 3.11, pp. 16–17, in combination with Lemma 3.17, pp. 19–20:** the inner-product identity under automorphisms is correct. The additional success guarantee required after transforming the hint vector is not a consequence of success for one chosen hint alone. This is recorded as a quantifier obligation; it is not used as an independent theorem that every intermediate lemma fails.

A fresh-hint oracle interpretation supplies a different source. Its total field-valued leakage must be counted, and Theorem 3.8's one-value guessing loss cannot be carried over unchanged. A repair may restrict hint structure, use a different ideal comparison, strengthen the source oracle while accounting for its leakage, or impose additional parameter conditions. This audit does not claim any such repair has already been proved.

## 6. Application boundary

Remark 3.6 (p. 14) explicitly distinguishes chosen hints from the challenger-sampled hints in the application. Theorem 4.5 and Lemma 4.6 (pp. 29–30) use the broad hardness claim as a sufficient premise for a particular commit-and-prove simulation.

The concrete hybrid in Lemma 4.6 samples Gaussian vectors, short challenges, and ternary commitment randomness. It uses a predicate of their inner product. The chosen evaluation functional in the counterexample is not shown to arise with useful probability under that sampling rule, and the predicate exposed by the protocol is not shown to disclose the evaluation test.

Therefore the broad hardness route is invalid under the written game, but the audit does not establish that the random-hint problem or the protocol is insecure. A direct proof for the sampled distribution could still exist. A broad-support observation about short effective hints can help explain why these questions differ, but it is not by itself a computational security proof.

## 7. Bounded correction and related-source check

The current official ePrint record, publisher page, and the author pages at <https://fenghaoliu.github.io/> and <https://faculty.snnu.edu.cn/laiqiqi/en/lwcg/10772/content/112628.htm> displayed no correction notice in the inspected material. This is a bounded observation, not a claim that no correction or private clarification exists.

Two later primary papers were inspected for their treatment of this result:

- Qiqi Lai, Akhil Swarnakar, and Chao-Kai Woo, *Leaky LWE: Learning with Errors with Semi-Adaptive Secret- and Error-Leakage*, IACR Communications in Cryptology 2(3), 2025. [Full primary text](https://cic.iacr.org/p/2/3/21/pdf), §1.4, printed p. 5, treats WLL as a positive exact-leakage reduction. Its discussion of a gap concerns a different paper.
- Katharina Boudgoust, Corentin Jeudy, Erkan Tairi, and Weiqiang Wen, *Hardness of M-LWE with General Distributions and Applications to Leaky Variants*, [ePrint 2025/1472](https://eprint.iacr.org/2025/1472), revision February 25, 2026 / PKC 2026. Section 6.2.1, printed pp. 24–25, including footnote 9, discusses exact linear leakage in the **search** setting and cites WLL's adversarial hint choices. That search result is not a proof of the decision claim contradicted here.

The closest application predecessor is Lyubashevsky–Nguyen–Seiler, *Shorter Lattice-Based Zero-Knowledge Proofs via One-Time Commitments*, PKC 2021. Its [official conference PDF](https://link.springer.com/content/pdf/10.1007/978-3-030-75245-3_9.pdf) was inspected. Section 1.1 discusses one-bit leakage and search equivalence; Definition 3.3, conference pp. 230–231, uses a prescribed sign of an integer inner product. That specific sampled sign bit is different from the chosen modular evaluation functional here. Neither generic bounded-leakage search preservation nor the general possibility of a search/decision distinction is claimed as a new observation.

No comprehensive audit of every later citation was performed. A TCHES 2026 paper citing WLL was identified but not read for this comparison. The source record supports a precisely located counterexample and bounded related-work comparison, not an exhaustive claim of priority.
