# Norm parity at even modulus

An exact aggregate norm exposes a simple public relation at every even modulus. For rank-one Ring-LWE, one bit of that norm gives a distinguisher with acceptance-probability gap **exactly $`1/4`$**, for every secret and error distribution and every positive number of samples. For module rank $`k`$, the same gap is $`2^{-(k+1)}`$. The ring degree does not enter this probability.

The result concerns the independent-uniform-sample benchmark retaining the genuine hint marginal. It applies to the stronger known-covariance experiment because the covariance reveals the required bit. A separate [Gaussian theorem](gaussian_characterization.md) proves matching hardness for this one-bit projection relative to an ideal that preserves the forced public relation.

## Model and the leaked bit

Let $`N\ge2`$ be a power of two, let $`k,m\ge1`$, and let $`q\ge2`$ be even. Work in

```math
R=\mathbb Z[X]/(X^N+1),\qquad R_q=R/qR.
```

Independently of a uniform matrix $`A\in R_q^{m\times k}`$, sample any jointly distributed $`S\in R^k`$ and $`E\in R^m`$. Set

```math
B=AS+E\pmod q,
\qquad
C=\sum_{j=1}^{k}\|S_j\|_{\mathrm{coef}}^2
  +\sum_{i=1}^{m}\|E_i\|_{\mathrm{coef}}^2,
\qquad c=C\bmod2.
```

The real bit-hint experiment returns $`(A,B,c)`$. The independent experiment samples $`U\in R_q^m`$ uniformly and independently and returns $`(A,U,c)`$, where $`c`$ has the **same genuine marginal** as in the real experiment. Correlations between $`S`$ and $`E`$ are allowed. Their independence from the public matrix is the only distributional requirement for the attack.

At even modulus, this parity is independent of the chosen coefficient representatives: changing an integer coefficient by a multiple of $`q`$ does not change its parity or the parity of its square.

Define the augmentation homomorphism

```math
\phi:R_q\longrightarrow\mathbb F_2,
\qquad \phi(f)=f(1)\bmod2.
```

Both the coefficient modulus and the relation $`X^N+1`$ vanish under this map. Since $`z^2=z`$ in $`\mathbb F_2`$,

```math
c=\sum_j\phi(S_j)+\sum_i\phi(E_i).
\tag{N1}
```

## The exact public test

### Theorem N1: Distribution-independent parity gap

Define the public event

```math
G(A):\qquad \sum_{i=1}^m\phi(A_{ij})=1
\quad\text{for every }j\in[k].
\tag{N2}
```

The deterministic test

```math
\mathcal D(A,B,c)=
\mathbf1\left\{G(A)\text{ and }c=\sum_i\phi(B_i)\right\}
```

has real acceptance probability $`2^{-k}`$ and independent-experiment acceptance probability $`2^{-(k+1)}`$. Its distinguishing advantage is therefore exactly $`2^{-(k+1)}`$.

*Proof.* Apply $`\phi`$ to every entry of the equation $`B=AS+E`$ and sum its rows. Combining the result with (N1) gives

```math
c+\sum_i\phi(B_i)
=\sum_{j=1}^{k}
 \left(1+\sum_{i=1}^{m}\phi(A_{ij})\right)\phi(S_j).
\tag{N3}
```

On $`G(A)`$, the right side is zero for every possible secret and error vector. Each augmentation column sum of uniform $`A`$ is a fair bit, and the $`k`$ sums are independent. Thus $`\Pr[G(A)]=2^{-k}`$, proving the real acceptance probability.

In the independent experiment, conditional on any fixed $`A,c`$, the bit $`\sum_i\phi(U_i)`$ is fair because $`m\ge1`$. The equality test therefore holds with probability $`1/2`$ on the gate, whatever the marginal distribution of $`c`$. Multiplying by the gate probability proves the result. $`\square`$

The test uses coefficient parity sums and binary comparisons, so it runs in polynomial time. It uses no anti-concentration condition, Gaussian approximation, or lower bound on the number of samples beyond $`m\ge1`$. For fixed module rank the gap is constant; it remains inverse-polynomial when $`k=O(\log\lambda)`$ for security parameter $`\lambda`$.

The ring structure explains why the gate depends on $`k`$, rather than the full secret coefficient dimension $`kN`$. In the coefficient expansion of each negacyclic multiplication block, all column sums are equal modulo two. An unstructured binary matrix with $`kN`$ independent columns would instead impose $`kN`$ independent gate conditions and give the corresponding probability $`2^{-kN}`$.

