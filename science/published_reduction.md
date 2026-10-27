# A quotient hint contradicts the written finite-batch reduction

## Statement and scope

A fixed, matrix-independent linear hint makes decisional Ring-LWE easy in a parameter regime admitted by the full version of Wang–Lai–Liu, *Ring/Module Learning with Errors under Linear Leakage—Hardness and Applications* [WLL24]. With uniform coefficient errors, the corresponding search problem remains information-theoretically unrecoverable after the one scalar hint supplied by the paper's finite-batch definition. This gives an unconditional counterexample to Theorem 3.9 under that definition.

All references to definitions, theorem numbers, and page numbers in this chapter refer to the **38-page ePrint version dated April 7, 2024**, whose source identity and retrieval limits are recorded in [the source audit](../references/wll_source_audit.md). The official publisher identifies a PKC 2024 chapter with the same title and broad reduction claim. Its full conference text has not been compared, so this chapter does not assert that every displayed conference theorem is identical.

The [general cancellation law](linear_leakage.md) explains why a hint supported on one small quotient has this effect. The obstruction concerns an augmented decision problem. The argument neither solves ordinary Ring-LWE nor establishes an attack on the paper's zero-knowledge application. The latter uses prescribed random hints, whereas the broad leakage game permits a chosen hint concentrated on one small quotient.

## 1. The finite-batch leakage game

Use the repository's notation throughout. The translation to WLL's symbols is:

| Meaning | This chapter | WLL |
| --- | --- | --- |
| Ring degree | $`N`$ | $`d`$ |
| Module rank | $`k`$ | $`n`$ |
| Number of samples | $`m`$ | $`m`$ |
| Terms summed inside the leakage functional | $`\kappa`$ | $`k`$ |
| Prime modulus | $`q`$ | $`q`$ |
| Prime-ideal factor count, with residue degree $`c`$ | $`\ell=N/c`$ | $`\ell=d/c`$ |

Ring-LWE is the case $`k=1`$. The counterexample uses $`\kappa=1`$.

Let

```math
R=\mathbb Z[X]/(X^N+1),\qquad R_q=R/qR,
```

where $`N`$ is a power of two. An error-leakage instance consists of

```math
A\leftarrow R_q^{m\times k},\qquad
S\leftarrow R_q^k,\qquad E\leftarrow\chi^m,\qquad
B=AS+E,
```

together with one scalar

```math
H=L(E)\in\mathbb F_q.
```

The adversary chooses $`L`$ before receiving $`A`$. Definition 3.1 permits arbitrary coefficient-linear functionals: choose $`\kappa=1`$, multiplier $`c_1=1`$, and the desired coefficient vector $`z_1`$. More generally, the displayed sum of $`\kappa`$ inner products still produces **one** element of $`\mathbb F_q`$, not $`\kappa`$ separate outputs. Definitions 3.4 and 3.5 supply this scalar once for the entire finite batch. [WLL24, pp. 12–14]

The search task is to recover the whole $`S`$. The decision task compares

```math
(A,AS+E,L(E))
\quad\text{and}\quad
(A,U,L(E)),
```

where $`U`$ is uniform in $`R_q^m`$ and independent of $`A,S,E`$. The secret-and-error variant also allows $`L(S,E)`$; an error-only hint is obtained by setting the secret coefficients to zero.

We distinguish two advantage conventions. A test has a **probability gap** equal to the absolute difference between its two acceptance probabilities. WLL's decision advantage is the optimal guessing success minus $`1/2`$, which is half that gap.

## 2. The quotient distinguisher

### Proposition 1: a fixed evaluation hint

Suppose $`q`$ is an odd prime and $`\alpha\in\mathbb F_q`$ satisfies $`\alpha^N=-1`$. Define the surjective ring homomorphism

```math
\rho:R_q\longrightarrow\mathbb F_q,\qquad \rho(f)=f(\alpha).
```

For any module rank $`k\ge1`$, any sample count $`m\ge1`$, and any secret/error distributions independent of the uniformly sampled matrix, the fixed hint

```math
H=\rho(E_1)
```

admits a polynomial-time test with probability gap

```math
\begin{aligned}
\Delta=q^{-k}(1-q^{-1}).
\end{aligned}
\tag{1}
```

**Proof.** The hint is coefficient-linear:

```math
H=\sum_{t=0}^{N-1}\alpha^t(E_1)_t\pmod q.
```

It is therefore a legal choice with $`\kappa=1`$, multiplier $`1`$, first error-coordinate coefficient vector $`(1,\alpha,\ldots,\alpha^{N-1})`$, and every other hint coefficient zero. It is fixed before the matrix is sampled.

Consider the public event

```math
G=\{\rho(A_{1j})=0\text{ for all }j\in[k]\}.
```

