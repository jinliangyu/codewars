# Number of trailing zeros of N!
"""
Write a program that will calculate the number of trailing
zeros in a factorial of a given number.

N! = 1 * 2 * 3 * 4 ... N

zeros(12) = 2 # 1 * 2 * 3 .. 12 = 479001600
that has 2 trailing zeros 4790016(00)
Be careful 1000! has length of 2568 digital numbers.
"""

'''
def zeros(n):
    count = n
    j = 10
    for i in range(2, 11):
        if j % i == 0:
            p = 0
            while j % i == 0:
                p += 1
                j /= i
            c = 0
            k = n
            while k / i > 0:
                c += k / i
                k /= i
            count = min(count, c / p)
    return count
'''

# cleverest method


def zeros(n):
    count = 0
    i = 1
    while 5**i <= n:
        count = count + n / 5**i
        i += 1
    return count

print zeros(100)
# 
# def zeros(n):
#   x = n/5
#   return x+zeros(x) if x else 0
