# Algebraic compatibility of coefficient-linear hints

This section isolates the information that a linear hint forces about an MLWE sample before any assumption about the noise is made. The main statement is a finite-distribution identity. It gives a public distinguishing test for every secret and error distribution, and gives the exact statistical distance when the hidden variables are uniform. For a scalar hint, the probability of the relevant public event is governed by the dimension of an ideal in the residue ring. This dimension, rather than the number of disclosed scalars alone, distinguishes a coefficient hint from a hint supported on one ring quotient.

All algebraic tools used here are standard: images of homomorphisms of finite groups, coefficient duality, ideals in a polynomial quotient, the Chinese remainder theorem, and determinant bounds. We include proofs to specify the distributions and the scope of the conclusions. In particular, the exact formula for uniform hidden variables is not, by itself, a hardness theorem for small errors.

## Model, notation, and advantage convention

Let $`N\geq 1`$ be the ring degree, $`k\geq 1`$ the module secret rank, and $`m\geq 1`$ the number of ring samples. Put

```math
R=\mathbb Z[X]/(X^N+1),\qquad
 R_q=(\mathbb Z/q\mathbb Z)[X]/(X^N+1).
```

Let $`p`$ be a prime divisor of the ciphertext modulus $`q`$. Coefficientwise reduction gives a surjective ring map $`R_q\longrightarrow R_p`$. Every ring element is represented in the basis $`1,X,\ldots,X^{N-1}`$; $`\mathrm{coef}`$ denotes this coefficient vector. A bar denotes the involution

```math
\bar f=f(X^{-1}),
```

which is well defined because $`X^N=-1`$, so $`X`$ is a unit. These definitions do not require $`X^N+1`$ to be squarefree modulo $`p`$. The power-of-two restriction on $`N`$ will be used only where stated explicitly.

Sample $`A\leftarrow R_q^{m\times k}`$ uniformly. Independently of $`A`$, sample $`(S,E)\leftarrow\mathcal D`$ in $`R_q^k\times R_q^m`$ and form

```math
B=AS+E.
```

The law $`\mathcal D`$ may be arbitrary and may correlate $`S`$ with $`E`$. It may also be the reduction modulo $`q`$ of an integer-valued law. Write $`\mathbf s,\mathbf e,\mathbf b`$ for the coefficient vectors of $`S,E,B`$ reduced modulo $`p`$. Let

```math
M_A\in\mathbb F_p^{mN\times kN}
```

be the coefficient matrix of multiplication by $`A`$ modulo $`p`$, so that $`\mathbf b=M_A\mathbf s+\mathbf e`$.

Fix an $`\ell`$-coordinate hint map

```math
H=[H_S\ H_E]\in\mathbb F_p^{\ell\times(k+m)N},
 \qquad h=H_S\mathbf s+H_E\mathbf e.
```

The hint map is fixed before $`A`$ is sampled. It need not have full row rank. Our results can also be conditioned on public randomness that chooses $`H`$ independently of $`A`$.

The real experiment $`\mathsf T_{\mathcal D,H}`$ outputs $`(A,B,h)`$. The independent experiment $`\mathsf J_{\mathcal D,H}`$ samples $`A`$ uniformly, $`U\leftarrow R_q^m`$ independently uniformly, and an independent copy of the genuine hint marginal $`h=H_S\mathbf s+H_E\mathbf e`$, and outputs $`(A,U,h)`$. In particular, the independent experiment does not silently replace a biased hint by a uniform one.

Throughout this section, distinguishing advantage means a difference in acceptance probabilities. Total variation distance is

```math
\Delta(P,Q)=\frac12\sum_x|P(x)-Q(x)|
            =\max_{\mathcal E}|P(\mathcal E)-Q(\mathcal E)|.
```

A convention based on $`|\Pr[\text{correct guess}]-1/2|`$ divides each stated gap by two.

## The affine-image law for vector hints

For a fixed public matrix $`A`$, define

```math
D_A=H_S-H_EM_A,\qquad
 W=\mathrm{Im}\,H,\qquad W_A=\mathrm{Im}\,D_A.
```

Both images are subspaces of $`\mathbb F_p^\ell`$. Write $`r_H=\dim W`$ and $`r_A=\dim W_A`$.

### Theorem A1: Affine-image law

With the preceding notation, the following statements hold.

#### (i) Public support test.

Every real transcript satisfies

```math
h-H_E\mathbf b\in W_A.
```

The public test accepting exactly when this membership holds has acceptance gap

