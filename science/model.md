# Leakage, search, and the random comparison

Module-LWE publishes noisy linear equations over a polynomial ring. Revealing a function of their secret and errors changes the joint distribution that a decision assumption must describe. This project studies fixed leakage functions whose coefficients are chosen before the public matrix. The central question is which relations that leakage forces on the public response, and whether a random comparison can preserve those relations.

The [linear leakage theorem](linear_leakage.md) identifies the relations and their exact distinguishing probability. It leads to a [counterexample to a stated finite-batch reduction](published_reduction.md) and to a [norm-parity obstruction at even modulus](norm_parity.md). The [Gaussian characterization](gaussian_characterization.md) proves hardness against a comparison distribution that retains the parity relation. The [interpretation](interpretation.md) connects the results and their cryptographic scope.

## 1. Ring and coefficient conventions

Let

```math
R=\mathbb Z[X]/(X^N+1),\qquad R_q=R/qR,
```

where $`N\ge1`$ and $`q\ge2`$. Each ring element has a coefficient vector of length $`N`$ in the basis $`1,X,\ldots,X^{N-1}`$. Multiplication is negacyclic: $`X^N=-1`$. A power-of-two $`N`$ is required for the cyclotomic and Gaussian normal-form statements that say so explicitly. The basic coefficient-pairing theorem does not require that restriction.

For an integer lift $`x\in R`$, the coefficient norm is

```math
\|x\|_{\mathrm{coef}}^2=\sum_{a=0}^{N-1}x_a^2.
```

This is the norm of the sampled integer vector, rather than a choice of centered representative made after seeing a residue. Its parity is well-defined on $`R_q`$ when $`q`$ is even.

The involution and the constant-coefficient functional are

```math
x^\star=x(X^{-1}),\qquad
\operatorname{ct}(x)=x_0.
```

Since $`X^{-1}=-X^{N-1}`$, the pairing satisfies

```math
\operatorname{ct}(v^\star x)=\sum_{a=0}^{N-1}v_a x_a,
\qquad
\operatorname{ct}(x^\star x)=\|x\|_{\mathrm{coef}}^2.
```

The notation $`\bar x`$ in later chapters denotes the same involution as $`x^\star`$. The first identity holds over every coefficient modulus. The second holds over the integers before reduction.

| Symbol | Meaning |
|---|---|
| $`N`$ | Ring degree |
| $`k`$ | Module secret rank |
| $`m`$ | Number of ring samples |
| $`q`$ | Ciphertext or sample modulus |
| $`p`$ | Prime residue modulus, when used |
| $`A\in R_q^{m\times k}`$ | Uniform public matrix |
| $`S\in R^k`$, $`E\in R^m`$ | Sampled secret and errors, reduced modulo $`q`$ for the equations |
| $`B=AS+E\in R_q^m`$ | Public response |
| $`d=N(k+m)`$ | Total coefficient dimension for a Gaussian secret-error vector |
| $`M_A`$ | Coefficient matrix of multiplication by $`A`$; its modulus is specified locally |
| $`s,t`$ | Source and target Gaussian widths, respectively |

The letter $`k`$ always denotes module rank here. The published paper analyzed in [the counterexample](published_reduction.md) uses different letters; that page gives the translation.

## 2. The two leakage experiments

Fix a distribution $`\mathcal X`$ on the integer secret-error vector $`(S,E)`$ and a deterministic leakage function $`f`$. Both are specified independently of $`A`$. The distribution $`\mathcal X`$ may correlate $`S`$ and $`E`$ unless a theorem assumes independence.

The real experiment is

```math
(S,E)\leftarrow\mathcal X,\quad
A\leftarrow U(R_q^{m\times k}),\quad
B=AS+E\bmod q,\quad H=f(S,E),
```

and returns $`(A,B,H)`$. The independent-response experiment draws the same hidden vector and leakage, draws $`U\leftarrow U(R_q^m)`$ independently, and returns $`(A,U,H)`$. Thus the leakage has its genuine marginal distribution in both experiments. Replacing it by a uniform value is a separate comparison that needs justification.

For coefficient-linear leakage over a prime residue field, $`f`$ is represented by public coefficient matrices or by the ring pairing above. For norm parity, it is the single bit

```math
f(S,E)=\left(\|S\|_{\mathrm{coef}}^2+
                  \|E\|_{\mathrm{coef}}^2\right)\bmod2.
```

An adversary may select the permitted leakage coefficients before $`A`$ is drawn. A distribution prescribed by a protocol, such as a Gaussian distribution on hint coefficients, defines a narrower game. The [source comparison](../references/RELATED_WORK.md) keeps these two models separate.

