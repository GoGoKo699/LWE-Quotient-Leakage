"""Exact finite-field certificate for the written WLL batch-leakage game.

No stochastic simulation. The root projection of a uniformly sampled ring
element is exactly uniform, so enumerating F_17 suffices for the event counts.
The ring-secret fiber calculation enumerates all 17^4 coefficient vectors.
"""
from collections import Counter
from fractions import Fraction
from itertools import product
import json

q, d, alpha, module_rank, sample_count = 17, 4, 2, 1, 1
assert pow(alpha, d, q) == q - 1
roots = [a for a in range(q) if (pow(a, d, q) + 1) % q == 0]
assert len(roots) == d
assert q >= d * d

weights = [pow(alpha, j, q) for j in range(d)]
real_rejects = 0
random_rejects = 0
real_trials = random_trials = 0

# Reject as random exactly when A(alpha)=0 and B(alpha)!=E(alpha).
for a, s, e in product(range(q), repeat=3):
    b = (a * s + e) % q
    real_rejects += (a == 0 and b != e)
    real_trials += 1
for a, b, leaked_e in product(range(q), repeat=3):
    random_rejects += (a == 0 and b != leaked_e)
    random_trials += 1

real_probability = Fraction(real_rejects, real_trials)
random_probability = Fraction(random_rejects, random_trials)
gap = random_probability - real_probability
guessing_advantage = gap / 2
assert real_probability == 0
assert gap == Fraction(16, 289)
assert guessing_advantage == Fraction(8, 289)

# In the uniform-error source, one scalar leakage gives at most one linear
# equation on the four F_q secret coefficients. A nonzero linear functional
# has exactly q^(d-1) elements in every fiber. This explicit functional is
# the evaluation hint, and the general statement follows by an invertible
# linear change of basis. The zero functional only increases the fiber size.
fibers = Counter()
for coeffs in product(range(-(q // 2), q // 2 + 1), repeat=d):
    fibers[sum(w * x for w, x in zip(weights, coeffs)) % q] += 1
assert set(fibers) == set(range(q))
assert set(fibers.values()) == {q ** (d - 1)}
source_max_recovery = Fraction(1, q ** (d - 1))
claimed_recovery = 1 - guessing_advantage / 8
assert source_max_recovery == Fraction(1, 4913)
assert claimed_recovery == Fraction(288, 289)
assert source_max_recovery < claimed_recovery

# The four automorphisms X -> X^t, t odd mod8, act on coefficients by
# signed permutations. Uniform centered coefficients are therefore invariant.
automorphisms = {}
for t in (1, 3, 5, 7):
    signed_permutation = []
    for j in range(d):
        exponent = j * t
        target = exponent % d
        sign = -1 if (exponent // d) % 2 else 1
        signed_permutation.append([target, sign])
    assert len({target for target, sign in signed_permutation}) == d
    automorphisms[str(t)] = signed_permutation

report = {
    "ring": "Z[X]/(X^4+1)",
    "q": q,
    "d": d,
    "alpha": alpha,
    "roots_mod_q": roots,
    "module_rank": module_rank,
    "target_sample_count": sample_count,
    "leakage_sum_parameter": 1,
    "error_distribution": "iid uniform centered coefficients in {-8,...,8}",
    "leakage": "e_0+2 e_1+4 e_2+8 e_3 mod17",
    "projection_weights": weights,
    "reject_rule": "a(alpha)=0 and b(alpha)!=leakage",
    "real_projected_trials": real_trials,
    "real_rejects": real_rejects,
    "random_projected_trials": random_trials,
    "random_rejects": random_rejects,
    "real_reject_probability": str(real_probability),
    "random_reject_probability": str(random_probability),
    "distinguishing_probability_gap": str(gap),
    "paper_guessing_advantage_epsilon": str(guessing_advantage),
    "number_of_ring_secrets": q ** d,
    "secret_fiber_sizes": {str(k): v for k, v in sorted(fibers.items())},
    "source_recovery_bound_any_batch_size_one_scalar": str(source_max_recovery),
    "theorem_3_9_claimed_recovery_lower_bound": str(claimed_recovery),
    "theorem_source_batch_size": 4 * 17 * ((289 * 289 + 63) // 64),
    "automorphism_signed_permutations": automorphisms,
    "scope": "Written finite-batch arbitrary linear-leakage game; not an attack on the actual random-hint ZK protocol.",
}
print(json.dumps(report, indent=2))