```math
\begin{aligned}
\delta(H)=\mathbb E_A\left[1-p^{r_A-r_H}\right]
\end{aligned}
\tag{A1}
```

between $`\mathsf T_{\mathcal D,H}`$ and $`\mathsf J_{\mathcal D,H}`$, for every law $`\mathcal D`$ independent of $`A`$.

#### (ii) Exact uniform-hidden law.

If $`S`$ and $`E`$ are independent and uniform modulo $`q`$, then

```math
\begin{aligned}
\Delta(\mathsf T_{\mathcal D,H},\mathsf J_{\mathcal D,H})
 =\delta(H).
\end{aligned}
\tag{A2}
```

More precisely, conditional on $`A,B`$, the real hint is uniform on $`H_E\mathbf b+W_A`$.

#### (iii) Compatible experiment.

Define $`\mathsf I_H`$ by sampling uniform independent $`A,U`$ and then sampling $`h`$ uniformly on $`H_E\mathbf u+W_A`$, where $`\mathbf u=\mathrm{coef}(U\bmod p)`$. For uniform independent $`S,E`$, the identity

```math
\mathsf T_{\mathcal D,H}=\mathsf I_H
```

holds exactly. The experiment $`\mathsf I_H`$ is efficiently samplable: sample $`z\leftarrow\mathbb F_p^{kN}`$ uniformly and set $`h=H_E\mathbf u+D_Az`$.

*Proof.* Substituting $`\mathbf e=\mathbf b-M_A\mathbf s`$ gives the identity

```math
\begin{aligned}
h=H_E\mathbf b+D_A\mathbf s.
\end{aligned}
\tag{A3}
```

This proves the support constraint. We also have

```math
\begin{aligned}
W=W_A+\mathrm{Im}\,H_E.
\end{aligned}
\tag{A4}
```

Indeed, $`D_A=H_S-H_EM_A`$ shows that the right-hand side is contained in $`W`$, while $`H_S=D_A+H_EM_A`$ proves the reverse inclusion.

Fix $`A`$. In the independent experiment, $`\mathbf u`$ is uniform and independent of $`h`$. Equation (A4) implies that the image of $`H_E\mathbf u`$ in $`W/W_A`$ is uniform on the entire quotient. Every genuine hint belongs to $`W`$, regardless of its distribution. Therefore, conditional on any particular value of $`h`$, the independent experiment satisfies the support constraint with probability

```math
|W_A|/|W|=p^{r_A-r_H}.
```

The real experiment satisfies it with probability one. Averaging over $`A`$ proves (A1). No uniformity assumption on the hint marginal was used.

Now suppose $`S,E`$ are independent uniform variables modulo $`q`$. Conditional on $`A`$, the map $`(S,E)\mapsto(S,AS+E)`$ is a bijection. Thus $`B`$ is uniform, and conditional on $`A,B`$, the variable $`S`$ remains uniform in $`R_q^k`$. Its coefficient reduction $`\mathbf s`$ is consequently uniform in $`\mathbb F_p^{kN}`$. Equation (A3) makes $`h`$ uniform on $`H_E\mathbf b+W_A`$. The genuine unconditional hint marginal is uniform on $`W`$. The statistical distance between the uniform law on a coset of $`W_A`$ inside $`W`$ and the uniform law on $`W`$ is $`1-|W_A|/|W|`$. Since the $`A,B`$ marginals coincide in the two experiments, averaging this conditional distance proves (A2) and the claimed identity with $`\mathsf I_H`$.

Finally, a linear map sends a uniform input to a uniform element of its image. This proves the sampling assertion. Image membership and ranks are computable by finite-field linear algebra in time polynomial in $`N,k,m,\ell,\log p`$. $`\square`$

The theorem separates two statements that should not be conflated. For arbitrary $`\mathcal D`$, $`\delta(H)`$ is the exact advantage of the stated public support test and hence a lower bound on the total variation distance. Other dependencies can make the full distance larger. For uniform hidden variables, the affine support is the entire discrepancy. In particular, $`\delta(H)=0`$ does not establish computational hardness for small errors.

## Scalar hints and the ideal-dimension formula

Write $`\mathrm{ct}(f)`$ for the constant coefficient of the canonical representative of $`f\in R_p`$. The identity

```math
\begin{aligned}
\mathrm{ct}(\bar v x)
 =\sum_{a=0}^{N-1}v_ax_a
\end{aligned}
\tag{A5}
```

