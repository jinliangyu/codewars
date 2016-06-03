# find the divisors
def divisors(integer):
    res = []
    for i in range(2, int(integer * 0.5) + 1):
        if integer % i == 0:
            res.append(i)
    if res == []:
        return str(integer) + ' is prime'
    else:
        return res


# clever method
"""
def divisors(num):
    l = [a for a in range(2,num) if num%a == 0]
    if len(l) == 0:
        return str(num) + " is prime"
    return l
"""
# test
print divisors(12)
