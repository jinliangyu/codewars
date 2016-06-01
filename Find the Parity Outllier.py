# Find  The Parity Outlier
"""
Description:

You are given an array (which will have a length of at least 3,
but could be very large) containing integers. The integers in the
array are either entirely odd or entirely even except for a single
integer N. Write a method that takes the array as an argument and returns N.

For example:

[2, 4, 0, 100, 4, 11, 2602, 36]

Should return: 11

[160, 3, 1719, 19, 11, 13, -21]

Should return: 160
"""


def odd(integers):
    res = []
    for i in integers:
        if i % 2 == 1:
            res.append(i)
    return res


def even(integers):
    res = []
    for i in integers:
        if i % 2 == 0:
            res.append(i)
    return res


def find_outlier(integers):
    oddnum = odd(integers)
    evennum = even(integers)

    if len(oddnum) == 1:
        return oddnum[0]
    else:
        return evennum[0]


# test
print find_outlier([2, 4, 0, 100, 4, 11, 2602, 36])  # 11
print find_outlier([160, 3, 1719, 19, 11, 13, -21])  # 160

# clever methiod 1
"""
def find_outlier(int):
    odds = [x for x in int if x%2!=0]
    evens= [x for x in int if x%2==0]
    return odds[0] if len(odds)<len(evens) else evens[0]

"""
# clever method 2
"""
def find_outlier(int):
    odds = [x for x in int if x%2!=0]
    evens= [x for x in int if x%2==0]
    return odds[0] if len(odds)<len(evens) else evens[0]
"""