shows that this pairing is nondegenerate. To see the identity directly, expand $`\bar v x=\sum_{a,b}v_ax_bX^{b-a}`$: since $`-(N-1)\leq b-a\leq N-1`$, only $`a=b`$ contributes to the constant term. Thus every scalar coefficient-linear hint can be written uniquely as

```math
\begin{aligned}
h=\mathrm{ct}\left(
       \sum_{j=1}^k\bar u_jS_j+
       \sum_{i=1}^m\bar v_iE_i\right),
 \qquad u\in R_p^k,\quad v\in R_p^m.
\end{aligned}
\tag{A6}
```

Here and below the hidden variables inside an expression over $`R_p`$ are implicitly reduced modulo $`p`$.

Assume $`v\neq0`$ and define

```math
I=(\bar v_1,\ldots,\bar v_m)\subseteq R_p,
 \qquad r=\dim_{\mathbb F_p}I.
```

Consider the public event

```math
\begin{aligned}
G_{u,v}(A):\qquad
 \sum_{i=1}^m\bar v_iA_{ij}=\bar u_j
 \quad\text{in }R_p\text{ for every }j\in[k].
\end{aligned}
\tag{A7}
```

### Theorem A2: Scalar ideal-dimension law

If some $`\bar u_j\notin I`$, then $`G_{u,v}`$ is empty. Otherwise,

```math
\begin{aligned}
\Pr_A[G_{u,v}(A)]=p^{-kr}.
\end{aligned}
\tag{A8}
```

On $`G_{u,v}`$, the public sample forces

```math
\begin{aligned}
h=\mathrm{ct}\left(\sum_i\bar v_iB_i\right).
\end{aligned}
\tag{A9}
```

The test accepting when both (A7) and (A9) hold has acceptance gap

```math
\begin{aligned}
\delta(u,v)=
 \begin{cases}
 p^{-kr}(1-1/p),&\text{if every }\bar u_j\in I,\\
 0,&\text{otherwise},
 \end{cases}
\end{aligned}
\tag{A10}
```

for every hidden law independent of $`A`$. For uniform independent $`S,E`$, this is the exact statistical distance from the independent experiment.

*Proof.* For one matrix column, the map

```math
R_p^m\longrightarrow R_p,
 \qquad (a_i)_i\longmapsto\sum_i\bar v_i a_i
```

has image exactly $`I`$. Applied to uniform input it is uniform on $`I`$. The $`k`$ matrix columns are independent, proving the event probability. Substituting $`E=B-AS`$ into (A6) proves (A9) on the event.

In the independent experiment, for any fixed hint value, the scalar $`\mathrm{ct}(\sum_i\bar v_iU_i)`$ is uniform in $`\mathbb F_p`$: $`v\neq0`$ and nondegeneracy of (A5) make it a nonzero linear functional of a uniform vector. This gives the claimed gap.

For completeness, the vector-hint theorem also proves exactness under uniform hidden variables. The residual scalar functional is

```math
(S_j)_j\longmapsto
 \mathrm{ct}\left(\sum_j
    \left(\bar u_j-\sum_i\bar v_iA_{ij}\right)S_j\right).
```

By nondegeneracy it is zero exactly on $`G_{u,v}`$. Off that event it has rank one, so the conditional hint is uniform. On the event it is forced, giving conditional statistical distance $`1-1/p`$. $`\square`$

If $`v=0`$, the theorem’s nonzero-error-hint hypothesis is unavailable. With uniform independent $`S,E`$, a secret-only scalar hint is independent of $`A,B`$ because the uniform error masks $`B`$; the distance is zero. The identically zero hint is likewise trivial. These cases are already covered by Theorem A1.

### Proposition A3: Computing the ideal dimension

Let $`F=X^N+1`$ and let $`V_i\in\mathbb F_p[X]`$ be the degree-$`<N`$ representative of $`\bar v_i`$. If

```math
g=\gcd(F,V_1,\ldots,V_m)
```

is chosen monic, then

```math
\begin{aligned}
r=N-\deg g.
\end{aligned}
\tag{A11}
```

The formula remains valid when $`F`$ has repeated irreducible factors.

*Proof.* The preimage of $`I`$ under $`\mathbb F_p[X]\to R_p`$ is the ideal $`(F,V_1,\ldots,V_m)=(g)`$. Since $`g`$ divides $`F`$, the map

```math
\mathbb F_p[X]/(F/g)\longrightarrow I,
 \qquad a\longmapsto ga\bmod F
```

is a vector-space isomorphism. Its source dimension is $`\deg(F/g)=N-\deg g`$. $`\square`$