### One finite batch

The finite-batch model gives one matrix, one response vector, and the stated leakage value for that entire batch. A sum of several coefficient inner products that is returned as one element of $`\mathbb F_q`$ remains one scalar. Increasing $`m`$ increases the number of public equations; it does not create additional leakage values.

A source that answers repeated requests for separate hints on sub-batches is a different resource. The [published-reduction analysis](published_reduction.md) identifies where this distinction matters.

## 3. Advantages and statistical distance

Throughout this repository, distinguishing advantage means an acceptance-probability difference:

```math
\operatorname{Adv}_{P,Q}(\mathcal D)
=\left|\Pr[\mathcal D(P)=1]-\Pr[\mathcal D(Q)=1]\right|.
```

If a challenger chooses equally between $`P`$ and $`Q`$, the best success probability is $`1/2+\operatorname{TV}(P,Q)/2`$. A convention that defines advantage as success minus $`1/2`$ therefore differs by a factor of two. The Wang-Lai-Liu comparison uses that paper's convention explicitly when substituting its numerical theorem parameters.

For finite distributions,

```math
\operatorname{TV}(P,Q)=\frac12\sum_z|P(z)-Q(z)|.
```

The algebraic tests give exact probability differences for every allowed hidden distribution. Their optimality as the full statistical distance is established when the hidden variables are uniform. For Gaussian hidden variables, the separate reduction gives computational bounds.

## 4. Search and bounded leakage

Search asks for the sampled secret $`S\bmod q`$. In particular, it asks for that hidden draw, rather than any secret that could be made consistent by choosing new errors. This distinction is explicit in the source game used in [the unconditional counterexample](published_reduction.md).

The following standard guessing argument will be used only as an inherited ingredient. Suppose $`f`$ takes values in a known set of size $`L`$, and a solver given $`(A,B,f(S,E))`$ recovers the secret with probability $`\epsilon`$. An ordinary search solver guesses a uniform leakage value, calls the augmented solver, and returns its answer. For each fixed original experiment, the guess is correct with probability $`1/L`$. Conditional on that event, the supplied input is exactly the real augmented input. Therefore the ordinary solver succeeds with probability at least $`\epsilon/L`$.

No verification of the returned secret is required for this success-probability reduction. For one leaked bit the loss is two. The argument also holds when the search solver is quantum and receives a classical transcript. Its role and prior use are recorded in [related work](../references/RELATED_WORK.md#bounded-leakage-and-search).

Consequently, an efficiently distinguishable augmented distribution can coexist with conditional search hardness. A positive search theorem alone does not establish the independent-response decision comparison.

## 5. The ordinary assumption used by the positive result

For modulus $`q_0`$, ordinary uniform-secret decision Module-LWE compares

```math
(A_0,A_0W+E_0)
\quad\text{and}\quad
(A_0,U_0),
```

where $`W\leftarrow U(R_{q_0}^k)`$, $`A_0`$ is uniform, and the coefficients of $`E_0`$ are independent discrete Gaussians of the stated width. Its normal-form version instead samples the coefficients of both secret and error independently from that Gaussian.

The width convention is

```math
\Pr[Z=z]\propto\exp(-\pi\|z\|_2^2/s^2),
\qquad Z\sim D_{\mathbb Z^a,s}.
```

The positive theorem uses normal-form Module-LWE modulo $`q/2`$ and then proves a constant-loss conversion from the ordinary uniform-secret assumption when $`q`$ and $`N`$ are powers of two. All sample counts, width changes, smoothing conditions, and sampling errors appear in [the Gaussian theorem](gaussian_characterization.md). Ordinary Module-LWE hardness is an assumption, not a result proved here.

## 6. Adversaries and resources

The attacks are classical and receive explicit public coefficient arrays and the declared leakage. They require no further leakage oracle. Quotient evaluation, polynomial gcds, and finite linear-image membership can be computed in polynomial time. The norm-parity test takes linear time in the displayed coefficient input. No quantum state-preparation or coherent sample access is assumed.

The positive reductions are classical randomized reductions on classical distributions. They can invoke either a classical or a quantum distinguisher. The latter conclusion requires the corresponding ordinary Module-LWE assumption against quantum polynomial-time algorithms. Statistical claims and the source-recovery information bound apply without computational restrictions.

## Reading onward

Continue with [linear leakage and public affine relations](linear_leakage.md). The exact finite examples are reproducible through [the verification route](../verification/README.md); the general statements are established by the written proofs.
