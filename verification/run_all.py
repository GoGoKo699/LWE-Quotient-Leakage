"""Run finite checks and compare their deterministic reports with expected output."""

import argparse
import json
from pathlib import Path
import subprocess
import sys


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--refresh', action='store_true',
                        help='regenerate committed reports after reviewing a mathematical change')
    args = parser.parse_args()
    root = Path(__file__).resolve().parent
    names = ['check_linear_leakage', 'check_counterexample',
             'check_norm_parity', 'check_gaussian_identity']
    for name in names:
        completed = subprocess.run([sys.executable, str(root / (name + '.py'))],
                                   check=True, capture_output=True, text=True)
        actual = json.loads(completed.stdout)
        target = root / 'expected' / (name + '.json')
        if args.refresh:
            target.parent.mkdir(exist_ok=True)
            target.write_text(json.dumps(actual, indent=2, sort_keys=True) + '\n')
        else:
            expected = json.loads(target.read_text())
            if actual != expected:
                raise AssertionError(f'{name}: output differs from {target.name}')
        print(f'PASS {name}')
    print('All four finite checks passed. General statements rely on the written proofs.')


if __name__ == '__main__':
    main()