The test is also a special case of the [scalar ideal-dimension law](linear_leakage.md). Over $`R_2`$, the polynomial $`\Omega=1+X+\cdots+X^{N-1}`$ satisfies $`X\Omega=\Omega`$, so $`(\Omega)`$ is a one-dimensional ideal. Norm parity has this effective coefficient on every secret and error component. Its error-hint ideal therefore has dimension one.

## Consequence for the full covariance hint

Let the disclosed ring element be

```math
K=\sum_{j=1}^{k}S_j\overline{S_j}
   +\sum_{i=1}^{m}E_i\overline{E_i}\in R,
\qquad \bar f=f(X^{-1}).
\tag{N4}
```

For a polynomial $`f=\sum_{a=0}^{N-1}f_aX^a`$, expansion of $`f\bar f`$ shows

```math
\operatorname{ct}(f\bar f)=\sum_{a=0}^{N-1}f_a^2.
```

Only equal exponents contribute to the constant coefficient, since their differences lie strictly between $`-N`$ and $`N`$. Hence $`\operatorname{ct}(K)=C`$, and the test needs only the low bit of that coefficient. The same conclusion holds if the descriptor reveals $`K\bmod q`$, because $`q`$ is even.

At $`k=1`$, (N4) is the covariance descriptor in Micciancio–Suhl's Known-Covariance RLWE definition. Thus Theorem N1 gives advantage $`1/4`$ against its independent-sample benchmark throughout the even-modulus regime. For $`k>1`$, the theorem applies to the explicitly specified module analogue whenever its hint reveals the parity of the constant coefficient of (N4). [MS2025, Definition 12, p. 16](https://cic.iacr.org/p/1/4/2/pdf).

This is a decisional obstruction. It does not recover the secret or, by itself, distinguish plaintexts in a complete encryption scheme. For the one-bit augmented *search* problem, the standard guessing argument gives the complementary fact: an algorithm recovering the secret with success $`\varepsilon`$ from the genuine bit yields an ordinary search algorithm with success at least $`\varepsilon/2`$ by supplying an independent guessed bit. This argument covers the bit alone; it supplies no search-hardness theorem for the full covariance descriptor.

## Exact comparison with the preceding results

The source statements address different models and parameter ranges:

