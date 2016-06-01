# Simple AKS Primality Test
"""
The AKS algorithm for testing whether a number is prime is a
polynomial-time test based on the following theorem:
"""
# clever method


# def aks_test(p):
#     coeff = 1
#     for i in xrange(p / 2):
#         coeff = coeff * (p - i) / (i + 1)
#         if coeff % p:
#             return False
#     return p > 1


def aks_test(p):
    if p == 1:
        return False
    c = p
    for i in range(2, p):
        if c % p != 0:
            return False
        c = c * (p - i + 1) / i
    return True


print aks_test(11)
print com(2, 10)
print com2(2, 10)
