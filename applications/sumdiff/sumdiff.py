"""
find all a, b, c, d in q such that
f(a) + f(b) = f(c) - f(d)
"""

#q = set(range(1, 10))
#q = set(range(1, 200))
q = (1, 3, 4, 7, 12)

hash_min = {}
hash_sum = {}


def f(x):
    return x * 4 + 6


r = [f(x) for x in q[-1::-1]]

for i in r:
    for j in r:
        hash_sum[(i, j)] = i + j
        hash_min[(i, j)] = i - j

for k, v in hash_sum.items():
    for k2, v2 in hash_min.items():
        if v == v2:
            print(k, k2)
