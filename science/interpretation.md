# Interpretation and limits

The results answer a specific question: when does exact information about the hidden variables force a recognizable relation in an otherwise noisy Module-LWE transcript? Their common mechanism is the image of the secret's remaining linear map after the public response is substituted into the hint. A small image leaves a constraint that an independent uniform response need not satisfy.

## What a leakage budget misses

A scalar hint over a field contains at most one field element, but its position in the ring can change the relevant probability by an exponential factor in the ring degree. A single coefficient has a full-dimensional error-hint ideal and cancellation probability $`p^{-kN}`$. Evaluation at a root has a one-dimensional ideal and cancellation probability $`p^{-k}`$. Both are matrix-independent linear functionals of the same error vector. The [scalar theorem](linear_leakage.md#theorem-a2-scalar-ideal-dimension-law) computes this distinction exactly.

The vector formulation exposes the same effect without requiring a scalar, a field, or a CRT decomposition. After writing $`\mathbf e=\mathbf b-M_A\mathbf s`$, a hint $`h=H_S\mathbf s+H_E\mathbf e`$ obeys

```math
h-H_E\mathbf b\in\operatorname{Im}(H_S-H_EM_A).
```

For arbitrary hidden distributions, this is a necessary relation and gives the stated test advantage. For uniform hidden variables, it describes the whole discrepancy from the independent-response experiment. At composite modulus, proper nonzero images also matter. The modulus-four example in the [algebra chapter](linear_leakage.md#prime-residue-fields-and-composite-coefficient-rings) has distance $`5/16`$, of which complete cancellation accounts for only $`3/16`$.

This suggests a useful order of analysis for exact leakage. First compute the induced affine image and its probability under the public matrix distribution. Then formulate any remaining computational assumption relative to a comparison distribution that preserves the forced relations. A distribution that violates an efficiently recognizable identity cannot be an appropriate pseudorandomness target.

## Search and decision require separate claims

The standard guessing argument preserves search hardness up to the number of possible leakage values. A one-bit hint costs a factor of two, and one field scalar costs a factor of the field size. This inherited argument is proved in [the model chapter](model.md#4-search-and-bounded-leakage), with its role in prior work explained in [related work](../references/RELATED_WORK.md#bounded-leakage-and-search).

That statement concerns recovery of the sampled secret. It gives no general search-to-decision equivalence after leakage is added. The [WLL counterexample](published_reduction.md) separates the tasks within the inspected finite-batch definition: the fixed quotient hint yields an efficient decision test, while the uniformly masked source secret remains information-theoretically hidden except for at most one scalar equation. Additional uniform-error samples cannot compensate for leakage values that the source game does not supply.

The counterexample has a polynomially specified growing-dimensional family, so its force does not depend on extrapolating one small numerical example. The exact $`N=4,q=17`$ certificate provides a transparent instance of the contradiction. It is neither a secure parameter recommendation nor an application parameter set.

## The even-modulus result and its matching ideal

Norm parity has unusually small algebraic support. Modulo two, squaring an integer preserves its residue, so the parity of a coefficient squared norm is a linear functional. In a negacyclic ring, the augmentation polynomial $`1+X+\cdots+X^{N-1}`$ generates a one-dimensional ideal. The resulting public event has probability $`2^{-k}`$ regardless of the ring degree or sample count.

The corresponding distinguishing gap $`2^{-(k+1)}`$ is constant at fixed module rank. It falls exponentially as the rank increases: it is inverse polynomial when $`k=O(\log\lambda)`$ and becomes negligible when $`k=\omega(\log\lambda)`$, for security parameter $`\lambda`$. These are statements about this test. A smaller test gap does not by itself establish computational hardness.

The [Gaussian characterization](gaussian_characterization.md) supplies the separate positive statement. For power-of-two ring degree and modulus, target coefficient width $`t=\sqrt8s`$, and

```math
s/\sqrt2\ge\eta_\epsilon(\mathbb Z^{N(k+m)}),
```

every efficient distinguisher against the parity-preserving ideal gives an ordinary Module-LWE distinguisher at modulus $`q/2`$, width $`s`$, and $`k+m`$ samples. The invertibility probability in the normal-form conversion is

```math
p_k=\prod_{i=1}^{k}(1-2^{-i})>1/4.
```

The loss is $`1/p_k`$ on the source distinguishing advantage, with additive $`2\epsilon+2\delta`$ for smoothing and the reduction's sampler. The theorem works against classical or quantum polynomial-time distinguishers on classical inputs, under the corresponding source assumption. It requires no coherent sample interface.

The Gaussian hint's genuine marginal can be slightly biased. If its bias is $`\alpha_t`$, the exact distance between the parity-preserving ideal and the genuine independent benchmark is

```math
2^{-(k+1)}+(1-2^{-k})\alpha_t.
```

The chapter gives $`\alpha_t`$ as an explicit Gaussian parity character and bounds it by $`\epsilon`$ under the smoothing hypothesis. Thus, assuming source hardness and negligible statistical terms, the forced public relation characterizes the optimal efficient distinguishing advantage up to negligible error.

## How the result transfers to stronger descriptors

An integer norm or the constant coefficient of a covariance element reveals norm parity. The negative result therefore applies to an even-modulus transcript carrying either stronger descriptor. This is a deterministic projection of the hint and needs no additional reduction assumption.

The direction of that implication matters. A simulator for the parity bit does not simulate the integer norm, the other norm bits, or the remaining covariance coefficients. The positive theorem establishes none of those stronger leakage assumptions. The [known-covariance comparison](norm_parity.md) states the relevant distinction from Micciancio–Suhl and from Bkakria's odd-prime Gram-determinant attacks.

## Restricted and short hint distributions

The quotient attack chooses its hint before the public matrix, as allowed by the broad finite-batch game. A protocol that samples a prescribed random functional poses another question: how much probability does that distribution put on effective hints with small image? The counterexample does not answer it merely by exhibiting one legal chosen hint.

The [support and norm bounds](linear_leakage.md#when-effective-hints-are-short-or-sparse) help separate these regimes. They force sufficiently sparse or sufficiently short effective error coefficients to generate a large ideal, reducing the cancellation probability. Ring multipliers must be included before applying the bounds; short displayed vectors do not automatically imply a short effective functional. These estimates bound the present obstruction. They are not a general security theorem for a random-hint protocol.

## Established endpoint

The scientific account proves the affine-image law, its scalar and composite specializations, the finite-batch theorem counterexample, the distribution-independent parity test, and the matching Gaussian reduction with its full parameter accounting. The finite checks give independently reproducible illustrations of those proofs.

Questions about all information in a covariance, the distribution of protocol-specific hints, or a repaired theorem with an interactive leakage oracle require distinct models and arguments. They are outside the positive claims made here. The [related-work comparison](../references/RELATED_WORK.md) identifies where the present result departs from the nearest verified sources without assigning novelty to its standard algebraic, guessing, or Gaussian ingredients.
