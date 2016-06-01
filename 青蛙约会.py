# -*- coding:utf-8 -*-
# 青蛙约会
def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


def frog(x, y, m, n, l):
    dx = abs(y - x)
    dv = abs(m - n)
    if dx % gcd(dv, l) != 0:
        return "Impossible"
    else:
        n = 0
        while True:
            if (dx - n * l) % dv == 0:
                return (dx - n * l) / dv


# test

# print gcd(2, 6)
print frog(1, 2, 3, 4, 5)
