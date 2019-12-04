from itertools import groupby
import re


def check(n):
    nl = list(n)
    ans = True
    i = 0
    while ans and i < 5:
        if nl[i] > nl[i+1]:
            ans = False
        i += 1

    return ans


l,r = tuple(map(int, open('4.in').read().strip().split('-')))

V = list(map(str, range(l,r+1)))
r = re.compile("\\d*(\\d)\\1+\\d*")
ANS = list(filter(lambda x: r.match(x) and check(x), V))

print(len(ANS))
