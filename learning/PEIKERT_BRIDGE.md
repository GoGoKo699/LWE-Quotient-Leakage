# From Peikert's LWE foundations to quotient leakage

The educational anchor is Chris Peikert, [*A Decade of Lattice Cryptography*](https://eprint.iacr.org/2015/939), ePrint 2015/939, revision posted **February 18, 2016**. The manuscript's title page is dated February 17, 2016. The published version is *Foundations and Trends in Theoretical Computer Science* **10**(4), 283–424 (2016), [DOI: 10.1561/0400000074](https://doi.org/10.1561/0400000074). Section numbers below refer to that ePrint revision.

Peikert develops the ordinary LWE experiments, their lattice interpretation, Gaussian tools, and ring structure. This bridge explains the additional reasoning needed when an experiment reveals information about its secret or errors. The central step is to retain the entire joint transcript: leakage can force a public relation that disappears when the response is replaced by an independent uniform value.

## 1. A focused route through the anchor

| Anchor section | What to carry into this project |
| --- | --- |
| **2.2, Lattices** | Lattice cosets and linear maps provide the language for both Gaussian residue classes and the affine sets of compatible hints. The lattice problems explain what a hardness assumption asserts. |
| **2.3, (Discrete) Gaussians and Subgaussians** | Learn the Gaussian width convention and smoothing parameter. Nearly equal Gaussian masses on translated lattice cosets are the ingredient behind the positive parity theorem. |
| **4.2.1, LWE definitions and normal form** | Keep search, decision, and the available sample count separate. Follow the invertible-block transformation that replaces the uniform secret by an error-distributed secret. |
| **4.3.1–4.3.3, ring structure and geometry** | Represent multiplication by a ring element as a structured coefficient matrix. Distinguish coefficient geometry from the canonical embedding. These ideas carry over from Ring-SIS without requiring its collision-resistance proof. |
| **4.4.1–4.4.3, Ring-LWE and generalizations** | Read the ring experiment and its normal form, then the module generalization. Section 4.4.2 makes clear that search-to-decision reductions have hypotheses about the ring, modulus, and errors. |

The relevant transition is from the definitions to the distributions in [the project model](../science/model.md). The survey's worst-case hardness statements supply context; the project's positive theorem explicitly assumes its stated ordinary Module-LWE source problem.

### Notation and assumption translation

| Meaning | Peikert's notation or convention | Project convention |
| --- | --- | --- |
| Ordinary LWE dimension | $`n`$ in Section 4.2 | A module secret has $`kN`$ coefficients; its expanded samples have ring-imposed correlations. |
| Ring degree and module rank | $`n`$ for ring degree; $`k`$ in Section 4.4.3 | $`N`$ and $`k`$; $`m`$ counts ring samples. |
| Public matrix orientation | $`A\in\mathbb Z_q^{n\times m}`$, with samples as columns; $`b^T=s^TA+e^T`$ | $`A\in R_q^{m\times k}`$, with samples as rows; $`B=AS+E`$. |
| Ring | General $`R=\mathbb Z[X]/(f)`$ in the introductory treatment | $`R=\mathbb Z[X]/(X^N+1)`$; power-of-two $`N`$ where specified. |
| Secret distribution | Uniform secret in the ordinary definitions; error-distributed secret in normal form | The algebra allows any hidden law independent of $`A`$; the Gaussian theorem specifies independent coefficient Gaussians. |
| Gaussian scale | $`\rho_s(x)=\exp(-\pi\lVert x\rVert_2^2/s^2)`$ | The same width convention; $`s`$ is the source width and $`t`$ the target width. Width is not standard deviation. |
| Ring error geometry | Canonical embedding, with the dual-ring adjustment discussed in Section 4.4.1 | Coefficient Gaussians. For the power-of-two ring, the full canonical embedding scales Euclidean norms by $`\sqrt N`$. |

## 2. From an LWE equation to the compatible hint set

Ordinary decision-LWE compares a noisy response with a uniform response. With leakage, specify what remains visible in both experiments. Here the comparison is

```math
(A,AS+E,h(S,E))
\quad\text{versus}\quad
(A,U,h(S,E)),
```

where $`U`$ is independent uniform and the hint retains its **genuine marginal distribution**. A hint need not be uniform. The hint map is fixed before the uniform public matrix is sampled.

Choose a prime $`p\mid q`$ and expand ring elements into coefficient vectors modulo $`p`$. Peikert's structured-matrix viewpoint gives

```math
\mathbf b=M_A\mathbf s+\mathbf e,
\qquad h=H_S\mathbf s+H_E\mathbf e.
```

The additional conceptual step is to eliminate the errors using the public response:

```math
h=H_E\mathbf b+D_A\mathbf s,
\qquad D_A=H_S-H_EM_A.
```

Thus every real hint lies in the affine set $`H_E\mathbf b+\mathrm{Im}\,D_A`$. “Affine” means a linear subspace translated by the known vector $`H_E\mathbf b`$. This constraint can be checked without recovering the secret.

Let $`W=\mathrm{Im}\,[H_S\ H_E]`$ and $`W_A=\mathrm{Im}\,D_A`$. The identity $`W=W_A+\mathrm{Im}\,H_E`$ explains the random experiment: the uniform response distributes $`H_E\mathbf u`$ uniformly across the quotient $`W/W_A`$. For any fixed genuine hint value, the compatibility test therefore accepts with probability $`|W_A|/|W|`$. It always accepts real transcripts. Its acceptance-probability gap is

```math
\mathbb E_A\left[1-p^{\dim W_A-\dim W}\right].
```

If the hidden secret-error vector is jointly uniform modulo $`q`$, conditioning on $`A,B`$ leaves $`S`$ uniform. The hint is then exactly uniform on that affine set. Consequently the gap is the full statistical distance in this uniform-hidden case. For other hidden laws, it is the gap of this particular test. [Theorem A1](../science/linear_leakage.md#theorem-a1-affine-image-law) proves both statements separately.

### Why the ring location of one scalar matters

The coefficient pairing can be written as $`\mathrm{ct}(\bar v x)`$, where $`\mathrm{ct}`$ extracts the constant coefficient and $`\bar v=v(X^{-1})`$. A scalar hint with secret coefficients $`u_j`$ and error coefficients $`v_i`$ has complete cancellation when

```math
\sum_i\bar v_iA_{ij}=\bar u_j\qquad\text{for every }j.
```

Let $`I=(\bar v_1,\ldots,\bar v_m)\subseteq R_p`$ have vector-space dimension $`r`$, with at least one nonzero error coefficient. Each column sum is uniform in $`I`$. If every target $`\bar u_j`$ belongs to $`I`$, cancellation occurs with probability $`p^{-kr}`$ and gives gap $`p^{-kr}(1-1/p)`$.

This is where ring algebra enters quantitatively. A hint disclosing one coefficient of $`E_1`$ has $`r=N`$; evaluation at one field root has $`r=1`$. Both reveal one field scalar. The ideal dimension is computable by a polynomial gcd, including when the modulus creates repeated roots. [The scalar law](../science/linear_leakage.md#scalar-hints-and-the-ideal-dimension-formula) supplies the details.

## 3. Search and decision after leakage

Peikert defines search as recovery of the secret and decision as distinguishing experiments. Their familiar relationship depends on a reduction for the actual experiment. Adding a scalar hint changes that experiment.

The project's [finite-batch counterexample](../science/published_reduction.md) makes the distinction concrete. At a fully split prime modulus, choose a root $`\alpha`$ of $`X^N+1`$ and disclose $`h=E_1(\alpha)`$. On the public event $`A_{1j}(\alpha)=0`$ for every secret component, the response satisfies $`B_1(\alpha)=h`$. This yields gap $`q^{-k}(1-q^{-1})`$ for any error distribution independent of $`A`$. For fixed $`k`$ and polynomially bounded $`q`$, the gap is inverse polynomial.

Now specialize to independent uniform secret and uniform coefficient errors. Before the hint, every one of the $`q^{Nk}`$ secrets remains equally likely given $`A,B`$. One scalar hint imposes at most one equation. Even unlimited computation therefore recovers the whole secret with probability at most $`q^{1-Nk}`$. Increasing the batch size $`m`$ does not supply additional hint values.

These are compatible conclusions: a quotient relation is visible while the complete secret remains hidden. They contradict the broad finite-batch reduction in Theorem 3.9 of the inspected April 7, 2024 ePrint version of Wang–Lai–Liu, under its admitted uniform-error case. They do not contradict Peikert's ordinary LWE definitions or reductions. The source audit and precise theorem comparison are in the linked chapter.

## 4. A complete four-case norm-parity example

Take $`N=2`$, $`q=4`$, and $`k=m=1`$, so

```math
R_4=(\mathbb Z/4\mathbb Z)[X]/(X^2+1),\qquad B=AS+E.
```

Let $`S=s_0+s_1X`$, $`E=e_0+e_1X`$, and disclose

```math
c=(s_0^2+s_1^2+e_0^2+e_1^2)\bmod2.
```

Define $`\phi(f)=f(1)\bmod2`$. This is a ring homomorphism because the relation $`X^2+1`$ evaluates to zero modulo two. Integer squares have the same parity as their bases, so

```math
c=\phi(S)+\phi(E),\qquad
c+\phi(B)=(1+\phi(A))\phi(S).
```

Our test accepts when $`\phi(A)=1`$ and $`c=\phi(B)`$. The four reductions of a uniform $`A`$ modulo two are equally likely: each has four lifts among the sixteen elements of $`R_4`$.

| $`A\bmod2`$ | $`\phi(A)`$ | Real conditional acceptance | Independent-response conditional acceptance |
| --- | --- | --- | --- |
| $`0`$ | $`0`$ | $`0`$ | $`0`$ |
| $`1`$ | $`1`$ | $`1`$ | $`1/2`$ |
| $`X`$ | $`1`$ | $`1`$ | $`1/2`$ |
| $`1+X`$ | $`0`$ | $`0`$ | $`0`$ |

On the two active rows, the displayed identity forces equality in every real transcript. In the independent experiment, $`\phi(U)`$ is fair even after fixing $`c`$, whatever that bit's genuine marginal. Averaging the rows gives real acceptance $`1/2`$, independent acceptance $`1/4`$, and gap **$`1/4`$**.

This example exhausts the public binary cases for these toy parameters. [Theorem N1](../science/norm_parity.md#theorem-n1-distribution-independent-parity-gap) proves the general result: the gate requires every augmentation column sum to equal one, has probability $`2^{-k}`$, and gives gap $`2^{-(k+1)}`$. The toy calculation illustrates that proof; it supplies no hardness evidence for cryptographic parameters.

## 5. What Gaussian smoothing adds

The natural compatible ideal samples independent uniform $`A,U`$, then chooses

```math
c=\begin{cases}
\sum_i\phi(U_i),&\text{every augmentation column sum of }A\text{ is }1,\\
\text{an independent fair bit},&\text{otherwise}.
\end{cases}
```

For independent hidden variables that are uniform modulo $`q`$, the affine-image calculation gives this full transcript law exactly. Its binary part determines the hint conditional on the complete coefficient-parity vector of the response. Uniform hidden parities alone do not guarantee that the higher response bits carry no additional information. In the Gaussian reduction's random branch, those higher bits are uniformly masked, as shown below. The positive theorem asks whether transcripts with independent Gaussian secret and error coefficients have any efficiently detectable structure beyond this ideal.

Peikert's Section 2.3 gives the needed intuition: above smoothing, translated Gaussian masses are nearly constant. Discrete Gaussian convolution is correspondingly approximate; it requires control of those masses and the normalizing constants.

The project specializes this machinery as follows. Set $`d=N(k+m)`$ and start from normal-form Module-LWE at modulus $`q_0=q/2\ge2`$, width $`s`$. Its hidden vector is $`U=(U_S,U_E)`$. Independently sample $`V\leftarrow D_{\mathbb Z^d,2s}`$, lift the public matrix uniformly from $`q_0`$ to $`q`$, and output

```math
B=2B_0+AV_S+V_E\pmod q,
\qquad c=\mathbf1^T V\pmod2.
```

In the real branch the new hidden vector is $`2U+V`$, whose parity is exactly that of $`V`$. If

```math
s/\sqrt2\ge\eta_\epsilon(\mathbb Z^d),\qquad t=\sqrt8\,s,
```

its distribution is within $`\epsilon`$ of the target width-$`t`$ Gaussian. The same smoothing hypothesis makes the full parity vector of $`V`$ nearly uniform. In the random branch, $`2B_0`$ uniformly masks all coefficients within their parity classes, producing the compatible ideal up to another $`\epsilon`$. Tracking the hidden vector and its parity jointly preserves their dependence.

For a power-of-two ring degree $`N\ge2`$ and a power-of-two modulus $`q\ge4`$, the normal-form argument from Section 4.2.1 has a precise local-ring specialization. It uses $`k`$ additional source samples and succeeds with probability

```math
p_k=\prod_{i=1}^k(1-2^{-i})>1/4.
```

The [Gaussian theorem](../science/gaussian_characterization.md) bounds target distinguishing advantage by ordinary uniform-secret Module-LWE advantage at **modulus $`q/2`$, width $`s=t/\sqrt8`$, and $`k+m`$ samples**, divided by $`p_k`$, plus $`2\epsilon+2\delta`$. Here $`\delta`$ is the product sampler's statistical error. For other even moduli $`q\ge4`$, the stated source assumption remains normal-form Module-LWE.

Finally, a Gaussian parity bit is not exactly fair. Its genuine bias is

```math
\alpha_t=\frac12\left|\mathbb E_{Z\leftarrow D_{\mathbb Z,t}}(-1)^Z\right|^d.
```

The ideal's distance from the independent benchmark retaining that genuine marginal is exactly $`2^{-(k+1)}+(1-2^{-k})\alpha_t`$, with $`\alpha_t\le\epsilon`$ under the smoothing condition. Thus the forced relation characterizes efficient distinguishing up to negligible terms under the stated source assumption. Revealing a full norm or covariance also reveals this parity and inherits the negative test; the positive characterization covers the single bit. [Interpretation and limits](../science/interpretation.md) connects these scopes to the rest of the project.
