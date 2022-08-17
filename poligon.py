from cmath import pi
from math import tan


def polysum(n, s):
    n = (0.25 * n * s ** 2) / tan(pi / n)
    s = (s * n) ** 2
    ans = n + s

    return ans


print(polysum(4, 5))