Since the $`k`$ matrix entries are independent and uniform and $`\rho`$ is onto,

```math
\Pr[G]=q^{-k}.
```

The test outputs “random” exactly when $`G`$ holds and $`\rho(B_1)\ne H`$.

In the real experiment,

```math
\rho(B_1)=\sum_{j=1}^k\rho(A_{1j})\rho(S_j)+\rho(E_1),
```

so $`G`$ forces $`\rho(B_1)=H`$. The test never outputs “random.”

In the random experiment, conditional on $`A`$ and $`H`$, the value $`\rho(U_1)`$ is uniform in $`\mathbb F_q`$. The test therefore outputs “random” with probability $`q^{-k}(1-q^{-1})`$. This proves (1). $`\square`$

The proof does not use uniform or large errors. In particular, the same chosen-hint decision obstruction applies to narrow Gaussian or other short errors. Uniform errors enter only the unconditional impossibility argument below.

The attack also applies directly to WLL's HNF secret-and-error decision game: ignore the secret positions of the leakage vector. For constant module rank and polynomial $`q`$, (1) is inverse polynomial. No claim is made that this particular gate remains useful when $`k`$ grows so quickly that $`q^{-k}`$ is negligible.

### Constant-degree field quotients

More generally, let $`\rho:R_q\to\mathbb F_{q^c}`$ be a surjective ring homomorphism and fix $`\beta\ne0`$ in that field. The base-field scalar

```math
H=\mathrm{Tr}_{\mathbb F_{q^c}/\mathbb F_q}
       (\beta\rho(E_1))
```

is still a legal coefficient-linear hint. The public event $`\rho(A_{1j})=0`$ for all $`j`$ has probability $`q^{-ck}`$ and forces the same trace of $`B_1`$ to equal $`H`$. The trace pairing is nondegenerate, so its value on a uniform field element is uniform in $`\mathbb F_q`$. The resulting test gap is therefore

```math
q^{-ck}(1-q^{-1}).
```

Thus the quotient mechanism also covers the constant residue-degree regime in the stated theorem. The fully split case $`c=1`$ already suffices for the unconditional counterexample below.

## 3. One batch scalar cannot recover the uniform-error source

### Proposition 2: information-theoretic search bound

Let $`\chi`$ be uniform on the centered coefficient representatives

```math
\begin{aligned}
\left\{-\frac{q-1}{2},\ldots,\frac{q-1}{2}\right\}^{N}\subset R.
\end{aligned}
\tag{2}
```

For every source batch size $`m`$, every chosen coefficient-linear scalar hint $`L(S,E)\in\mathbb F_q`$, and every algorithm, including an unbounded one, full-secret recovery from

```math
(A,AS+E,L(S,E))
```

has success probability at most

```math
\begin{aligned}
q^{1-Nk}.
\end{aligned}
\tag{3}
```

Without the hint, the optimal success probability is exactly $`q^{-Nk}`$.

**Proof.** Identify $`R_q^k`$ with $`\mathbb F_q^{Nk}`$ using the coefficient basis. Write $`T_A`$ for the $`\mathbb F_q`$-linear map induced by multiplication by the module matrix $`A`$.

The error in (2) is exactly uniform modulo $`qR`$. Conditional on any fixed $`A`$, the value

```math
B=T_A S+E
```

is uniform and independent of the uniform $`S`$. In particular, conditional on $`(A,B)`$, the secret still has $`q^{Nk}`$ equally likely possibilities.

Write the scalar linear hint as

```math
H=u^\top S+v^\top E.
```

After fixing $`A`$ and $`B`$, substitute $`E=B-T_A S`$:

```math
\begin{aligned}
H=v^\top B+(u^\top-v^\top T_A)S.
\end{aligned}
\tag{4}
```

Equation (4) imposes at most one linear equation on the $`Nk`$ secret coordinates. Every nonempty posterior fiber is an affine subspace with at least $`q^{Nk-1}`$ elements, and the posterior is uniform on that fiber. Even optimal guessing therefore succeeds with probability at most (3). $`\square`$

The bound is independent of $`m`$. Enlarging the source batch gives more uniformly masked equations but still only one scalar constraint on $`S`$.

There is also a cardinality version of the same argument. Conditional on $`(A,B)`$, any deterministic hint with at most $`q`$ possible values partitions $`q^{Nk}`$ equally likely secrets into at most $`q`$ nonempty cells. The optimal average guessing success is the number of nonempty cells divided by $`q^{Nk}`$, hence at most $`q^{1-Nk}`$. Thus replacing the linear functional by a more general single $`q`$-valued hint would not remove this information bound.

### The error distribution meets the invariance requirement

