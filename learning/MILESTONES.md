# Milestones: quotient leakage in Module-LWE

This route follows one question through the project: when an exact hint forces a public relation, what random comparison remains appropriate, and what hardness statement can still be proved? Its single background anchor is Chris Peikert, [*A Decade of Lattice Cryptography* (2016)][anchor]. Section and page pointers below use the printed pagination of the full version dated February 17, 2016.

The allocation follows the argument. **Phase I has 10 milestones** for the residue-ring model, conditional distributions, search and decision, and the Gaussian tools needed by the positive reduction. It ends by assembling those ingredients into the exact augmented experiment. **Phase II has 20 milestones**: five develop the algebraic law, five analyze the finite-batch reduction, three establish the norm-parity obstruction and its compatible ideal, five prove the Gaussian characterization, and two delimit and synthesize the conclusions. General lattice algorithms, unrelated constructions, and a history of lattice cryptography are outside this route because they are not dependencies of these results.

Peikert supplies the background vocabulary and established reduction techniques. The project chapters supply the new calculations and their exact scope. WLL24, Micciancio-Suhl, Bkakria, Xylouris, and the original Gaussian and normal-form papers remain primary research citations in [related work](../references/RELATED_WORK.md) and the linked chapters; they are not additional background anchors. The survey's historical statements are read in their 2016 context.

The notation follows the [model](../science/model.md): $`N`$ is ring degree, $`k`$ module rank, $`m`$ the number of ring samples, $`q`$ the sample modulus, and $`p`$ a prime residue modulus. The symbols $`s,t`$ denote source and target Gaussian widths. Each milestone names a question, the understanding it supports, its dependency and role in the argument, a conceptual connection, and precise source pointers.

## Compact overview