| Source and location | Statement relevant to this chapter | Boundary |
|---|---|---|
| [Micciancio–Suhl (2025), Definition 10 and Lemma 9, p. 10; Appendix B.2, p. 30](https://cic.iacr.org/p/1/4/2/pdf) | Ordinary LWE with a disclosed secret-and-error norm; Appendix B derives its decision guarantee through search-to-decision. | Appendix B.2 explicitly assumes a polynomially large **prime** modulus. It does not establish the even-modulus ring claim. |
| [Micciancio–Suhl (2025), Definition 12 and Section 5.3.2, pp. 16–17](https://cic.iacr.org/p/1/4/2/pdf) | Rank-one Ring-LWE with the exact covariance (N4), retaining that descriptor in both experiments. | The definition does not restrict the modulus to odd values; its ring hardness question is left open. |
| [Bkakria (2026), Theorem 6, Corollary 3, Lemma 10, and Section 9](https://eprint.iacr.org/2026/2638) | Rank-one public-Gram-determinant attacks using reciprocal or Hermitian components at odd primes, with stated activity conditions and separate one-sample results; divisor reduction transfers the proved attacks. | Section 6.3 and the conclusion on p. 31 leave pure power-of-two moduli outside those attack guarantees. |

Theorem N1 covers the even-modulus branch, including pure powers of two, with a distribution-independent constant gap at rank one and the displayed rank-dependent extension. It uses only a parity projection of the full descriptor. The reduction modulo two and the linearization of integer squares are the entire mechanism; no claim of a new general CRT attack technique is needed.

The ordinary prime-modulus known-norm result, the odd-prime ring attacks, and this even-modulus parity calculation are therefore compatible. The Gaussian characterization below also changes the benchmark: it preserves the public relation that the independent-sample experiment violates.

## The compatible ideal and the genuine parity marginal

The independent benchmark must retain the actual marginal of the leaked bit. A Gaussian norm-parity bit is very close to fair in the smoothed regime, but it is not exactly fair. Keeping these distributions separate gives an exact description of the unavoidable gap.

Let $`G(A)`$ be the public augmentation event

```math
\sum_{i=1}^m\phi(A_{ij})=1\qquad\text{for every }j\in[k].
```

Define $`\mathsf I_q`$ by sampling independent uniform $`A\in R_q^{m\times k}`$ and $`U\in R_q^m`$, then setting

```math
c=\begin{cases}
\sum_i\phi(U_i),&G(A),\\
\text{an independent fair bit},&\neg G(A).
\end{cases}
```

This is the exact transcript law when the full coefficient vectors of the secret and errors are uniform modulo two and the remaining bits of the public sample are uniformly masked. It is also the ideal to which the Gaussian reduction applies. The fairness assertion off the event holds even conditional on the **entire public sample**, not merely on its augmentation.

To see the full conditional law, expand multiplication by $`A`$ modulo two into $`M_A`$. For independent uniform binary coefficient vectors $`r_S,r_E`$, write $`z=M_A r_S+r_E`$. Given $`z`$, the vector $`r_S`$ remains uniform, and

```math
c=\mathbf1^Tz+(\mathbf1+M_A^T\mathbf1)^Tr_S.
```

The second term vanishes precisely on $`G(A)`$. Otherwise it is a nonzero linear functional of a uniform vector and hence is fair. This is a statement about the full binary system, including the identity error block.

Let $`\mathsf J_{\mathrm{fair}}`$ sample $`A,U,c`$ independently and uniformly. Let $`\mathsf J_t`$ instead sample $`c`$ independently from its genuine marginal for coefficient Gaussians of width $`t`$. Put $`d=N(k+m)`$ and

```math
\alpha_t=\left|\Pr[c=0]-\frac12\right|
=\frac12\left|\mathbb E_{Z\leftarrow D_{\mathbb Z,t}}(-1)^Z\right|^d.
```

The product formula follows because norm parity is the sum of the $`d`$ independent coefficient parities. In terms of one-dimensional Gaussian masses,

```math
\mathbb E_{Z\leftarrow D_{\mathbb Z,t}}(-1)^Z
=\frac{\sum_{z\in\mathbb Z}(-1)^z e^{-\pi z^2/t^2}}
       {\sum_{z\in\mathbb Z}e^{-\pi z^2/t^2}}.
```

The distances from the compatible ideal are exactly

```math
\begin{aligned}
\Delta(\mathsf I_q,\mathsf J_{\mathrm{fair}})
 &=2^{-(k+1)},\\
\Delta(\mathsf I_q,\mathsf J_t)
 &=2^{-(k+1)}+(1-2^{-k})\alpha_t.
\end{aligned}
```

The public event occurs with probability $`2^{-k}`$. On that event, averaging over the fair bit $`\sum_i\phi(U_i)`$ gives conditional distance $`1/2`$ from an independent bit with any marginal. Off the event, the only difference is the bias $`\alpha_t`$. These observations prove both formulas.

The simple gate test still has advantage **exactly** $`2^{-(k+1)}`$ between the real experiment and either independent benchmark, for every secret and error law independent of $`A`$. Its gap does not require the bit to be fair. At rank one the gap is $`1/4`$; for any fixed rank it is independent of the ring degree and number of samples. When the rank grows, the advantage decreases according to the displayed formula.

The [matching Gaussian theorem](gaussian_characterization.md) proves that, at a pure power-of-two modulus $`q\ge4`$, Gaussian norm parity is computationally indistinguishable from $`\mathsf I_q`$ under ordinary uniform-secret Module-LWE at modulus $`q/2`$ and width $`s=t/\sqrt8`$, with $`k`$ extra samples. Its explicit reduction bound is

```math
\operatorname{Adv}_{\mathsf T_{q,t},\mathsf I_q}(\mathcal D)
\le \frac{\operatorname{Adv}_{\mathrm{MLWE}(q/2,s,k+m)}(\mathcal B)}{p_k}
     +2\epsilon+2\delta,
\qquad p_k=\prod_{i=1}^{k}(1-2^{-i})>\frac14,
```

provided $`s/\sqrt2\ge\eta_\epsilon(\mathbb Z^d)`$. Here $`\delta`$ is the error of the reduction's product Gaussian sampler. The same hypothesis gives $`\alpha_t\le\epsilon`$. Thus the gate test is optimal up to negligible terms when the source assumption holds and the smoothing and sampling errors are negligible.

This positive characterization concerns only the single parity bit. Revealing the full coefficient norm or covariance also reveals that bit and therefore inherits the negative test, but the remaining information in the stronger hint is outside this positive theorem.