If $`F`$ is squarefree, the Chinese remainder theorem expresses $`R_p`$ as a product of finite fields. Each ideal selects some of these field factors, and $`r`$ is the sum of their residue degrees. Thus, in the fully split case, $`r`$ counts the active root components. When $`F`$ has repeated factors, the gcd formula remains correct, but interpreting $`r`$ as a count of distinct field factors can fail. The use of polynomial-quotient ideals and their CRT description is standard; compare the cyclic-code formulation in [Evra–Kowalski–Lubotzky (2017)](https://arxiv.org/abs/1703.01080).

### An individual coefficient versus a quotient value

The hint giving one error coefficient has $`v_1=X^a`$, a unit of $`R_p`$. It therefore has $`r=N`$ and gap $`p^{-kN}(1-1/p)`$. In contrast, if $`\alpha\in\mathbb F_p`$ satisfies $`\alpha^N=-1`$, the hint $`h=E_1(\alpha)`$ has

```math
v_1=1+\alpha X+\cdots+\alpha^{N-1}X^{N-1}.
```

Its adjoint coefficient polynomial is

```math
\bar v_1=-\alpha\,\frac{X^N+1}{X-\alpha},
```

so the generated ideal has dimension one. The resulting gap is $`p^{-k}(1-1/p)`$. This calculation uses only the existence of the displayed root; it does not require the entire polynomial to split. Both hints disclose one field element, but they have different algebraic support.

## Prime residue fields and composite coefficient rings

The assumption $`p\mid q`$ is essential when projecting a transcript modulo $`q`$ to $`\mathbb F_p`$: it makes the projection independent of the choice of integer representatives. The ciphertext modulus $`q`$ itself need not be prime. All preceding field statements remain valid for a prime residue projection of a composite ciphertext modulus.

If the hint instead takes values in $`(\mathbb Z/t\mathbb Z)^\ell`$ for a composite divisor $`t`$ of $`q`$, the vector law has a precise replacement. Let $`H_S,H_E,M_A`$ be matrices over $`\mathbb Z/t\mathbb Z`$, and define $`W,W_A`$ as their additive image groups. Then

```math
\begin{aligned}
\delta_t(H)=\mathbb E_A\left[1-\frac{|W_A|}{|W|}\right].
\end{aligned}
\tag{A12}
```

The same public affine-support test has this exact acceptance gap for every hidden law, and this is the exact statistical distance for uniform independent hidden variables. The proof of Theorem A1 uses only uniformity under homomorphisms of finite additive groups and the identity $`W=W_A+\mathrm{Im}\,H_E`$, so it applies without change. Image cardinalities can be evaluated by integer Smith normal form, or by a prime-power CRT decomposition.

Field ranks cannot simply be substituted at composite modulus. A nonzero scalar linear map over $`\mathbb Z/t\mathbb Z`$ can have a proper nonzero image. For example, take $`N=k=m=1`$, $`q=t=4`$, the hint $`h=E`$, and uniform independent $`S,E`$. For $`A=0,1,2,3`$, respectively, the image of the residual map $`S\mapsto-AS`$ has cardinality $`1,4,2,4`$. Consequently,

```math
\Delta=\frac14\left[(1-1/4)+0+(1-2/4)+0\right]=\frac5{16}.
```

The completely zero residual event $`A=0`$ accounts for only $`3/16`$ of this distance. At $`A=2`$, the hint still obeys a nontrivial residue constraint.

The scalar ideal argument does still determine the probability of complete cancellation over a composite coefficient ring: it is $`|I|^{-k}`$ when all targets belong to the image ideal. It does not imply that complete cancellation is the only source of an affine support constraint. This is why the dimension and scalar two-case formulas are stated over a field.

## Norm parity and known covariance at even modulus

Suppose $`q`$ is even and take $`p=2`$. Define the augmentation

```math
\varphi:R_q\longrightarrow\mathbb F_2,
 \qquad \varphi(f)=f(1)\bmod2.
```

This is a well-defined surjective ring map. For integer coefficient vectors, the bit

```math
\begin{aligned}
c=\left(\sum_{j=1}^k\|S_j\|_{\mathrm{coef}}^2+
           \sum_{i=1}^m\|E_i\|_{\mathrm{coef}}^2\right)\bmod2
\end{aligned}
\tag{A13}
```

equals $`\sum_j\varphi(S_j)+\sum_i\varphi(E_i)`$ because $`a^2=a\bmod2`$. It is independent of the chosen representatives modulo even $`q`$.

Put $`\Omega=1+X+\cdots+X^{N-1}\in R_2`$. Then $`X\Omega=\Omega`$, and $`\bar\Omega=\Omega`$. The ideal $`(\Omega)`$ is one-dimensional: all its elements are scalar multiples of $`\Omega`$. Thus (A13) is the scalar hint with every $`u_j=v_i=\Omega`$. The cancellation event becomes

```math
\begin{aligned}
G(A):\qquad\sum_{i=1}^m\varphi(A_{ij})=1
 \quad\text{for all }j\in[k].
\end{aligned}
\tag{A14}
```

It has probability $`2^{-k}`$. On this event,

```math
c=\sum_i\varphi(B_i).
```

### Corollary A4: Distribution-independent norm-parity gap

For every secret and error law independent of uniform $`A`$, the test

```math
\text{accept iff }G(A)\text{ and }c=\sum_i\varphi(B_i)
```

has acceptance gap $`2^{-(k+1)}`$ from the independent-uniform-sample experiment retaining the genuine norm-parity marginal. For uniform independent hidden variables this is the exact statistical distance.

*Proof.* This is Theorem A2 with $`p=2`$ and $`r=1`$. Equivalently, the real test accepts with probability $`2^{-k}`$, whereas the independent test accepts with probability $`2^{-k}/2`$ for either value of the independent hint bit. $`\square`$

The corresponding affine-image experiment samples uniform $`A,U`$, forces $`c=\sum_i\varphi(U_i)`$ on $`G(A)`$, and samples a fair independent bit off the event. Theorem A1 identifies this experiment exactly for uniform hidden variables. The [matching Gaussian characterization](gaussian_characterization.md) is a separate result: it compares Gaussian norm parity at modulus $`q`$ with this experiment using MLWE at modulus $`q/2`$ and an explicitly enlarged Gaussian width. It does not follow from the algebraic identity alone.

For comparison with known-covariance formulations, let

```math
K=\sum_j S_j\bar S_j+\sum_i E_i\bar E_i.
```

By (A5), $`\mathrm{ct}(K)`$ is the sum of the coefficient squared norms as an integer, or its residue if $`K`$ is given modulo $`q`$. At even modulus its parity therefore reveals (A13). The negative corollary applies to an experiment revealing $`K`$, or the full integer norm, because either reveals this bit. The positive matching theorem for the bit must not be promoted to a theorem for the complete covariance or the complete norm. The relevant known-covariance definition appears in [Micciancio–Suhl (2025)](https://cic.iacr.org/p/1/4/2); the odd-prime decision attacks in [Bkakria (2026)](https://eprint.iacr.org/2026/2638) are a separate comparator.

## When effective hints are short or sparse

A small ideal cannot be generated by an arbitrary short coefficient hint. The following elementary bounds make this qualification explicit. They concern the algebraic obstruction identified above; eliminating that obstruction does not establish a leakage hardness theorem.

### Proposition A5: Support and coefficient-window bounds

Let $`v_i\neq0`$ be one error coefficient in a scalar hint, let $`t_i`$ be the number of its nonzero coefficients modulo $`p`$, and let $`r=\dim(\bar v_1,\ldots,\bar v_m)`$. Then

```math
\begin{aligned}
r\,t_i\geq N.
\end{aligned}
\tag{A15}
```

If, after multiplication by a monomial unit, the nonzero coefficients of $`v_i`$ lie in a coefficient window of length $`w`$, then also

```math
\begin{aligned}
r\geq N-w+1.
\end{aligned}
\tag{A16}
```

*Proof.* The principal ideal $`(v_i)`$ is spanned by the $`N`$ negacyclic shifts $`v_i,Xv_i,\ldots,X^{N-1}v_i`$. Let its dimension be $`r_i\leq r`$; the bar involution preserves dimensions. Choose $`r_i`$ of these shifts as a basis. Their supports must collectively cover all $`N`$ coefficient positions: otherwise every vector in their span would vanish at an uncovered position, whereas the full family of shifts of nonzero $`v_i`$ does not. Every basis shift has $`t_i`$ nonzero coefficients, giving $`r_i t_i\geq N`$ and hence (A15).

For the second claim, multiply by the stated monomial unit, which leaves the principal ideal unchanged, and take a representative of degree at most $`w-1`$. Its gcd with $`X^N+1`$ has degree at most $`w-1`$. Proposition A3 gives principal-ideal dimension at least $`N-w+1`$. $`\square`$

The support estimate is the elementary shift-span form of a finite-dimensional uncertainty bound, not a new uncertainty principle. General group-algebra versions, including sharper estimates, appear in [Chen–Fan–Luo (2025)](https://arxiv.org/abs/2211.11204v3). Its direct proof above applies to negacyclic shifts, including repeated-root residue rings.

### Proposition A6: A coefficient-norm bound

Assume $`N`$ is a power of two. Let $`\widetilde v_i\in\mathbb Z[X]`$ be a degree-$`<N`$ integer lift of a nonzero error coefficient $`v_i\in R_p`$, and write $`B_i=\|\widetilde v_i\|_2`$ in the coefficient embedding. Then

```math
\begin{aligned}
p^{N-r}\leq B_i^N,
 \qquad
 r\geq N\bigl(1-\log_p B_i\bigr).
\end{aligned}
\tag{A17}
```

More generally, the same conclusion holds whenever $`\gcd(\widetilde v_i,X^N+1)=1`$ over $`\mathbb Q[X]`$.

*Proof.* Let $`C`$ be the integer $`N\times N`$ coefficient matrix for multiplication by $`\widetilde v_i`$ in $`\mathbb Z[X]/(X^N+1)`$. Its reduction modulo $`p`$ has rank $`r_i=\dim(v_i)\leq r`$. Integer Smith normal form therefore gives

```math
p^{N-r_i}\mid\det C.
```

The assumed coprimality makes $`\det C\neq0`$. When $`N`$ is a power of two, $`X^N+1`$ is irreducible over $`\mathbb Q`$, so coprimality holds for every nonzero representative of degree less than $`N`$. Consequently, $`p^{N-r}\leq|\det C|`$. Each column of $`C`$ is a signed permutation of the coefficient vector of $`\widetilde v_i`$ and has Euclidean norm $`B_i`$. Hadamard’s determinant bound gives $`|\det C|\leq B_i^N`$, proving the claim. $`\square`$

In particular, a one-dimensional error-hint ideal requires every nonzero generator to have full coefficient support, and every integer lift in the power-of-two cyclotomic case has norm at least $`p^{1-1/N}`$. More generally, if some nonzero effective error coefficient has norm at most $`p^{1-\gamma}`$, with $`0<\gamma\leq1`$, then $`r\geq\gamma N`$ and the scalar cancellation gap is at most $`p^{-k\gamma N}`$. Similarly, support size at most $`t`$ gives gap at most $`p^{-k\lceil N/t\rceil}`$. These are bounds on the identified test, not on all distinguishers.

The word *effective* is necessary. A syntactically short hint written as

```math
\sum_{a=1}^{a_0}\langle z_a,c_a x\rangle
```

has effective coefficient vector

```math
\sum_{a=1}^{a_0}\bar c_a z_a,
```

because $`\langle z,cx\rangle=\mathrm{ct}(\bar zcx) =\langle\bar c z,x\rangle`$. Arbitrary ring multipliers $`c_a`$ can destroy shortness or sparsity of the effective vector even when each displayed $`z_a`$ is short. For specified integer lifts, the elementary negacyclic convolution estimate

```math
\left\|\sum_a\bar c_a z_a\right\|_2
 \leq\sum_a\|c_a\|_1\|z_a\|_2
```

provides a sufficient effective-norm bound; it follows because each monomial shift is a signed coefficient isometry. Any use of Proposition A6 must verify such a bound for the actual error coefficients after all multipliers and sums are included.

## What the algebra does and does not establish

The scalar and vector laws identify public constraints imposed by exact coefficient-linear hints and measure their unavoidable distinguishing contribution. They apply to the independent-random-sample benchmark with the genuine hint marginal. In the uniform-hidden model, they also specify the complete conditional law and an exact compatible benchmark. A small-dimensional error-hint ideal can make the independent benchmark easy even when guessing the short hint preserves search hardness.

Three additional conclusions require separate arguments. First, short-error pseudorandomness relative to the compatible benchmark is a computational statement, supplied only in the parameter regime of the separate Gaussian reduction. Second, a counterexample for adversarially chosen hints does not automatically apply to a scheme that samples a restricted distribution of hints. Third, extracting one distinguishing bit from a norm or covariance descriptor does not prove that the descriptor reveals no further information. We make none of those inferences from the algebraic law.

For the specific applications, see the [published reduction audit](published_reduction.md), [norm-parity analysis](norm_parity.md), and [interpretation and limits](interpretation.md).