For $`N`$ a power of two, every automorphism of $`\mathbb Q[X]/(X^N+1)`$ sends $`X`$ to $`X^a`$ for an odd $`a`$. On the power basis, this is a signed permutation. The product of the symmetric uniform coefficient distributions in (2) is preserved exactly. Therefore $`\chi`$ satisfies Theorem 3.9's automorphism-invariance hypothesis as a distribution on the integer ring, not merely after reduction modulo $`q`$.

No global shortness restriction on $`\chi`$ is imposed by the formal theorem or its preceding definitions. The paper's separate discussion of Gaussian errors for its application does not impose such a restriction on Theorem 3.9. [WLL24, pp. 4, 9–15]

## 4. Contradiction to the written theorem

Theorem 3.9 permits prime $`q`$ with distinct constant-degree prime-ideal factors, $`\ell=N/c`$, and $`q\ge\ell^2`$. It claims a reduction from the finite-batch search problem with one error hint to a decision problem, with source sample count

```math
\begin{aligned}
\overline m^{\,*}
=\ell q^c mk\left\lceil\frac1{\epsilon^2}\right\rceil
\end{aligned}
\tag{5}
```

and source recovery probability at least

```math
\begin{aligned}
1-\frac{\epsilon}{8}.
\end{aligned}
\tag{6}
```

See the [source audit](../references/wll_source_audit.md) for the exact statement and notation conventions. [WLL24, p. 15]

Take $`k=m=\kappa=1`$ and a fully split prime, so $`c=1`$ and $`\ell=N`$. Proposition 1 gives a target solver with WLL advantage

```math
\begin{aligned}
\epsilon=\frac{q-1}{2q^2}.
\end{aligned}
\tag{7}
```

Proposition 2 gives an unconditional source upper bound $`q^{1-N}`$, regardless of the enlarged sample count in (5). These are incompatible with (6).

The same choice also contradicts the composed Corollary 3.19: ordinary search succeeds with probability exactly $`q^{-N}`$, whereas the corollary claims a solver with success at least $`(1/q)(1-\epsilon/8)`$. The one-scalar guessing argument in Theorem 3.8 is valid; the incompatible step is the claimed recovery from the easy decision problem. [WLL24, pp. 15, 21]

The theorem's prose switches once from the error-leakage label D-MLWELE to the secret-and-error label D-MLWE-LS. This notation inconsistency does not account for the contradiction: the same target attack works in both decision variants, and the same source upper bound holds for either single-scalar source variant under (2). We do not rely on interpreting an otherwise undefined expression literally.

### A small exact certificate

Set

```math
N=4,\quad q=17,\quad \alpha=2,\quad k=m=\kappa=1,\qquad
\chi=\mathrm{Unif}\{-8,\ldots,8\}^{4}.
```

The polynomial $`X^4+1`$ has the four distinct roots $`2,8,9,15`$ modulo $`17`$, and $`17\ge4^2`$. The legal hint is

```math
H=E_{1,0}+2E_{1,1}+4E_{1,2}+8E_{1,3}\pmod{17}.
```

| Quantity | Exact value |
| --- | --- |
| Probability of the public gate | $`1/17`$ |
| Real probability of the test output “random” | $`0`$ |
| Random probability of that output | $`16/289`$ |
| WLL guessing advantage $`\epsilon`$ | $`8/289`$ |
| Source sample count from (5) | $`88{,}808`$ |
| Claimed source success from (6) | $`288/289`$ |
| Unconditional upper bound on source success | $`1/4913`$ |

The companion certificate uses exact integer and rational arithmetic. It enumerates all $`17^3`$ projected triples and all $`17^4`$ ring secrets. It checks zero real rejections, $`272`$ random rejections out of $`4913`$ projected triples, and evaluation fibers of size $`4913`$. These computations verify the finite illustration; Propositions 1 and 2 prove the statements for arbitrary dimension and batch size.

### An unconditional asymptotic family

A finite example alone does not refute an asymptotic hardness statement. The following family closes that gap without a conjecture about the density of convenient primes.

For a security parameter $`\lambda`$, take

```math
N=2^{\lceil\log_2\lambda\rceil},\qquad
Q_N=2N^2,
```

and let $`q_N`$ be the least prime congruent to $`1`$ modulo $`Q_N`$. Linnik's theorem supplies absolute effective constants $`C,L`$ such that

```math
q_N\le C Q_N^L.
```

For example, Xylouris proves the sufficient bound $`L=5.2`$ in Theorem 1.1 of the inspected primary preprint [Xyl09, p. 9]. We need only that $`L`$ is an absolute constant.

Since $`1`$ is not prime, $`q_N\ge2N^2+1`$. Since $`2N`$ divides $`q_N-1`$, $`X^N+1`$ splits into distinct linear factors in $`\mathbb F_{q_N}`$. Consequently,

