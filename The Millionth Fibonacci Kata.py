# Method 1
# def fib(n):
#     if n <= 2:
#         return 1
#     else:
#         return fib(n - 1) + fib(n - 2)

# Method 2
# def fib(n):
#     a, b = 0, 1
#     for i in range(n):
#         a, b = b, a + b
#     return a
# def fib(n):

# Method 3
# def fib(n):
#     value = fib_iter(1, 0, 0, 1, abs(n))
#     if n >= 0:
#     	return value
#     else:
#     	return (-1)**(-n+1)*value


# def fib_iter(a, b, p, q, count):
#     if count == 0:
#         return b
#     if count % 2 == 0:
#         return fib_iter(a, b, p * p + q * q, 2 * p * q + q * q, count / 2)
#     else:
#         return fib_iter(b * q + a * q + a * p, b * p + a * q, p, q, count - 1)


# Method 4
# def fib(n):
#     a = 0
#     b = 1
#     for i in range(abs(n)):
#         a, b = b, a + b
#     if n >= 0:
#         return a
#     else:
#         return (-1)**(n+1)*a

# Method 5 My method
# import numpy as np


# def fib(n):
#     f1 = np.matrix([[1, 1], [1, 0]], dtype=object)
#     f2 = np.matrix([[-1, 1], [1, 0]], dtype=object)
#     a = np.matrix([[1], [0]], dtype=object)
#     b = np.matrix([[0], [1]], dtype=object)

#     if n >= 0:
#         return (f1**n * a)[1, 0]
#     else:
#         return (f2**(-n) * b)[0, 0]

# Method 6
# def multvec(m, v):
#     return [
#         m[0][0] * v[0] + m[0][1] * v[1],
#         m[1][0] * v[0] + m[1][1] * v[1],
#     ]


# def matmult(a, b):
#     c = [[0, 0], [0, 0]]
#     for i in xrange(2):
#         for j in xrange(2):
#             for k in xrange(2):
#                 c[i][j] += a[i][k] * b[k][j]
#     return c


# def matpow(m, n):
#     if n == 1:
#         return m
#     mp = matpow(m, n >> 1)
#     res = matmult(mp, mp)
#     if n & 1:
#         res = matmult(res, m)
#     return res


# def calcTerm(v, m, n):
#     mp = matpow(m, n - 1)
#     return multvec(mp, v)[1]


# def fib(n):
#     if n >= 0 and n <= 1:
#         return n
#     if n > 1:
#         return calcTerm([0, 1], [[0, 1], [1, 1]], n)
#     else:
#         return calcTerm([1, 0], [[0, 1], [1, -1]], 1 - n)

# print fib(-96)  # -51680708854858323072(L)

# Other clever method
from numpy import matrix


def fib(n):
    return (matrix(
        '0 1; 1 1' if n >= 0 else '-1 1; 1 0', object
    ) ** abs(n))[0, 1]


# def fib(n):
#     value = fib_iter(a=1, b=0, p=0, q=1, n=abs(n))
#     if n < 0 and n % 2 == 0:
#         value *= -1
#     return value


# def fib_iter(a, b, p, q, n):
#     if n == 0:
#         return b
#     if n % 2 == 0:
#         return fib_iter(a, b, p**2 + q**2, 2*p*q + q**2, n/2)
#     return fib_iter(b*q+a*q+a*p, b*p+a*q, p, q, n-1)

print fib(-96)

# def fib(n):
#   if n < 0: return (-1)**(n % 2 + 1) * fib(-n)
#   a = b = x = 1
#   c = y = 0
#   while n:
#     if n % 2 == 1:
#       (x, y) = (a * x + b * y,
#                 b * x + c * y)
#     (a, b, c) = (a * a + b * b,
#                  a * b + b * c,
#                  b * b + c * c)
#     n //= 2

#   return y