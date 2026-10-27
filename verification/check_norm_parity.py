"""Finite exact checks for the norm-parity theorem. These do not replace its proof."""
from collections import Counter
from fractions import Fraction
from itertools import product
import json
import random


def mul(a, b):
    n = len(a)
    out = [0] * n
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            k = i + j
            out[k % n] += x * y * (1 if k < n else -1)
    return tuple(out)


def star(a):
    return (a[0],) + tuple(-x for x in a[:0:-1])


def binary_projection(m, k):
    real, rand = Counter(), Counter()
    real_hits = rand_hits = gates = 0
    avecs = list(product(range(2), repeat=m*k))
    svecs = list(product(range(2), repeat=k))
    evecs = list(product(range(2), repeat=m))
    for av in avecs:
        aa = [av[i*k:(i+1)*k] for i in range(m)]
        gate = all(sum(aa[i][j] for i in range(m)) % 2 == 1 for j in range(k))
        gates += gate
        for s in svecs:
            for e in evecs:
                c = (sum(s) + sum(e)) % 2
                b = tuple((sum(a*x for a,x in zip(row,s)) + ei) % 2 for row,ei in zip(aa,e))
                real[(av,b,c)] += len(evecs)
                real_hits += gate and ((sum(b) + c) % 2 == 1)
                for u in evecs:
                    rand[(av,u,c)] += 1
                    rand_hits += gate and ((sum(u) + c) % 2 == 1)
    nr, nu = sum(real.values()), sum(rand.values())
    assert nr == nu
    exact_tv = Fraction(sum(abs(real[t] - rand[t]) for t in real.keys() | rand.keys()),2*nr)
    expected = Fraction(1, 2**(k+1))
    assert real_hits == 0 and exact_tv == expected
    assert Fraction(rand_hits,nu) == expected
    return {'m':m,'k':k,'gate_probability':str(Fraction(gates,len(avecs))),
            'real_reject_probability':'0','random_reject_probability':str(expected),
            'projection_tv':str(exact_tv),'weighted_transcripts_per_branch':nr}


def negacyclic_exact():
    n,q=2,4
    rings=list(product(range(q),repeat=n))
    real,rand=Counter(),Counter()
    real_hits=rand_hits=0
    for a in rings:
        gate=sum(a)%2 == 1
        for s in rings:
            for e in rings:
                prod=mul(a,s)
                b=tuple((x+y)%q for x,y in zip(prod,e))
                c=(sum(x*x for x in s)+sum(x*x for x in e))%2
                covariance=tuple(x+y for x,y in zip(mul(s,star(s)),mul(e,star(e))))
                assert covariance[0]%2 == c
                assert sum(covariance)%2 == c
                real[(a,b,c)] += len(rings)
                real_hits += gate and ((sum(b)+c)%2 == 1)
                for u in rings:
                    rand[(a,u,c)] += 1
                    rand_hits += gate and ((sum(u)+c)%2 == 1)
    total=sum(real.values())
    tv=Fraction(sum(abs(real[t]-rand[t]) for t in real.keys()|rand.keys()),2*total)
    assert real_hits == 0 and Fraction(rand_hits,total)==Fraction(1,4) and tv==Fraction(1,4)
    return {'n':n,'q':q,'m':1,'k':1,'real_reject_probability':'0',
            'random_reject_probability':str(Fraction(rand_hits,total)),
            'full_mod4_transcript_tv_with_parity_hint':str(tv),'weighted_transcripts_per_branch':total}


def arbitrary_integer_checks():
    rng=random.Random(20261027)
    cases=0
    for n in [2,4,8]:
        for q in [2,4,8,12,30]:
            for _ in range(100):
                a=tuple(rng.randrange(q) for _ in range(n))
                s=tuple(rng.randrange(-30,31) for _ in range(n))
                e=tuple(rng.randrange(-30,31) for _ in range(n))
                b=tuple((x+y)%q for x,y in zip(mul(a,s),e))
                c=(sum(x*x for x in s)+sum(x*x for x in e))%2
                assert (c+sum(b))%2 == ((1+sum(a))*sum(s))%2
                cov=tuple(x+y for x,y in zip(mul(s,star(s)),mul(e,star(e))))
                assert cov[0] == sum(x*x for x in s)+sum(x*x for x in e)
                assert sum(cov)%2 == c
                cases+=1
    return {'cases':cases,'failure_count':0,'scope':'finite arithmetic checks only'}


if __name__ == '__main__':
    result={'binary_exact':[binary_projection(2,k) for k in [1,2,3]],
            'negacyclic_exact':negacyclic_exact(),
            'arbitrary_integer_checks':arbitrary_integer_checks()}
    print(json.dumps(result,indent=2))