| ID | Mathematical focus | Role in the argument |
|---|---|---|
| [M01](#m01) | Residues, cosets, and integer lifts | Fix the objects represented by a transcript. |
| [M02](#m02) | Module equations and structured coefficient matrices | Separate module rank from coefficient dimension. |
| [M03](#m03) | Coefficient pairings and norm conventions | Put linear and norm leakage in one notation. |
| [M04](#m04) | Images, ideals, and quotient size | Establish the counting language for public constraints. |
| [M05](#m05) | Search, decision, and the complete transcript | Specify the task and its random comparison. |
| [M06](#m06) | What bounded leakage preserves | Separate inherited search preservation from decision claims. |
| [M07](#m07) | Discrete Gaussian mass and width | Fix the probability law used by the positive result. |
| [M08](#m08) | Smoothing and coset masses | Identify the precise statistical tool. |
| [M09](#m09) | Normal form and reduction parameters | Track distributions and resources through a reduction. |
| [M10](#m10) | Background synthesis | Assemble a faithful leakage-aware experiment. |
| [M11](#m11) | The scalar residual equation | Locate a forced public relation. |
| [M12](#m12) | Ideal dimension and cancellation probability | Turn the relation into an exact probability. |
| [M13](#m13) | Coefficient hints versus quotient hints | Explain why equal leakage lengths behave differently. |
| [M14](#m14) | Vector hints and affine images | Identify the full uniform-hidden discrepancy. |
| [M15](#m15) | Short and sparse effective hints | Delimit which hints can support this obstruction. |
| [M16](#m16) | The allowed WLL evaluation hint | Instantiate the general mechanism in the written game. |
| [M17](#m17) | Information in one batch scalar | Bound source recovery independently of computation. |
| [M18](#m18) | Theorem hypotheses and a finite certificate | Compare incompatible guarantees in one admissible instance. |
| [M19](#m19) | A growing-dimensional counterexample family | Establish the asymptotic contradiction. |
| [M20](#m20) | The reduction's leakage interface | Diagnose the missing resource without changing the game. |
| [M21](#m21) | Norm parity as a linear functional | Connect covariance leakage to a small quotient. |
| [M22](#m22) | The exact parity gap | Explain the dependence on module rank. |
| [M23](#m23) | The parity-compatible ideal | State the complete comparison needed by the positive proof. |
| [M24](#m24) | A lift from half the modulus | Preserve the actual leaked parity in both branches. |
| [M25](#m25) | The real Gaussian branch | Control convolution with its full normalizers. |
| [M26](#m26) | The uniform branch | Recover the ideal from complete parity cosets. |
| [M27](#m27) | Ordinary secrets over the local ring | Obtain the stated source assumption and exact loss. |
| [M28](#m28) | Computational and statistical accounting | Complete the matching characterization. |
| [M29](#m29) | Descriptor and application boundaries | Determine which consequences transfer. |
| [M30](#m30) | Narrative synthesis | Connect forced relations, counterexample, and matching hardness. |

## Phase I: background and preliminaries

This phase moves from individual ring elements and maps to the complete distributions and reduction interfaces used by the project. M10 is its synthesis point.

<a id="m01"></a>
### M01. Residues, cosets, and integer lifts

**Central question.** Which parts of an MLWE transcript are residues, and which quantities depend on the sampled integer representatives?

**Understanding target.** Distinguish an element of $`R_q`$, its coefficient representation, and an integer lift in $`R`$. Identify why reduction to a prime residue field requires $`p\mid q`$, and why norm parity survives a change of representative at even modulus.

**Dependencies and story role.** This is the starting point. It fixes the domains needed by M02-M04 and prevents a later covariance or Gaussian statement from changing the underlying random variable implicitly.

**Conceptual connection.** Quotient maps preserve algebraic identities, whereas norms describe the chosen integer distribution. The project uses both viewpoints and must keep them compatible.

**Source pointers.** [Peikert §§2.1 and 2.2.1, pp. 6-7][anchor]; [project ring and coefficient conventions](../science/model.md#1-ring-and-coefficient-conventions).

<a id="m02"></a>
### M02. Module equations and structured coefficient matrices

**Central question.** What changes when one noisy scalar equation is replaced by an equation over a polynomial ring?

**Understanding target.** Relate $`B=AS+E`$ over $`R_q`$ to its coefficient system with multiplication matrix $`M_A`$. Keep $`k`$, $`N`$, $`kN`$, and $`m`$ distinct, and recognize that coefficients inside a multiplication block are correlated.

**Dependencies and story role.** Uses M01. It supplies the structured linear system behind the ideal law and the later distinction between probabilities governed by $`k`$ and by $`kN`$.

**Conceptual connection.** Peikert's generalized ring-LWE interpolates between ordinary LWE and Ring-LWE. Here the same structure controls which linear constraints occur together.

**Source pointers.** [Peikert §§4.3.2, 4.4.1, and 4.4.3, pp. 28 and 30-32][anchor]; [project model](../science/model.md#1-ring-and-coefficient-conventions) and [coefficient formulation](../science/linear_leakage.md#model-notation-and-advantage-convention).

<a id="m03"></a>
### M03. Coefficient pairings and norm conventions

**Central question.** How can a coefficient inner product be represented within the ring without changing its meaning?

**Understanding target.** Understand the roles of the involution $`x\mapsto\bar x`$ and the constant coefficient $`\mathrm{ct}(x)`$ in coefficient-linear hints and squared norms. Distinguish the coefficient norm from the full canonical-embedding norm and carry the stated scaling convention into Gaussian widths.

**Dependencies and story role.** Uses M01-M02. It provides the common notation needed for scalar leakage, effective multipliers, and extraction of norm parity from covariance.

**Conceptual connection.** The ring's algebraic action and its geometric embedding serve different purposes. A correct pairing lets a proof move between them without treating their norms as interchangeable.

**Source pointers.** [Peikert §4.3.3, pp. 28-29][anchor]; [project pairing identities](../science/model.md#1-ring-and-coefficient-conventions) and [Gaussian embedding convention](../science/gaussian_characterization.md#distributions-and-conventions).

<a id="m04"></a>
### M04. Images, ideals, and quotient size

**Central question.** Which image does a uniform input induce, and what does the size of that image determine?

**Understanding target.** Relate linear images and their fibers to uniform distributions on finite groups. Recognize an ideal as the image of a ring-linear map, and distinguish a squarefree field decomposition from a repeated-root or composite-coefficient setting.

**Dependencies and story role.** Uses M01-M03. It supplies the elementary counting language for M12 and M14; the project-specific probability laws will be derived there.

**Conceptual connection.** Algebraic structure supplies image sizes and kernel fibers. Those finite quantities become observable probabilities once a public matrix is sampled uniformly.

**Source pointers.** [Peikert §4.3.4, pp. 29-30, and §4.4.2, pp. 31-32][anchor]; [project ideal dimension](../science/linear_leakage.md#proposition-a3-computing-the-ideal-dimension) and [field/composite boundary](../science/linear_leakage.md#prime-residue-fields-and-composite-coefficient-rings). The detailed finite-image identities are supplied by the project, rather than attributed to the survey.

<a id="m05"></a>
### M05. Search, decision, and the complete transcript

**Central question.** What must a leakage-augmented decision comparison preserve, and what does successful search recover?

**Understanding target.** Specify both joint distributions, including the genuine hint marginal and the uniform public matrix. Distinguish recovery of the sampled secret from finding any consistent secret, and distinguish an acceptance-probability gap from guessing advantage and full statistical distance.

**Dependencies and story role.** Uses M01-M04. This is the common experiment specification for both the counterexample and the positive theorem, including the fact that one finite batch supplies only its declared hint.

**Conceptual connection.** A decision claim concerns an entire joint distribution. Preserving separate marginals does not preserve the relations among them.

**Source pointers.** [Peikert §4.2.1, pp. 22-24, and §2.4, p. 10][anchor]; [project leakage experiments](../science/model.md#2-the-two-leakage-experiments), [advantage conventions](../science/model.md#3-advantages-and-statistical-distance), and [search target](../science/model.md#4-search-and-bounded-leakage).

<a id="m06"></a>
### M06. What bounded leakage preserves

**Central question.** Why can a short hint preserve search hardness while invalidating an independent-response decision comparison?

**Understanding target.** Understand the ordinary guessing reduction for a finite hint alphabet, its success loss, and why it requires no verification of the solver's output. Separate that inherited search statement from a search-to-decision theorem with its own distribution and resource hypotheses.

**Dependencies and story role.** Uses M05. It creates the logical separation that the WLL counterexample and the one-bit norm-parity result will exploit.

**Conceptual connection.** The number of possible hint values controls a guessing loss. The algebraic position of those values can control a different phenomenon, namely an exact public relation.

**Source pointers.** [Peikert §4.2.4, “Robustness,” p. 26, and §4.2.2, pp. 24-25][anchor]; [project bounded-leakage argument](../science/model.md#4-search-and-bounded-leakage) and [its attribution](../references/RELATED_WORK.md#bounded-leakage-and-search).

<a id="m07"></a>
### M07. Discrete Gaussian mass and width

**Central question.** Which normalized probability law is meant by a coefficient Gaussian of width $`s`$?

**Understanding target.** Distinguish the Gaussian mass function from its normalized distribution, a discrete Gaussian from a rounded continuous one, and width from standard deviation. Track product structure in the full $`N(k+m)`$-coordinate hidden vector.

**Dependencies and story role.** Uses M01 and M03. It fixes the quantities that appear in the convolution normalizers and the true marginal of the leaked parity bit.

**Conceptual connection.** Independence across coefficients makes the Gaussian mass factorize, but taking a function of those coefficients does not make that function independent of the public sample.

**Source pointers.** [Peikert §2.3, especially “Gaussians,” p. 9, and §4.4.1, pp. 30-31][anchor]; [project Gaussian distributions](../science/gaussian_characterization.md#distributions-and-conventions).

<a id="m08"></a>
### M08. Smoothing and coset masses

**Central question.** What statistical statement does exceeding the smoothing parameter actually provide?

**Understanding target.** Connect the dual-lattice definition of smoothing to nearly equal Gaussian mass on translated cosets. Keep the tolerance $`\epsilon`$ explicit, and distinguish approximate convolution behavior from an exact equality of discrete distributions.

**Dependencies and story role.** Uses M04 and M07. It provides the analytic tool used twice in the positive proof: once for a Gaussian convolution and once for uniformity of a residue vector.

**Conceptual connection.** The same control of coset masses governs both geometric smoothing and the algebraic quotient distribution seen by a leakage bit.

**Source pointers.** [Peikert §2.2.1, pp. 6-7, and §2.3, including Theorem 2.3.2, pp. 9-10][anchor]; [project smoothing convention and lift](../science/gaussian_characterization.md#a-gaussian-lift-that-preserves-the-leaked-bit).

<a id="m09"></a>
### M09. Normal form and reduction parameters

**Central question.** What must be preserved when a reduction changes the secret distribution or the modulus?

**Understanding target.** Follow the normal-form cancellation that replaces an ordinary secret by part of the error vector, while checking both real and uniform branches. Track public-matrix uniformity, sample consumption, source and target widths, and the distinction between an average-case assumption and a worst-case hardness theorem.

**Dependencies and story role.** Uses M02, M05, and M07-M08. It prepares the exact local-ring conversion and half-modulus lift without assuming that a familiar transformation preserves all resources automatically.

**Conceptual connection.** An algebraic transformation becomes a reduction only after its output distributions and parameter changes are accounted for.

**Source pointers.** [Peikert §4.2.1, “Normal form,” p. 23; §4.2.4, pp. 25-26; and §4.4.1, p. 31][anchor]; [project ordinary assumption](../science/model.md#5-the-ordinary-assumption-used-by-the-positive-result).

<a id="m10"></a>
### M10. Background synthesis: the augmented experiment

**Central question.** Can the algebra, distributions, and computational task be assembled into one unambiguous model?

**Understanding target.** Give a coherent account of what is fixed before $`A`$, what is sampled, what the adversary receives, which secret search must recover, and which joint law decision compares. Keep the uniform-hidden algebraic model separate from the Gaussian model used by the positive theorem.

**Dependencies and story role.** Synthesizes M01-M09 and completes Phase I. It establishes the common specification against which every later attack, impossibility bound, and reduction is interpreted.

**Conceptual connection.** Modeling the leakage interface and the random comparison is part of the mathematical problem. It determines which reduction statements can be compared at all.

**Source pointers.** [Peikert §§4.2.1 and 4.4.1, pp. 22-24 and 30-31, together with §2.3, pp. 8-10][anchor]; [complete project model](../science/model.md) and [ordinary assumption used by the positive result](../science/model.md#5-the-ordinary-assumption-used-by-the-positive-result).

## Phase II: narrative and innovation

This phase starts with one substituted hint equation, develops the general image law, and follows its two concrete consequences. The final steps combine the norm-parity attack with the matching Gaussian reduction and establish the precise endpoint. M30 is the synthesis point.

<a id="m11"></a>
### M11. The scalar residual equation

**Central question.** After the public response is substituted into a scalar hint, what secret dependence remains?

**Understanding target.** Identify the residual coefficient multiplying each secret component and the public condition under which every residual vanishes. Understand why the resulting equality holds for every secret and error value, without a Gaussian or anti-concentration assumption.

**Dependencies and story role.** Uses M03-M06 and the synthesis in M10. This is the local algebraic mechanism from which the broader distinguishing results are built.

**Conceptual connection.** Noise can remain computationally difficult to infer while an exact auxiliary equation cancels its unknown components on a public event.

**Source pointers.** [Peikert §4.2.1, matrix formulation and normal form, p. 23, and §4.4.1, pp. 30-31][anchor]; [project scalar hint and cancellation condition](../science/linear_leakage.md#scalar-hints-and-the-ideal-dimension-formula).

<a id="m12"></a>
### M12. Ideal dimension and cancellation probability

**Central question.** How often does the scalar cancellation condition occur for a uniform public matrix?

**Understanding target.** Connect the image ideal generated by the error-hint coefficients to the independent matrix columns. Obtain the event probability $`p^{-kr}`$ when every secret-hint coefficient lies in that ideal, and recognize the empty event otherwise. Understand the gcd formula for $`r`$ and distinguish its general validity from the more restrictive interpretation through distinct CRT field components.

**Dependencies and story role.** Uses M04 and M11. It turns a pointwise identity into a quantified distribution-independent test and supplies the parameter that organizes the rest of the algebraic analysis.

**Conceptual connection.** The relevant size is the dimension of a ring ideal generated by the hint, which may be much smaller than the coefficient dimension of the secret.

**Source pointers.** [Peikert §4.3.4, pp. 29-30, and §4.4.2, pp. 31-32][anchor]; [Theorem A2](../science/linear_leakage.md#theorem-a2-scalar-ideal-dimension-law) and [Proposition A3](../science/linear_leakage.md#proposition-a3-computing-the-ideal-dimension).

<a id="m13"></a>
### M13. Equal-sized hints with unequal algebraic support

**Central question.** Why can two hints revealing one field element have exponentially different cancellation probabilities?

**Understanding target.** Compare an individual coefficient hint with evaluation at a root of the defining polynomial. Relate their respective full-dimensional and one-dimensional ideals to the resulting dependence on $`kN`$ or $`k`$.

**Dependencies and story role.** Uses M02 and M12. It makes the consequence of the ideal law concrete and identifies the quotient hint later used against the written reduction.

**Conceptual connection.** A bit-length budget measures how much a hint can encode. Its algebraic support determines which public equations it can constrain.

**Source pointers.** [Peikert §§4.3.2 and 4.4.3, pp. 28 and 32][anchor]; [coefficient-versus-quotient comparison](../science/linear_leakage.md#an-individual-coefficient-versus-a-quotient-value) and [what a leakage budget misses](../science/interpretation.md#what-a-leakage-budget-misses).

<a id="m14"></a>
### M14. Vector hints and the compatible affine image

**Central question.** What remains of the scalar mechanism when a hint has several coordinates or a composite coefficient modulus?

**Understanding target.** Understand the affine support determined by $`D_A=H_S-H_EM_A`$ and the quotient identity $`W=W_A+\mathrm{Im}(H_E)`$. Distinguish the distribution-independent gap of the support test from its equality with full TV for jointly uniform hidden variables, and use image cardinalities when field ranks are unavailable.

**Dependencies and story role.** Uses M04-M05 and M11-M13. It generalizes the local obstruction into a complete compatible comparison in the uniform-hidden model, including the modulus-four example.

**Conceptual connection.** A uniform image conditioned on a public linear equation becomes uniform on an affine fiber. This is the distributional structure the independent-response benchmark may erase.

**Source pointers.** [Peikert §2.2.1, pp. 6-7, and §4.2.1, pp. 22-24][anchor]; [Theorem A1](../science/linear_leakage.md#theorem-a1-affine-image-law) and [composite coefficient rings](../science/linear_leakage.md#prime-residue-fields-and-composite-coefficient-rings). The exact affine-image law is proved in the project.

<a id="m15"></a>
### M15. Short and sparse effective hints

**Central question.** Which restrictions on the actual hint coefficients prevent a very small error-hint ideal?

**Understanding target.** Understand the shift-span support bound and the determinant-based coefficient-norm bound, including the condition making the integer determinant nonzero. Apply the restrictions to the effective coefficients after all ring multipliers and sums, and distinguish a bound on this obstruction from a general security theorem.

**Dependencies and story role.** Uses M03 and M12-M14. It qualifies the freedom used by the quotient attack and provides a principled boundary for protocol-specific hint distributions.

**Conceptual connection.** Algebraic concentration has a geometric cost. Dense or large effective coefficients can create small quotient support even when a syntactic description appears short.

**Source pointers.** [Peikert §§4.3.2-4.3.4, pp. 28-30][anchor]; [project support and norm bounds](../science/linear_leakage.md#when-effective-hints-are-short-or-sparse) and [restricted hint distributions](../science/interpretation.md#restricted-and-short-hint-distributions).

<a id="m16"></a>
### M16. The permitted WLL evaluation hint

**Central question.** Is the quotient hint an allowed instance of the inspected finite-batch leakage game?

**Understanding target.** Match the fixed error evaluation functional to the paper's coefficient-linear syntax and the repository's notation. Follow the public zero-row quotient event and its exact real-versus-independent probability gap, keeping the paper's guessing-advantage convention separate.

**Dependencies and story role.** Uses M05, M10, and M13. It instantiates the general mechanism inside a specific claimed reduction without requiring adaptive hint selection or unusually large errors.

**Conceptual connection.** A theorem quantified over all permitted hints must cover a hint concentrated on one quotient, even if a later application samples hints differently.

**Source pointers.** [Peikert §§4.4.1-4.4.2, pp. 30-32][anchor]; [WLL finite-batch game](../science/published_reduction.md#1-the-finite-batch-leakage-game), [Proposition 1](../science/published_reduction.md#proposition-1-a-fixed-evaluation-hint), and [verified source identity](../references/wll_source_audit.md#1-verified-text-and-publication-identity).

<a id="m17"></a>
### M17. Information in one finite-batch scalar

**Central question.** How much of a uniformly masked secret can one scalar hint identify, however many samples the batch contains?

**Understanding target.** Follow the conditional distribution of the secret after fixing $`A,B`$ under an independent uniform secret and uniform coefficient errors. Relate one remaining scalar equation, or the cardinality of a general scalar hint, to the maximum probability of recovering the sampled secret.

**Dependencies and story role.** Uses M05-M06, M14, and M16. It supplies an unconditional source bound, allowing the reduction claim to be tested without assuming a cryptographic hardness conjecture.

**Conceptual connection.** Adding uniformly masked equations does not replace leakage values that the source interface never supplied. Sample count and hint count are different resources.

**Source pointers.** [Peikert §4.2.1, pp. 22-24, and §7.1, discussion before Question 7, p. 75][anchor]; [Proposition 2 and the one-scalar information bound](../science/published_reduction.md#proposition-2-information-theoretic-search-bound).

<a id="m18"></a>
### M18. Theorem hypotheses and the finite certificate

**Central question.** Do the easy target and the unrecoverable source coexist under the written theorem's actual hypotheses?

**Understanding target.** Check the signed-permutation automorphism action, invariance of the centered uniform coefficient law, full splitting, and the stated modulus bound. Interpret the $`N=4,q=17`$ certificate as a comparison of exact theorem quantities, with consistent advantage conventions and source sample count.

**Dependencies and story role.** Uses M02 and M16-M17. It connects the two independent arguments inside one admissible instance and isolates the particular theorem statement being contradicted.

**Conceptual connection.** A counterexample to a reduction must satisfy the source and target quantifiers simultaneously. An easy target outside those hypotheses would not establish the same conclusion.

**Source pointers.** [Peikert §4.4.2, pp. 31-32][anchor]; [invariance requirement](../science/published_reduction.md#the-error-distribution-meets-the-invariance-requirement), [finite certificate](../science/published_reduction.md#a-small-exact-certificate), and [exact verification](../verification/check_counterexample.py).

<a id="m19"></a>
### M19. A growing-dimensional counterexample family

**Central question.** How does the contradiction persist as an asymptotic, polynomially specified family?

**Understanding target.** Track the role of an effective least-prime bound in choosing fully split primes above the theorem's threshold. Check polynomial constructibility, nonnegligible target advantage, polynomial source sample growth, and negligible source recovery within the same family.

**Dependencies and story role.** Uses M05 and M18. It closes the gap between a finite certificate and a contradiction to the asymptotic theorem.

**Conceptual connection.** An exact small example illustrates a mechanism; an admissible growing family establishes the asymptotic statement. The number-theoretic ingredient has a precise existence-and-complexity role.

**Source pointers.** [Peikert §2.4, p. 10, and §4.4.2, pp. 31-32][anchor]; [unconditional asymptotic family](../science/published_reduction.md#an-unconditional-asymptotic-family) and [the primary least-prime citation](../references/wll_source_audit.md#4-the-asymptotic-prime-family-has-a-primary-proof). The least-prime theorem is a research citation, not content attributed to Peikert.

<a id="m20"></a>
### M20. The reduction's leakage interface

**Central question.** What resource does the inspected proof use that its finite-batch source definition does not provide?

**Understanding target.** Distinguish one global scalar from separate block hints and distinguish transporting a hint algebraically from preserving a solver's success guarantee on that hint. Keep the unconditional contradiction separate from additional proof obligations, and retain the inspected-version boundary.

**Dependencies and story role.** Uses M06 and M16-M19. It completes the finite-batch branch by locating the interface issue instead of treating a larger batch as a different leakage oracle.

**Conceptual connection.** Search-to-decision reductions consume precisely specified resources. Their sample amplification cannot silently amplify the permitted leakage interface as well.

**Source pointers.** [Peikert §4.2.2, pp. 24-25, and §7.1, Question 7 and preceding discussion, p. 75][anchor]; [proof-resource diagnosis](../science/published_reduction.md#5-what-the-proof-audit-establishes) and [source hypothesis audit](../references/wll_source_audit.md#2-hypothesis-and-quantifier-audit).

<a id="m21"></a>
### M21. Norm parity as a linear functional

**Central question.** How does a quadratic-looking covariance descriptor expose a linear residue hint?

**Understanding target.** Follow the constant coefficient of $`K=\sum_jS_j\bar S_j+\sum_iE_i\bar E_i`$ to the aggregate coefficient squared norm and then to its parity. Identify augmentation at $`X=1`$ modulo two and its one-dimensional ideal.

**Dependencies and story role.** Uses M01, M03, and M12. It begins the even-modulus branch by placing a natural descriptor inside the same scalar leakage framework.

**Conceptual connection.** Reduction to characteristic two can change the apparent degree of a leaked quantity. The meaningful public constraint can reside in a very small projection of a much larger descriptor.

**Source pointers.** [Peikert §§4.3.1 and 4.3.3, pp. 27-29][anchor]; [norm-parity model](../science/norm_parity.md#model-and-the-leaked-bit) and [covariance projection](../science/norm_parity.md#consequence-for-the-full-covariance-hint).

<a id="m22"></a>
### M22. The exact rank-dependent parity gap

**Central question.** Why does the parity test retain a constant gap at fixed module rank even as the ring degree grows?

**Understanding target.** Connect the augmentation column-sum event to the exact gap $`2^{-(k+1)}`$. Separate the identity holding for every fixed hidden vector from the event probability requiring uniform $`A`$, and compare the structured coefficient blocks with an unstructured matrix.

**Dependencies and story role.** Uses M02, M12, and M21. It proves the even-modulus obstruction and explains its dependence on module rank, without invoking a noise distribution.

**Conceptual connection.** Ring multiplication couples many coefficient constraints into one quotient condition per module component. The event therefore reflects module structure rather than coefficient dimension alone.

**Source pointers.** [Peikert §§4.3.2 and 4.4.3, pp. 28 and 32][anchor]; [Theorem N1](../science/norm_parity.md#theorem-n1-distribution-independent-parity-gap) and [finite parity checks](../verification/check_norm_parity.py).

<a id="m23"></a>
### M23. The parity-compatible ideal

**Central question.** What complete conditional hint law should replace the independent-bit comparison?

**Understanding target.** Understand why the parity is forced on the public event and fair off it for independent uniform hidden coefficient bits, conditional on the response's entire coefficient-parity vector. Identify the additional uniformity or masking of the higher response bits needed for the complete transcript law. Keep the compatible ideal, a fair independent bit, and the genuine Gaussian parity marginal distinct, including the bias term $`\alpha_t`$.

**Dependencies and story role.** Uses M07-M08, M14, and M22. It converts the negative result into the exact target distribution required for the positive reduction.

**Conceptual connection.** A simulation target can preserve unavoidable public information while leaving the remaining information computationally hidden. Correctness of that target requires a joint conditional law, not only a parity marginal.

**Source pointers.** [Peikert §2.3, p. 9, and §4.2.1, pp. 22-24][anchor]; [compatible ideal and genuine marginal](../science/norm_parity.md#the-compatible-ideal-and-the-genuine-parity-marginal) and [Lemma G1](../science/gaussian_characterization.md#lemma-g1-the-exact-parity-ideal).

<a id="m24"></a>
### M24. A lift from half the modulus

**Central question.** How can a reduction produce a wider Gaussian sample together with its actual parity without knowing the source secret?

**Understanding target.** Follow the public transformation from modulus $`q/2`$ to $`q`$, the uniform lift of the public matrix, and the latent identity $`X=2U+V`$. Separate what the algorithm computes from the hidden variables used only to analyze it, and track the exact parity preservation.

**Dependencies and story role.** Uses M09, M21, and M23. It constructs the bridge between the normal-form Module-LWE source and the leakage-aware target; M25-M26 will establish its two output distributions.

**Conceptual connection.** Multiplying the unknown source by two removes its contribution to the disclosed bit. An independently sampled perturbation then carries the actual target parity.

**Source pointers.** [Peikert §4.2.4, modulus transformations on p. 26, and §5.4.2, perturbation and convolution discussion on p. 49][anchor]; [Theorem G2 and transformation G10](../science/gaussian_characterization.md#theorem-g2-matching-normal-form-reduction).

<a id="m25"></a>
### M25. The real Gaussian branch

**Central question.** What justifies replacing the convolution by the target Gaussian while retaining the leaked bit?

**Understanding target.** Track the completed-square identity, both Gaussian normalizers, the center-dependent theta factor, and the reciprocal likelihood-ratio bound. Understand why the proof controls the full latent vector at width $`t=\sqrt8s`$ before applying the response-and-parity map.

**Dependencies and story role.** Uses M07-M08 and M24. It proves the real-branch approximation with its explicit $`\epsilon`$ loss and prevents a marginal-only argument from discarding the leakage dependence.

**Conceptual connection.** Approximate convolution becomes a security-relevant statement only when its statistical bound survives the deterministic map producing the entire observed transcript.

**Source pointers.** [Peikert §2.3, p. 9, and §5.4.2, p. 49][anchor]; [Theorem G2, real branch and equations G11-G13](../science/gaussian_characterization.md#theorem-g2-matching-normal-form-reduction) and [Gaussian identity verification](../verification/check_gaussian_identity.py).

<a id="m26"></a>
### M26. The uniform branch and complete parity cosets

**Central question.** Why does the uniform source branch produce the compatible ideal rather than an unrelated uniform hint?

**Understanding target.** Follow the uniform mask on the even-coefficient subgroup, the resulting full parity coset, and smoothing of $`V\bmod2`$. Apply the fixed-matrix conditional law from M23 only after controlling the complete residue vector.

**Dependencies and story role.** Uses M08 and M23-M25. It closes the second branch of the lift and establishes the second $`\epsilon`$ term in the reduction.

**Conceptual connection.** The lift combines uniformity within a coset with an almost uniform choice of coset. A single augmentation bit would not by itself describe the full public response distribution.

**Source pointers.** [Peikert §2.2.1, pp. 6-7, and §2.3, p. 9][anchor]; [Theorem G2, uniform branch and equations G14-G15](../science/gaussian_characterization.md#theorem-g2-matching-normal-form-reduction).

<a id="m27"></a>
### M27. Ordinary secrets over the local ring

**Central question.** How is the normal-form source obtained from the stated ordinary uniform-secret Module-LWE assumption?

**Understanding target.** For power-of-two ring degree $`N\ge2`$ and target modulus $`q=2^a`$ with $`a\ge2`$, understand invertibility through the source ring's residue field, the probability $`p_k=\prod_{i=1}^k(1-2^{-i})`$, and the cancellation using the first $`k`$ rows. Check that conditioning changes neither the error law nor the uniform-branch guarantee.

**Dependencies and story role.** Uses M02, M09, and M24-M26. It replaces an intermediate assumption with the declared ordinary source, while preserving the source modulus $`q/2`$ and accounting for the extra samples.

**Conceptual connection.** The standard normal-form transformation needs a ring-specific invertibility calculation. Its exact success probability $`p_k`$ determines the multiplicative advantage loss; the abort probability is $`1-p_k`$.

**Source pointers.** [Peikert §4.2.1, “Normal form,” p. 23, and §4.4.1, p. 31][anchor]; [Lemma G3](../science/gaussian_characterization.md#lemma-g3-normal-form-over-the-local-ring) and [Corollary G4](../science/gaussian_characterization.md#corollary-g4-ordinary-mlwe-characterization).

<a id="m28"></a>
### M28. Completing the matching characterization

**Central question.** What is the complete computational statement after sampling and all reduction losses are included?

**Understanding target.** Account for the source modulus, $`k+m`$ source samples, target width, smoothing condition, and the advantage against the compatible ideal, bounded by source advantage divided by $`p_k`$ plus $`2\epsilon+2\delta`$. For the genuine independent-response benchmark, add $`2^{-(k+1)}+(1-2^{-k})\alpha_t`$. Connect the finite-precision Gaussian sampler to that error budget and the upper bound to the explicit parity test, including classical-input QPT scope.

**Dependencies and story role.** Uses M05, M07-M09, and M25-M27. It assembles the positive result and establishes optimality up to negligible terms under the specified source assumption.

**Conceptual connection.** Exact algebraic leakage and approximate simulation coexist in one theorem. Statistical errors remain additive, while the normal-form conditioning affects the source advantage multiplicatively.

**Source pointers.** [Peikert §2.4, p. 10; §4.2.2, pp. 24-25; and §5.4.2, Theorem 5.4.2 and sampling discussion, pp. 46-49][anchor]; [Corollary G4 and parameter table](../science/gaussian_characterization.md#corollary-g4-ordinary-mlwe-characterization) and [sampling and computational model](../science/gaussian_characterization.md#sampling-computational-model-and-scope).

<a id="m29"></a>
### M29. Descriptor and application boundaries

**Central question.** Which consequences transfer to stronger hints or existing protocols, and which require another theorem?

**Understanding target.** Distinguish projecting a full norm or covariance to its parity from simulating that stronger descriptor. Keep adversarially chosen hints separate from prescribed random hints, and compare the ordinary prime-modulus known-norm result, odd-prime ring attacks, and the even-modulus parity result within their actual hypotheses.

**Dependencies and story role.** Uses M15, M20, M22, and M28. It connects the completed branches to their closest research statements and fixes the scope of every claimed consequence.

**Conceptual connection.** Deterministic projection transfers a negative distinguisher in one direction. A positive theorem for the projection does not automatically reconstruct the information discarded by that projection.

**Source pointers.** [Peikert §2.4.2, p. 11; §4.2.4, “Robustness,” p. 26; and §4.4.2, pp. 31-32][anchor]; [known-covariance comparison](../science/norm_parity.md#exact-comparison-with-the-preceding-results), [WLL application boundary](../science/published_reduction.md#6-boundary-of-the-application-claim), and [related work](../references/RELATED_WORK.md#closest-cryptographic-results).

<a id="m30"></a>
### M30. Narrative synthesis: forced relations and matching hardness

**Central question.** What unified account explains the algebraic obstruction, the finite-batch contradiction, and the surviving Gaussian hardness claim?

**Understanding target.** Connect the chain from a fixed hint to its residual image, from that image to a public test, and from the forced relation to a compatible random experiment. Place the unconditional WLL counterexample and the conditional Gaussian parity characterization on that same map, with their distinct assumptions, source resources, and limits.

**Dependencies and story role.** Synthesizes M11-M29 and the model assembled in M10. This is the endpoint of the route: the general algebra and both concrete branches form one scientific argument with an explicit boundary.

**Conceptual connection.** The appropriate decision comparison is shaped by unavoidable information. A meaningful hardness statement then concerns the information remaining after those constraints are preserved.

**Source pointers.** [Peikert §§4.4.1-4.4.3, pp. 30-32, and §2.3, pp. 8-10][anchor]; [project interpretation and limits](../science/interpretation.md), [established endpoint](../science/interpretation.md#established-endpoint), and [verification scope](../verification/README.md#exact-arithmetic-and-numerical-scope).

[anchor]: https://eprint.iacr.org/2015/939