```math
q_N\ge N^2,\qquad q_N=\mathrm{poly}(\lambda),\qquad
\ell=N,\qquad c=1.
```

The family is uniformly constructible in polynomial time in $`\lambda`$: enumerate the progression until its first prime, test primality, and find a root by enumerating $`\mathbb F_{q_N}`$. Even elementary trial division is polynomial here because the integers enumerated have value polynomial in $`\lambda`$. This is an existence-and-complexity argument, not a proposed practical parameter generator.

For $`k=m=\kappa=1`$, the advantage (7) is $`\Theta(1/q_N)`$ and hence nonnegligible; (5) is $`O(Nq_N^3)`$ and hence polynomial; yet the source success bound $`q_N^{1-N}`$ is negligible. The contradiction therefore persists in a growing-dimensional, admissible, efficiently specified family.

## 5. What the proof audit establishes

The unconditional counterexample is the reason the written reduction cannot hold. Inspection of the proof also identifies a concrete resource that is not supplied by the stated game.

**One global hint does not supply individual block hints.** Lemma 3.14 uses many $`m`$-sample decision inputs to test candidate secret residues. The written source supplies a larger batch and one scalar over the entire batch. Separate leakage values for its blocks do not follow from that scalar. The proof needs an explicit simulation of those values or a different source oracle. [WLL24, pp. 17–18]

**The later normal-form step explicitly requests several scalar values.** Lemma 3.18 obtains tuples carrying separate $`\delta_i`$ values under several hint vectors and combines them with another $`\delta`$. Its footnote 8 appeals to the ability to choose hints. Choosing one functional in the finite-batch game does not authorize receiving all these separate values. This observation concerns the later step toward the secret-and-error game; it is not needed for the direct contradiction to Theorem 3.9. [WLL24, pp. 20–21]

**The automorphism calculation and the solver quantifier must be separated.** The coefficient-inner-product identity used in Lemma 3.11 is correct for the signed-permutation action. It transports a valid tuple while also transforming its hint vector. A success guarantee for a solver's chosen hint does not, by itself, give a success guarantee on every transformed hint. When combined with the useful CRT hybrid selected in Lemma 3.17, that quantifier needs explicit justification. We record this as an additional proof obligation, rather than claiming that the algebraic identity or every intervening lemma is false. [WLL24, pp. 16–20]

Reading the source as an oracle that returns a fresh scalar for every fresh block changes the resource. With $`t`$ unconstrained field-valued hints, the elementary guessing loss is $`q^t`$, whereas Theorem 3.8 accounts for one factor of $`q`$. A corrected oracle theorem must track both its total leakage and its hint quantifiers. Merely renaming the batch does not repair the stated result.

## 6. Boundary of the application claim

Remark 3.6 expressly distinguishes adversarially chosen hints from challenger-sampled hints. In the application, Lemma 4.6 uses Gaussian vectors $`z`$, short challenges $`c`$, and ternary commitment randomness $`r`$. The simulated proof uses a predicate of an inner product involving $`z`$ and automorphic challenge multiples of $`r`$. [WLL24, pp. 14, 29–30]

The evaluation vector in Proposition 1 is a deterministic chosen functional. We have not shown that the application's sampled functional has this form, that it concentrates on a small quotient with useful probability, or that the protocol reveals the evaluation predicate used by our test. Therefore the established consequence is failure of the broad chosen-hint reduction as written. Security of the specific random-hint assumption and proof protocol requires a separate analysis.

There is an additional application-specific congruence $`q-1\equiv2\ell\pmod{4\ell}`$ in Section 4. It is not a hypothesis of Theorem 3.9, and the $`N=4,q=17`$ certificate is not presented as an application parameter set. This separation prevents an application restriction from being silently moved into the broad theorem, or a broad theorem counterexample from being silently promoted into a protocol attack.

## References

**[WLL24]** Zhedong Wang, Qiqi Lai, and Feng-Hao Liu. *Ring/Module Learning with Errors under Linear Leakage—Hardness and Applications*. Cryptology ePrint Archive, paper 2023/826, full version dated April 7, 2024. [Official record](https://eprint.iacr.org/2023/826). Published chapter: PKC 2024, LNCS 14602, pp. 275–304, [DOI 10.1007/978-3-031-57722-2_9](https://doi.org/10.1007/978-3-031-57722-2_9). Exact version and coverage: [source audit](../references/wll_source_audit.md).

**[Xyl09]** Triantafyllos Xylouris. *On Linnik's constant*. arXiv:0906.2749v1, submitted June 15, 2009. [Versioned record](https://arxiv.org/abs/0906.2749v1), [PDF](https://arxiv.org/pdf/0906.2749v1). Definition of the least-prime function: p. 6; effective polynomial bound: Theorem 1.1, p. 9.
