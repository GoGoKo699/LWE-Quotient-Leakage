"""Exact finite checks of the affine-image and ideal-dimension formulas.

Only Python's standard library is used. The general results are proved in
science/linear_leakage.md; these examples test the field, ramified, dependent
hint, composite-modulus, and nonuniform-hidden-variable distinctions.
"""

from collections import Counter
from fractions import Fraction
from itertools import product
import json


def ring_mul(a, b, q):
    n = len(a)
    out = [0] * n
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[(i + j) % n] += x * y * (1 if i + j < n else -1)
    return tuple(x % q for x in out)


def star(a, q):
    return (a[0] % q,) + tuple(-x % q for x in a[:0:-1])


def dot(a, b, q):
    return sum(x * y for x, y in zip(a, b)) % q


def matvec(matrix, vector, q):
    return tuple(dot(row, vector, q) for row in matrix)


def coefficient_matrix(a, q):
    n = len(a)
    columns = [ring_mul(a, tuple(int(i == j) for i in range(n)), q)
               for j in range(n)]
    return [list(row) for row in zip(*columns)]


def image(matrix, q, columns):
    return {matvec(matrix, x, q) for x in product(range(q), repeat=columns)}


def tv(left, right):
    left_total, right_total = sum(left.values()), sum(right.values())
    return sum(abs(Fraction(left[key], left_total)
                   - Fraction(right[key], right_total))
               for key in left.keys() | right.keys()) / 2


def transcript_check(q, n, hs, he, hidden):
    """One ring sample and rank one; hints may have several coordinates."""
    rings = list(product(range(q), repeat=n))
    hint_count = len(hs)
    assert hint_count == len(he)
    h = [list(a) + list(b) for a, b in zip(hs, he)]
    w = image(h, q, 2 * n)
    hidden_hint = Counter()
    for (secret, error), weight in hidden.items():
        hint = tuple((dot(a, secret, q) + dot(b, error, q)) % q
                     for a, b in zip(hs, he))
        hidden_hint[hint] += weight
    real, independent = Counter(), Counter()
    real_accept = independent_accept = 0
    real_total = independent_total = 0
    image_sizes = Counter()
    predicted_gap = Fraction(0)
    for a in rings:
        ma = coefficient_matrix(a, q)
        residual = [[(hs[t][j] - sum(he[t][i] * ma[i][j]
                                    for i in range(n))) % q
                     for j in range(n)] for t in range(hint_count)]
        wa = image(residual, q, n)
        image_sizes[len(wa)] += 1
        predicted_gap += 1 - Fraction(len(wa), len(w))
        for (secret, error), weight in hidden.items():
            b = tuple((x + y) % q for x, y in zip(ring_mul(a, secret, q), error))
            hint = tuple((dot(x, secret, q) + dot(y, error, q)) % q
                         for x, y in zip(hs, he))
            residual_hint = tuple((x - y) % q
                                  for x, y in zip(hint, matvec(he, b, q)))
            real[(a, b, hint)] += weight
            real_accept += weight * (residual_hint in wa)
            real_total += weight
        for b in rings:
            for hint, weight in hidden_hint.items():
                residual_hint = tuple((x - y) % q
                                      for x, y in zip(hint, matvec(he, b, q)))
                independent[(a, b, hint)] += weight
                independent_accept += weight * (residual_hint in wa)
                independent_total += weight
    predicted_gap /= len(rings)
    actual_gap = (Fraction(real_accept, real_total)
                  - Fraction(independent_accept, independent_total))
    assert Fraction(real_accept, real_total) == 1
    assert actual_gap == predicted_gap
    distance = tv(real, independent)
    assert distance >= actual_gap
    return {
        'q': q, 'N': n, 'k': 1, 'm': 1,
        'hint_coordinates': hint_count,
        'hint_image_size': len(w),
        'residual_image_size_counts': dict(sorted(image_sizes.items())),
        'consistency_test_gap': str(actual_gap),
        'full_transcript_tv': str(distance),
    }


def scalar_ideal_case(name, p, n, u, v):
    rings = list(product(range(p), repeat=n))
    generated_ideal = {ring_mul(star(v, p), a, p) for a in rings}
    r = 0
    while p ** r < len(generated_ideal):
        r += 1
    assert p ** r == len(generated_ideal)
    feasible = star(u, p) in generated_ideal
    gates = sum(ring_mul(star(v, p), a, p) == star(u, p) for a in rings)
    expected_gate = Fraction(1, p ** r) if feasible else Fraction(0)
    assert Fraction(gates, len(rings)) == expected_gate
    expected_gap = expected_gate * (1 - Fraction(1, p))
    uniform = {(s, e): 1 for s in rings for e in rings}
    report = transcript_check(p, n, [u], [v], uniform)
    assert Fraction(report['consistency_test_gap']) == expected_gap
    assert Fraction(report['full_transcript_tv']) == expected_gap
    zero = (0,) * n
    unit = (1,) + (0,) * (n - 1)
    correlated = {(zero, zero): 2, (unit, v): 1}
    biased_report = transcript_check(p, n, [u], [v], correlated)
    assert Fraction(biased_report['consistency_test_gap']) == expected_gap
    return {'case': name, 'ideal_dimension': r, 'cancellation_feasible': feasible,
            'gate_probability': str(expected_gate), 'uniform': report,
            'correlated_hidden': biased_report}


def main():
    scalar = [
        scalar_ideal_case('split quotient evaluation', 5, 2, (0, 0), (1, 2)),
        scalar_ideal_case('split full ideal', 5, 2, (0, 0), (1, 0)),
        scalar_ideal_case('infeasible secret target', 5, 2, (1, 0), (1, 2)),
        scalar_ideal_case('irreducible quotient', 3, 2, (0, 0), (1, 2)),
        scalar_ideal_case('ramified parity ideal', 2, 4, (1, 1, 1, 1), (1, 1, 1, 1)),
        scalar_ideal_case('ramified intermediate ideal', 2, 4, (0, 0, 0, 0), (1, 0, 1, 0)),
    ]
    rings3 = list(product(range(3), repeat=2))
    uniform3 = {(s, e): 1 for s in rings3 for e in rings3}
    vector = transcript_check(3, 2, [[0, 0], [1, 0]], [[1, 0], [0, 1]], uniform3)
    dependent = transcript_check(3, 2, [[0, 0], [0, 0]], [[1, 0], [2, 0]], uniform3)
    assert vector['consistency_test_gap'] == vector['full_transcript_tv']
    assert dependent['hint_image_size'] == 3
    assert dependent['consistency_test_gap'] == dependent['full_transcript_tv']
    rings4 = list(product(range(4), repeat=1))
    uniform4 = {(s, e): 1 for s in rings4 for e in rings4}
    composite = transcript_check(4, 1, [[0]], [[1]], uniform4)
    assert Fraction(composite['full_transcript_tv']) == Fraction(5, 16)
    assert composite['residual_image_size_counts'] == {1: 1, 2: 1, 4: 2}
    return {'scalar_ideal_cases': scalar, 'vector_hint': vector,
            'dependent_hint_coordinates': dependent,
            'composite_modulus_partial_image': composite,
            'scope': 'Exact finite examples; universal claims are proved in science/linear_leakage.md.'}


if __name__ == '__main__':
    print(json.dumps(main(), indent=2, sort_keys=True))
