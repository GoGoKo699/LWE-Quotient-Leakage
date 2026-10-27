# A matching Gaussian characterization of norm parity

The parity obstruction admits a matching positive statement.  At an even
modulus, a uniform transcript must preserve a public binary relation on a
recognizable set of matrices.  We prove that, for sufficiently smoothed
coefficient Gaussians at a pure power-of-two modulus $`q\ge4`$, ordinary Module-LWE
accounts for every efficient distinguishing advantage beyond this relation.
For other even moduli $`q\ge4`$, we prove the corresponding statement from normal-form
Module-LWE.  The target of the reduction
is a precisely defined, efficiently samplable distribution.  The result
concerns the single norm-parity bit; it does not establish security when the
whole norm or covariance is revealed.

The proof uses established Gaussian smoothing and convolution machinery
[MR07](https://cseweb.ucsd.edu/~daniele/papers/Gaussian.pdf), [GPV08](https://people.csail.mit.edu/cpeikert/pubs/trap_lattice.pdf), [Pei10](https://sites.cc.gatech.edu/fac/cpeikert/pubs/pargauss.pdf), together with the normal-form transformation of
Applebaum, Cash, Peikert, and Sahai [ACPS09, Lemma 2](https://www.wisdom.weizmann.ac.il/~bennyap/pubs/kdm-learning.pdf).  We give the
specialized calculations and all normalizers, because the dependence between
the output Gaussian and its parity is essential here.  We do not claim a new
general Gaussian convolution technique.

Modulus conversion is also an established LWE technique; a general
modulus-and-dimension transformation appears in
[BLPRS13, Theorem 3.1](https://arxiv.org/html/1306.0281v1#S3).
The integral doubling map used here and its joint law with the leaked parity
are proved explicitly below.

## Distributions and conventions

Let $`N\ge 2`$ be a power of two, let

```math
R=\mathbb Z[X]/(X^N+1),\qquad R_q=R/qR,
```

and let $`k,m\ge 1`$.  Put $`d=N(k+m)`$.  We identify elements of $`R^k\times R^m`$
with their $`d`$ integer coefficients.  For $`w>0`$, write

```math
\rho_w(x)=\exp(-\pi\|x\|_2^2/w^2),\qquad
 D_{\mathbb Z^d,w}(x)=\frac{\rho_w(x)}{\rho_w(\mathbb Z^d)}.
```

Thus $`w`$ is a Gaussian *width*; the corresponding continuous standard
deviation is $`w/\sqrt{2\pi}`$.  All widths in this section refer to the
coefficient embedding.  In a power-of-two cyclotomic ring, the full canonical
embedding with all $`N`$ complex embeddings scales squared Euclidean norms by $`N`$, so a statement using
canonical-embedding widths must scale these widths by $`\sqrt N`$.

For even $`q`$, define the augmentation homomorphism

```math
\phi:R_q\longrightarrow\mathbb F_2,
 \qquad \phi(f)=f(1)\bmod 2.
```

It is well defined because both $`q`$ and $`(X^N+1)(1)=2`$ vanish modulo two.
For a public matrix $`A\in R_q^{m\times k}`$, let

```math
\mathcal G(A):\quad
 \sum_{i=1}^{m}\phi(A_{ij})=1\quad\text{for every }j\in\{1,\ldots,k\}.
 \tag{G1}
```

The real norm-parity transcript $`\mathsf T_{q,t}`$ is sampled as follows:

```math
\begin{aligned}
 A&\leftarrow U(R_q^{m\times k}),\\
 (S,E)&\leftarrow D_{\mathbb Z^d,t},\\
 b&=AS+E\pmod q,\\
 c&=(\|S\|_{\mathrm{coef}}^2+\|E\|_{\mathrm{coef}}^2)\bmod2.
 \end{aligned}
 \qquad\text{Return }(A,b,c).
```

All randomness in the first two lines is independent.  Integer squares
satisfy $`z^2=z\pmod2`$, so

```math
c=\sum_{j=1}^{k}\phi(S_j)+\sum_{i=1}^{m}\phi(E_i).
 \tag{G2}
```

The *constraint-preserving ideal* $`\mathsf I_q`$ samples
$`A\leftarrow U(R_q^{m\times k})`$ and $`u\leftarrow U(R_q^m)`$ independently,
and then sets

```math
c=\begin{cases}
       \sum_i\phi(u_i),&\mathcal G(A),\\
       \text{an independent uniform bit},&\neg\mathcal G(A).
    \end{cases}
 \qquad\text{Return }(A,u,c).
 \tag{G3}
```

We also distinguish two independent benchmarks.  In $`\mathsf J_{\mathrm{fair}}`$,
$`A,u,c`$ are mutually independent and uniform on their respective spaces.
In $`\mathsf J_t`$, $`A,u`$ are independent uniform, while $`c`$ is sampled
independently from its **genuine marginal law** in $`\mathsf T_{q,t}`$.
The latter marginal need not be exactly fair.  Define its bias by

```math
\alpha_t=\left|\Pr_{\mathsf T_{q,t}}[c=0]-\frac12\right|.
```

For any two distributions $`P,Q`$ on the same space, write
$`\Delta(P,Q)=\frac12\sum_x|P(x)-Q(x)|`$.  The distinguishing advantage of an
algorithm $`\mathcal D`$ is the absolute difference of its acceptance
probabilities, without an additional factor of one half.

## The forced bit and the independent benchmarks

### Lemma G1: The exact parity ideal

For every fixed $`A`$, let $`r_S\in\mathbb F_2^{kN}`$ and
$`r_E\in\mathbb F_2^{mN}`$ be independent uniform vectors.  Let $`M_A`$ be the
coefficient matrix for multiplication by $`A`$ modulo two.  The joint law

```math
z=M_A r_S+r_E,\qquad c=\mathbf1^T r_S+\mathbf1^T r_E
```

has $`z`$ uniform.  Conditional on the entire vector $`z`$, the bit $`c`$ is
$`\mathbf1^Tz`$ if $`\mathcal G(A)`$ holds and is an independent fair bit
otherwise.

*Proof.*
Given $`z`$, the vector $`r_S`$ remains uniform and
$`r_E=z-M_A r_S`$.  Consequently

```math
c=\mathbf1^Tz+(\mathbf1+M_A^T\mathbf1)^T r_S.
 \tag{G4}
```

A nonzero binary linear functional of a uniform vector is fair.  Every column
of a negacyclic multiplication matrix has, modulo two, the same sum as the
coefficient vector of its defining polynomial.  Thus the $`j`$th block of
$`M_A^T\mathbf1`$ is constant, with value $`\sum_i\phi(A_{ij})`$.
The functional in the second term vanishes exactly on $`\mathcal G(A)`$.
$`\square`$

For uniform $`A`$, its $`k`$ augmentation column sums are independent fair bits;
therefore

```math
\Pr[\mathcal G(A)]=2^{-k}.
 \tag{G5}
```

Moreover, the identity
$`c=\sum_i\phi(b_i)`$ on $`\mathcal G(A)`$ holds for *every* choice of
integer secret and errors, with no distributional assumption.  It follows that
the efficient test

```math
\mathcal D_{\mathrm{gate}}(A,b,c)=
 \mathbf1\{\mathcal G(A)\ \text{and}\ c=\sum_i\phi(b_i)\}
```

has advantage exactly $`2^{-(k+1)}`$ against either independent benchmark.
Indeed, its acceptance probabilities are $`2^{-k}`$ and $`2^{-(k+1)}`$,
respectively.  The latter equality holds for any independent marginal of $`c`$,
because $`\sum_i\phi(u_i)`$ is fair when $`m\ge1`$.

The corresponding distances from the corrected ideal are also explicit:

```math
\begin{aligned}
 \Delta(\mathsf I_q,\mathsf J_{\mathrm{fair}})
     &=2^{-(k+1)},\\
 \Delta(\mathsf I_q,\mathsf J_t)
     &=2^{-(k+1)}+(1-2^{-k})\alpha_t.
 \end{aligned}
 \tag{G6}
```

Off the gate, the second comparison is a fair bit versus the genuine
marginal, at distance $`\alpha_t`$.  On the gate, averaging over the fair bit
$`\sum_i\phi(u_i)`$ gives distance $`1/2`$, regardless of that marginal.

For independent coefficient Gaussians, the bias has the exact expression

```math
\alpha_t=\frac12\left|
    \frac{\sum_{z\in\mathbb Z}(-1)^z e^{-\pi z^2/t^2}}
         {\sum_{z\in\mathbb Z}e^{-\pi z^2/t^2}}
                 \right|^{d}
   =\frac12\left|\mathbb E_{Z\leftarrow D_{\mathbb Z,t}}(-1)^Z\right|^d.
 \tag{G7}
```

This follows by multiplying the $`d`$ independent parity characters.  In
particular, it does not replace the genuine marginal by a fair bit silently.

## A Gaussian lift that preserves the leaked bit

Define normal-form Module-LWE with parameters $`(R,q_0,k,m,s)`$ as the decision
problem between

```math
\mathsf{NFReal}_{q_0,s}:
 \quad A_0\leftarrow U(R_{q_0}^{m\times k}),\quad
 (U_S,U_E)\leftarrow D_{\mathbb Z^d,s},\quad
 b_0=A_0U_S+U_E\pmod{q_0},
```

and $`\mathsf{NFRand}_{q_0}`$, in which $`A_0,b_0`$ are independent uniform.
The challenge is the classical finite batch $`(A_0,b_0)`$; the reduction has no
access to $`U_S`$ or $`U_E`$.

For the integer lattice we use the usual smoothing convention

```math
\eta_\epsilon(\mathbb Z^d)
  =\inf\left\{a>0:
        \sum_{w\in\mathbb Z^d\setminus\{0\}}
                 e^{-\pi a^2\|w\|_2^2}\le\epsilon\right\}.
```

This is the Micciancio–Regev smoothing parameter [MR07](https://cseweb.ucsd.edu/~daniele/papers/Gaussian.pdf); translated
Gaussian mass bounds are stated explicitly in
[GPV08, Lemma 2.7](https://people.csail.mit.edu/cpeikert/pubs/trap_lattice.pdf) and [Pei10, Lemma 2.4](https://sites.cc.gatech.edu/fac/cpeikert/pubs/pargauss.pdf).

### Theorem G2: Matching normal-form reduction

Let $`q=2q_0`$ with $`q_0\ge2`$, let $`0<\epsilon<1/2`$, and suppose

```math
\frac{s}{\sqrt2}\ge\eta_\epsilon(\mathbb Z^d),
 \qquad t=\sqrt8\,s.
 \tag{G8}
```

For every distinguisher $`\mathcal D`$, there is a distinguisher $`\mathcal B`$
for normal-form Module-LWE at $`(R,q_0,k,m,s)`$ such that

```math
\mathrm{Adv}_{\mathsf T_{q,t},\mathsf I_q}(\mathcal D)
 \le
 \mathrm{Adv}_{\mathsf{NFReal}_{q_0,s},\mathsf{NFRand}_{q_0}}
                 (\mathcal B)+2\epsilon+2\delta.
 \tag{G9}
```

Here $`\delta`$ is the total variation error of the reduction's one product
Gaussian sample.  With ideal Gaussian sampling one may set $`\delta=0`$.
With polynomially encoded parameters, every inverse-polynomial or negligible
choice of $`\delta`$ with polynomially bounded $`\log(1/\delta)`$ is attainable
in probabilistic polynomial time.  The same statement holds for QPT
distinguishers on classical challenge inputs.

*Proof.*
First analyze exact Gaussian sampling.  On input $`(A_0,b_0)`$, take the
canonical coefficient representatives of $`A_0`$ in $`\{0,\ldots,q_0-1\}`$.
Choose a matrix $`K`$ with independent uniform binary coefficients, sample
$`V=(V_S,V_E)\leftarrow D_{\mathbb Z^d,2s}`$ independently, and output

```math
\begin{aligned}
 A&=A_0+q_0K\pmod q,\\
 b&=2b_0+AV_S+V_E\pmod q,\\
 c&=\mathbf1^T\mathrm{coef}(V)\pmod2.
 \end{aligned}
 \tag{G10}
```

The map $`(A_0,K)\mapsto A`$ is a bijection on coefficient representatives, so
$`A`$ is exactly uniform modulo $`q`$.

**Real branch.**
Write $`U=(U_S,U_E)`$ for the source's hidden Gaussian vector and put
$`X=2U+V`$.  Since $`2(A-A_0)=qK`$, the public value in
(G10) satisfies

```math
b=AX_S+X_E\pmod q.
```

Also $`X\equiv V\pmod2`$, so $`c`$ is exactly the norm parity of $`X`$.
The vector $`X`$ is independent of $`A`$.

It remains to compare the *joint* latent vector $`X`$ with the target
product Gaussian.  Define

```math
\Theta_a(v)=\sum_{u\in\mathbb Z^d}
                    e^{-\pi\|u-v\|_2^2/a^2}.
```

Completing the square gives, for every $`x\in\mathbb Z^d`$,

```math
\frac{\|u\|_2^2}{s^2}
 +\frac{\|x-2u\|_2^2}{4s^2}
 =\frac{2\|u-x/4\|_2^2}{s^2}
  +\frac{\|x\|_2^2}{8s^2},
```

and therefore the exact mass formula

```math
\Pr[X=x]
 =\frac{\rho_{\sqrt8s}(x)\,\Theta_{s/\sqrt2}(x/4)}
        {\rho_s(\mathbb Z^d)\rho_{2s}(\mathbb Z^d)}.
 \tag{G11}
```

In particular, neither normalizer in the denominator is omitted.

Poisson summation and the smoothing definition imply, for every real $`v`$ and
$`a\ge\eta_\epsilon(\mathbb Z^d)`$,

```math
a^d(1-\epsilon)\le\Theta_a(v)\le a^d(1+\epsilon).
 \tag{G12}
```

Indeed, after dividing by $`a^d`$, the zero dual-lattice term is one and the
absolute sum of all other Fourier terms is at most $`\epsilon`$.
Let $`Q=D_{\mathbb Z^d,\sqrt8s}`$ and
$`f(x)=\Theta_{s/\sqrt2}(x/4)`$.  Equation
(G11) says precisely that
$`\Pr[X=x]/Q(x)=f(x)/\mathbb E_Q[f]`$.
Thus the density ratio lies between $`\Gamma^{-1}`$ and $`\Gamma`$, where
$`\Gamma=(1+\epsilon)/(1-\epsilon)`$.

For any density ratio $`r\in[\Gamma^{-1},\Gamma]`$,
$`|r-1|\le((\Gamma-1)/(\Gamma+1))(r+1)`$ pointwise.  Integrating gives
$`\Delta(P,Q)\le(\Gamma-1)/(\Gamma+1)=\epsilon`$.
Consequently

```math
\Delta(\mathcal L(X),D_{\mathbb Z^d,t})\le\epsilon.
 \tag{G13}
```

Applying the same deterministic map
$`(A,X)\mapsto(A,AX_S+X_E,\|X\|_2^2\bmod2)`$ to the two distributions proves
that the full real output transcript is within $`\epsilon`$ of
$`\mathsf T_{q,t}`$.  This data-processing step preserves the dependence
between the Gaussian and the leaked bit.

For the Gaussian marginal, this is also a specialization of
[Pei10, Theorem 3.1](https://sites.cc.gatech.edu/fac/cpeikert/pubs/pargauss.pdf)
to the lattices $`\mathbb Z^d`$ and $`2\mathbb Z^d`$, with both input widths
$`2s`$. Its first draw is $`2U`$; the second is independent because
$`\mathbb Z^d-2U=\mathbb Z^d`$. The explicit mass calculation above records
the sharper error constant used here.

**Uniform branch.**
Conditional on $`A,V`$, the value $`2b_0`$ is uniform on the even-coefficient
subgroup of $`R_q^m`$.  Hence $`b`$ is uniform on the full coefficient-parity coset

```math
\{y\in R_q^m:y\bmod2=M_A(V_S\bmod2)+(V_E\bmod2)\}.
 \tag{G14}
```

This conditional distribution depends on $`V`$ only through its complete
coefficient parity vector $`r`$, not only through its augmentation.  For each
$`r\in\{0,1\}^d`$,

```math
\Pr[V\bmod2=r]=
       \frac{\Theta_s(r/2)}{\rho_{2s}(\mathbb Z^d)}.
 \tag{G15}
```

The hypothesis implies $`s\ge\eta_\epsilon(\mathbb Z^d)`$.  Comparing these
$`2^d`$ masses with their average and using the same reciprocal likelihood-ratio
argument shows

```math
\Delta(\mathcal L(V\bmod2),U(\mathbb F_2^d))\le\epsilon.
```

Replace $`r`$ by uniform at this cost.  Lemma G1
then gives the corrected conditional law of $`c`$, even given the entire
coefficient parity of $`b`$.  The higher coefficient bits of $`b`$ are uniform
within (G14).  Thus the resulting law is exactly
$`\mathsf I_q`$, and the actual uniform-branch output is within $`\epsilon`$ of
that ideal.

The triangle inequality now proves (G9) with
$`\delta=0`$.  Replacing the independent sample $`V`$ by one at distance at most
$`\delta`$ changes each output branch by at most $`\delta`$, giving the stated
$`2\delta`$ term.  The algorithm invokes $`\mathcal D`$ once and otherwise
performs classical sampling and ring arithmetic.
$`\square`$

The statistical parameter can be chosen explicitly.  The standard bound
[Pei10, Lemma 2.5](https://sites.cc.gatech.edu/fac/cpeikert/pubs/pargauss.pdf)

```math
\eta_\epsilon(\mathbb Z^d)
 \le\sqrt{\frac{\ln(2d(1+1/\epsilon))}{\pi}}
```

shows that it suffices to take
$`s\ge\sqrt{2\ln(2d(1+1/\epsilon))/\pi}`$.
Also $`t/2=\sqrt2s\ge\eta_\epsilon(\mathbb Z^d)`$, so the residue-mass
argument applied to $`D_{\mathbb Z^d,t}`$ gives

```math
\alpha_t\le\epsilon.
 \tag{G16}
```

The exact expression (G7) may be much smaller.

## From ordinary uniform-secret Module-LWE

We now specialize to $`q=2^a`$ with $`a\ge2`$.  Set $`q_0=q/2`$.
Ordinary decision Module-LWE at parameters $`(R,q_0,k,k+m,s)`$ compares

```math
C\leftarrow U(R_{q_0}^{(k+m)\times k}),\quad
 W\leftarrow U(R_{q_0}^{k}),\quad
 e\leftarrow D_{\mathbb Z^{N(k+m)},s},\quad
 v=CW+e\pmod{q_0}
```

with independent uniform $`(C,v)`$.  This definition fixes the ring, coefficient
Gaussian convention, sample count, and uniform-secret source assumption.

### Lemma G3: Normal form over the local ring

For every normal-form distinguisher $`\mathcal B`$ with $`m`$ samples there is an
ordinary uniform-secret Module-LWE distinguisher $`\mathcal B'`$ with $`k+m`$
samples, at the same source modulus $`q_0`$ and width $`s`$, satisfying

```math
\mathrm{Adv}_{\mathrm{MLWE}(q_0,s,k+m)}(\mathcal B')
 =p_k\mathrm{Adv}_{\mathrm{NFMLWE}(q_0,s,m)}(\mathcal B),
 \qquad
 p_k=\prod_{i=1}^{k}(1-2^{-i})>\frac14.
 \tag{G17}
```

*Proof.*
The ring $`R_{q_0}`$ is local.  Every maximal ideal contains the nilpotent
element $`2`$, and

```math
R_{q_0}/2R_{q_0}\simeq\mathbb F_2[X]/((X+1)^N)
```

has the unique maximal ideal generated by $`X+1`$.  Thus the unique maximal
ideal of $`R_{q_0}`$ is $`(2,X+1)`$ and its residue field is $`\mathbb F_2`$, with
residue map $`\phi`$.

A square matrix over this commutative ring is invertible exactly when its
determinant is a unit, equivalently when its augmentation is invertible over
$`\mathbb F_2`$.  A uniform $`B\in R_{q_0}^{k\times k}`$ therefore has
invertibility probability $`p_k`$: reveal the columns of its uniform binary
augmentation one at a time.  The $`i`$th column avoids the span of the previous
$`i-1`$ columns with probability $`1-2^{i-1-k}`$.
For completeness, $`p_1=1/2`$, and for $`k\ge2`$,

```math
p_k\ge\frac12\frac34
       \left(1-\sum_{i=3}^{k}2^{-i}\right)
       \ge\frac{9}{32}>\frac14.
```

Split the challenge rows into $`(B,v_B)`$ with $`k`$ rows and $`(C_1,v_1)`$ with
$`m`$ rows.  If $`B`$ is not invertible, output a fixed bit.  Otherwise form

```math
A_0=C_1B^{-1},\qquad b_0=v_1-A_0v_B.
 \tag{G18}
```

In the real branch, writing the two error blocks as $`e_B,e_1`$ gives
$`b_0=e_1-A_0e_B`$.  The new secret $`-e_B`$ and errors $`e_1`$ have the required
independent Gaussian distributions.  Conditional on any invertible $`B`$,
$`A_0`$ is uniform and independent of both error blocks.  Conditioning on
invertibility does not change their laws because the event depends only on
the public matrix.  In the uniform branch, $`v_1-A_0v_B`$ is still independent
uniform given $`A_0`$.

The two challenge branches have the same abort probability, and the same
fixed output on abort.  Conditional on non-abort they are exactly the two
normal-form branches.  Multiplying the signed acceptance difference by
$`p_k`$ and taking absolute values proves (G17).
This is the standard normal-form argument [ACPS09, Lemma 2](https://www.wisdom.weizmann.ac.il/~bennyap/pubs/kdm-learning.pdf), with its
local-ring invertibility probability and finite sample loss made explicit.
$`\square`$

### Corollary G4: Ordinary-MLWE characterization

Under the hypotheses of Theorem G2, suppose also that
$`q=2^a`$ with $`a\ge2`$.  For every $`\mathcal D`$ there is an ordinary
uniform-secret Module-LWE distinguisher $`\mathcal B'`$ such that

```math
\mathrm{Adv}_{\mathsf T_{q,t},\mathsf I_q}(\mathcal D)
 \le
 \frac{\mathrm{Adv}_{\mathrm{MLWE}(q/2,s,k+m)}(\mathcal B')}{p_k}
       +2\epsilon+2\delta.
 \tag{G19}
```

Consequently,

```math
\begin{aligned}
 \mathrm{Adv}_{\mathsf T_{q,t},\mathsf J_{\mathrm{fair}}}(\mathcal D)
 &\le 2^{-(k+1)}+
       \frac{\mathrm{Adv}_{\mathrm{MLWE}(q/2,s,k+m)}(\mathcal B')}{p_k}
       +2\epsilon+2\delta,\\
 \mathrm{Adv}_{\mathsf T_{q,t},\mathsf J_t}(\mathcal D)
 &\le 2^{-(k+1)}+(1-2^{-k})\alpha_t+
       \frac{\mathrm{Adv}_{\mathrm{MLWE}(q/2,s,k+m)}(\mathcal B')}{p_k}
       +2\epsilon+2\delta.
 \end{aligned}
 \tag{G20}
```

The explicit gate test attains $`2^{-(k+1)}`$ against both benchmarks.
If the source assumption holds and $`\epsilon,\delta`$ are negligible, this
characterizes the optimal efficient distinguishing advantage up to negligible
terms.

The complete parameter accounting is:

| Parameter | Ordinary MLWE source | Norm-parity target |
|---|---|---|
| Ring degree and module rank | $`N,k`$ | $`N,k`$ |
| Modulus | $`q/2`$ | $`q`$ |
| Ring samples | $`k+m`$ | $`m`$ |
| Secret distribution | Uniform in $`R_{q/2}^k`$ | Coefficient Gaussian of width $`t`$ |
| Error width | $`s`$ | $`t=\sqrt8s`$ |
| Auxiliary hint | None | One actual total norm-parity bit |
| Decision reference | Independent uniform sample | The compatible ideal $`\mathsf I_q`$ |

The source and target use the same ring degree and module rank.  The source
uses $`k`$ additional ring samples, modulus $`q/2`$, and Gaussian width
$`s=t/\sqrt8`$.  The reduction loses exactly the factor $`p_k`$ in the
normal-form step; the two smoothing and two sampling terms are not divided by
$`p_k`$.  For a general even modulus $`q`$, the normal-form theorem still applies,
but the uniform-secret conversion above is asserted only when $`q`$ is a pure
power of two.  No worst-case lattice reduction for additional parameter
regimes is claimed.

## Sampling, computational model, and scope

The probability calculations use ideal discrete Gaussians, while an actual
reduction uses a finite-precision sampler.  There is no infinite-support or
real-arithmetic oracle hidden in the computational claim.  The product
Gaussian on $`\mathbb Z^d`$ can be sampled coordinatewise using the one-dimensional
rejection sampler of [GPV08, Section 4.1, Lemmas 4.2--4.3](https://people.csail.mit.edu/cpeikert/pubs/trap_lattice.pdf); see also the
rounding implementation discussion in [Pei10, Section 4.1](https://sites.cc.gatech.edu/fac/cpeikert/pubs/pargauss.pdf).

For an explicit implementation, assume $`s^2`$ is a positive rational of
polynomial bit length, and $`N,k,m,\log q,\log(1/\delta)`$ are polynomially
bounded in the security parameter.  Set $`w=2s`$ and choose

```math
T\ge\max\left\{1,\sqrt{\ln(24d/\delta)/\pi}\right\},\quad
 C=\lceil wT\rceil,\quad
 L\ge 5e^{\pi}T\ln(4d/\delta).
```

For each coordinate, repeatedly choose a uniform integer in $`[-C,C]`$ and
accept $`z`$ with probability $`\rho_w(z)`$, stopping after $`L`$ attempts
and returning the fixed value zero if no attempt succeeds.
The smoothing hypothesis implies $`w\ge1`$.  The exact acceptance probability
per attempt is at least $`e^{-\pi}/(5T)`$, by restricting to $`|z|\le w`$.
The Gaussian tail outside $`[-C,C]`$ is at most
$`6e^{-\pi T^2}\le\delta/(4d)`$, and the cutoff failure probability is at most
$`\delta/(4d)`$.

Implement each acceptance probability to absolute error at most
$`\delta/(4dL)`$, and implement each uniform interval draw with failure at most
$`\delta/(4dL)`$.  A union bound over the attempted draws and coordinates adds
at most the remaining $`\delta/2`$.  The resulting product sample is therefore
within $`\delta`$ of $`D_{\mathbb Z^d,2s}`$.
These operations require polynomial precision: on the truncated interval
the exponent has polynomial magnitude, and its evaluation uses
$`w^2=4s^2`$, a rational input.  The interval may be large, but uniform sampling
uses its binary representation rather than an enumeration of its elements.
Standard bitwise rejection with a polynomial cutoff implements the stated
uniform-draw error.  Ring operations, invertibility tests, and inverses modulo
a power of two likewise have polynomial bit complexity.
On a uniform-draw failure the sampler likewise returns a fixed value; this
failure event is included in the stated sampling error.

All challenges and transcripts are classical.  For a QPT distinguisher,
the same reduction invokes it on the produced classical transcript.
Total variation distance equals trace distance for the corresponding diagonal
classical states, so the same error bounds apply.  The statement does not
grant coherent access to a sampling oracle or any extra leakage interface.

Finally, if an integer covariance element

```math
C_{\mathrm{int}}=\sum_{j=1}^{k}S_j\overline{S_j}
                    +\sum_{i=1}^{m}E_i\overline{E_i}\in R
```

is revealed, its constant coefficient is exactly
$`\|S\|_{\mathrm{coef}}^2+\|E\|_{\mathrm{coef}}^2`$.
Thus the negative parity test applies to that stronger leakage experiment by
projection.  The positive theorem applies only after projecting the hint to
this single bit.  It neither simulates $`C_{\mathrm{int}}`$ nor shows that its
remaining coefficients or the remaining norm bits are harmless.
