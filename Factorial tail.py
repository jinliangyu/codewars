"""
Factorial tail
The problem

How many zeroes are at the end of the factorial of 10? 10! = 3628800,
i.e. there are two zeroes.
16! in hexadecimal would be 0x130777758000, which results in three
zeroes.

Unfortunately machine integer numbers has not enough precision for
larger values. Floats drops the tail we need. We can fall back to
arbitrary-precision ones - built-ins or from a library, but
calculating the full product isn't an efficient way to find
the tail of the factorial. Calculating 100'000! takes around 10
seconds on my machine, let alone 1'000'000!.

Your task

is to write a function, which will find number of zeroes at the end
of (number) factorial in arbitrary radix = base for larger numbers.

base is an integer from 2 to 256
number is an integer from 1 to 1'000'000
"""

# Clever Method
# from math import log

# def zeroes(base, number):
#   f = 1
#   c = 0
#   b = base**int(log(1000000,base))
#   for i in range(2,number+1):
#     f *= i
#     while f%base == 0:
#       f /= base
#       c += 1
#     f = f%b
#   return c

# Clever Method


def zeroes(base, number):
    noz = number
    j = base
    for i in range(2, base + 1):
        if (j % i == 0):
            p = 0
            while (j % i == 0):
                p = p + 1
                j = j / i
            c = 0
            k = number
            while (k / i > 0):
                c = c + k / i
                k = k / i
            noz = min(noz, c / p)
    return noz

