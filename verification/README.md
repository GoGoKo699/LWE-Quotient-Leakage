# Verification route

The proofs in [science/](../science/model.md) establish the general claims. The scripts here check finite distributions and arithmetic identities that are useful for detecting convention, normalization, and implementation mistakes. They use Python's standard library only.

## Run the checks

With Python 3.10 or later, run from the repository root:

```sh
python3 verification/run_all.py
```

The runner executes each script, parses its JSON output, and compares it with the corresponding committed report in [expected/](expected/). A successful run prints one `PASS` line for each of the four scripts and exits with status zero. Each script can also be run directly to inspect its full report.

| Script | What it checks | Expected feature |
|---|---|---|
| [check_linear_leakage.py](check_linear_leakage.py) | Enumerates full finite transcripts for scalar and vector hints, dependent hint coordinates, correlated hidden laws, split and repeated-root rings, and a composite coefficient ring. Independently computes hint images and residual images. | The consistency gap agrees with the image formula. With uniform hidden variables it equals full transcript TV; with correlated variables the TV can be larger. The modulus-four example gives $`5/16`$. |
| [check_counterexample.py](check_counterexample.py) | Enumerates the $`17^3`$ projected triples and $`17^4`$ ring secrets, checks the evaluation fibers, the signed-permutation automorphisms, and the written theorem's parameter substitution. | Gap $`16/289`$, WLL advantage $`8/289`$, claimed recovery $`288/289`$, source bound $`1/4913`$, source batch size $`88{,}808`$. |
| [check_norm_parity.py](check_norm_parity.py) | Enumerates binary projected experiments at module ranks one, two, and three; checks full modulus-four negacyclic transcripts; verifies the integer identity in 1,500 deterministic seeded cases. | Gaps $`1/4,1/8,1/16`$ in the binary cases, full transcript TV $`1/4`$ in the modulus-four case, and no identity failures. |
| [check_gaussian_identity.py](check_gaussian_identity.py) | Computes the one-dimensional convolution of $`2U+V`$ at source widths $`0.5,1,2`$ and compares it with the exact theta-weighted formula, including both normalizers. | Pointwise discrepancy below $`10^{-13}`$ at the finite cutoff. The narrow-width examples retain a visible theta factor, so the convolution is not treated as an exact single Gaussian. |

## Exact arithmetic and numerical scope

The finite-distribution checks use integer counts and `fractions.Fraction`; their reported probabilities and distances are exact. They retain the same genuine hint marginal in the two challenge branches. Their matrix and coefficient arrays are explicit, so no sampling assumption enters those enumerations.

The Gaussian script uses floating-point arithmetic. Each input sum is truncated beyond twelve Gaussian widths, with a computed bound below $`10^{-100}`$ on its omitted unnormalized mass. The displayed convolution distances are rounded to ten decimal places. This is a consistency check of the scalar identity, not a numerical proof of the high-dimensional smoothing theorem. The latter is proved by Poisson summation and likelihood-ratio bounds in [the Gaussian chapter](../science/gaussian_characterization.md).

The script reports widths where the smoothing condition can fail as well as a wider example. This is intentional: a narrow Gaussian gives a concrete check that the theta factor and its normalizers cannot be discarded. The sampler used in the reduction is analyzed with an explicit statistical error in the proof; the numerical convolution check is not presented as a production cryptographic sampler.

## Updating a scientific check

After an intentional change to a script or a mathematical convention, inspect its assertions and full report. The runner supports regenerating expected outputs:

```sh
python3 verification/run_all.py --refresh
```

This runs the script assertions before writing the new reports. An updated expected file is evidence of a changed check, not independent evidence that the change is correct. Review the corresponding scientific statement and rerun without `--refresh` before committing.

No external solver, remote data, network request, or large search is required for this route. The checks are small finite certificates; they do not test practical cryptographic security or replace the asymptotic proofs.
