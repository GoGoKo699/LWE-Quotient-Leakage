"""Numerical check of the exact scalar theta identity, with explicit tail bounds.

This protects the center-dependent normalizer in the Gaussian proof. It is
not a statistical experiment, a sampler-security test, or a proof of smoothing.
"""

from collections import defaultdict
import json
import math


def rho(width, x):
    return math.exp(-math.pi * (x / width) ** 2)


def radius(width):
    return max(8, math.ceil(12 * width))


def discarded_mass_bound(width, cutoff):
    # For decreasing f, sum_{j=cutoff+1}^infty f(j) <= integral_cutoff^infty f(x) dx.
    # The displayed bound follows by x/cutoff >= 1 in the Gaussian integral.
    return width * width * math.exp(-math.pi * (cutoff / width) ** 2) / (math.pi * cutoff)


def weights(width):
    cutoff = radius(width)
    mass = {x: rho(width, x) for x in range(-cutoff, cutoff + 1)}
    total = math.fsum(mass.values())
    return {x: w / total for x, w in mass.items()}, total, cutoff


def run_case(s):
    u, zu, ru = weights(s)
    v, zv, rv = weights(2 * s)
    convolution = defaultdict(float)
    for x, px in u.items():
        for y, py in v.items():
            convolution[2 * x + y] += px * py
    target_width = math.sqrt(8) * s
    all_x = range(-2 * ru - rv, 2 * ru + rv + 1)
    gaussian_mass = {x: rho(target_width, x) for x in all_x}
    zg = math.fsum(gaussian_mass.values())
    target = {x: w / zg for x, w in gaussian_mass.items()}
    theta_width = s / math.sqrt(2)
    errors = []
    for x in all_x:
        center = x / 4
        cutoff = radius(theta_width)
        lo = math.floor(center) - cutoff
        hi = math.ceil(center) + cutoff
        theta = math.fsum(rho(theta_width, z - center) for z in range(lo, hi + 1))
        identity = rho(target_width, x) * theta / (zu * zv)
        errors.append(abs(convolution[x] - identity))
    identity_error = max(errors)
    assert identity_error < 1e-13
    distance = math.fsum(abs(convolution[x] - target[x]) for x in all_x) / 2
    assert discarded_mass_bound(s, ru) < 1e-100
    assert discarded_mass_bound(2 * s, rv) < 1e-100
    # The narrow case makes the theta factor visibly necessary.
    if s == 0.5:
        assert distance > 0.1
    return {'source_width': s, 'target_width_formula': 'sqrt(8)*source_width',
            'convolution_tv_to_single_gaussian': round(distance, 10),
            'theta_identity_max_error_below_1e-13': identity_error < 1e-13,
            'each_input_omitted_unnormalized_mass_below_1e-100': True}


if __name__ == '__main__':
    report = {'cases': [run_case(s) for s in (0.5, 1.0, 2.0)],
              'scope': 'Finite floating-point consistency check; the analytic smoothing bounds are proved in the scientific account.'}
    print(json.dumps(report, indent=2, sort_keys=True))
