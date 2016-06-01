# Is a number prime?
"""
Is Prime

Define a function isPrime that takes one integer argument
and returns true or false depending on if the integer is
a prime.

Per Wikipedia, a prime number (or a prime) is a natural
number greater than 1 that has no positive divisors other
than 1 and itself.

Example

isPrime(5)
=> true
"""


def is_prime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True and n > 1

# test
print is_prime(5)

# clever method
# def is_prime(num):
#     return num > 1 and not any(num % n == 0 for n in range(2,num))
