def isPrime(x):
    # if x <= 1:
    #     return False
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            return False

    return True

P = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47]

def getPrimes(x):
    return [i for i in range(2, int(x * 0.5) + 1) if isPrime(i) and x % i == 0]


def getAllPrimeFactors2(n):
    i = 2
    res = []
    while n > 1:
        if n % i == 0:
            n /= i
            res.append(i)
        else:
            i += 1
            while not (i in P and n % i == 0):
                i += 1
        print n
    return res


def getAllPrimeFactors(n):
    if not isinstance(n, (int, long)) or n <= 0:
        return []
    elif n == 1:
        return [1]
    elif n == 2:
        return [2]
    res = []
    primes = getPrimes(n)
    i = 0
    while n > 1:
        if n % primes[i] == 0:
            n /= primes[i]
            res.append(primes[i])
        else:
            i += 1
    return res


def getUniquePrimeFactorsWithCount(n):
    if not isinstance(n, (int, long)) or n <= 0:
        return [[], []]
    elif n == 1:
        return [[1], [1]]
    elif n == 2:
        return [[2], [1]]
    # res = []
    # allprimes = getAllPrimeFactors(n)
    # primes = getPrimes(n)
    # res.append(primes)
    # count = []
    # for i in primes:
    #     count.append(allprimes.count(i))
    # res.append(count)
    return [getPrimes(n), [getAllPrimeFactors(n).count(i) for i in
                           getPrimes(n)]]


def getUniquePrimeFactorsWithProducts(n):
    if not isinstance(n, (int, long)) or n <= 0:
        return []
    elif n == 1:
        return [1]
    elif n == 2:
        return [2]
    primescount = getUniquePrimeFactorsWithCount(n)
    return [primescount[0][i]**primescount[1][i] for i in
            range(len(primescount[0]))]
    # test
print isPrime(11)
print getPrimes(10)
print getAllPrimeFactors2(100)
print getUniquePrimeFactorsWithCount(100)
print getUniquePrimeFactorsWithProducts(100)


#　Clever method 1
import math
import collections

def getAllPrimeFactors(n):
  numberToDecompose = n
  if (not isinstance(numberToDecompose,(int,long)) or numberToDecompose<=0):    return []
  answer = ([1] if (numberToDecompose==1) else  [])
  for possibleFactor in range (2,numberToDecompose+1):
      while (numberToDecompose % possibleFactor == 0):
         answer.extend([possibleFactor])
         numberToDecompose = numberToDecompose / possibleFactor
  answer = sorted(answer)
  return answer


def getUniquePrimeFactorsWithProducts(n):
  ch= getUniquePrimeFactorsWithCount(n)
  x= [a**b for (a,b) in zip (ch[0], ch[1])]
  return x
  
def getUniquePrimeFactorsWithCount(n):
    c = collections.Counter (getAllPrimeFactors(n))
    d=  [a for  (a,_) in c.items()]
    e = [b for  (_,b) in c.items()]
    return [d,e]

#　Clever method 2
def getAllPrimeFactors(n):
    output = []
    i = 2
    if n < 1 or type(n) != type(0):
        return []
    if n < 3:
        return {1: [1], 2: [2]}[n]
    while i < n:
        if n % i == 0:
            output.append(i)
            n = n / i
        else:
            i += 1
    output.append(n)
    return output

def getUniquePrimeFactorsWithCount(n):
    myDict = {}
    output = []
    i = 2
    if n < 1 or type(n) != type(0):
        return [[], []]
    if n < 3:
        return {1: [[1], [1]], 2: [[2], [1]]}[n]
    while i < n:
        if n % i == 0:
            if i not in myDict:
                output.append(i)
                myDict[i] = 1
                n = n / i
            else:
                myDict[i] += 1
                n = n / i
        else:
            i += 1
    if n not in myDict:
        output.append(n)
        myDict[n] = 1
    else:
        myDict[n] += 1
    return [output, [myDict[i] for i in output]]

def getUniquePrimeFactorsWithProducts(n):
    myDict = {}
    output = []
    i = 2
    if n < 1 or type(n) != type(0):
        return []
    if n < 3:
        return {1: [1], 2: [2]}[n]
    while i < n:
        if n % i == 0:
            if i not in myDict:
                output.append(i)
                myDict[i] = 1
                n = n / i
            else:
                myDict[i] += 1
                n = n / i
        else:
            i += 1
    if n not in myDict:
        output.append(n)
        myDict[n] = 1
    else:
        myDict[n] += 1
    return [i**myDict[i] for i in output]

# Clever method 3
from math import sqrt, floor
from collections import Counter

def positive_integer(default=None):
    def _decorator(func):
        def _wrapper(n):
            if not isinstance(n, int) or n <= 0:
                return default
            return func(n)
        return _wrapper
    return _decorator

@positive_integer(default=[])
def getAllPrimeFactors(n): 
    return sorted(get_factors(n))

@positive_integer(default=[[], []])
def getUniquePrimeFactorsWithCount(n):
    factors = getAllPrimeFactors(n)
    c = zip(*sorted(Counter(factors).items(), key=lambda x: x[0]))
    return [list(tup) for tup in c]
    

@positive_integer(default=[])
def getUniquePrimeFactorsWithProducts(n):
    factors = getUniquePrimeFactorsWithCount(n)
    return [tup[0]**tup[1] for tup in zip(*factors)]
    

    
def get_factors(n):
    def _get_factor(n):
        for i in xrange(2, 1 + int(floor(sqrt(n)))):
            if n % i == 0:
                return i
        return n
    
    prime_factors = []
    factor = _get_factor(n)
    if factor == n: return [factor]
    factors = [factor, n / factor]
    while factors:
        factor = factors.pop()
        new_factor = _get_factor(factor)
        if new_factor == factor: prime_factors.append(factor)
        else: factors.extend([new_factor, factor / new_factor])
    return prime_factors