"""
Nesting Structure Comparison
"""
"""
Description:

Complete the method (or function in Python) to return true when its argument is an array that has the same nesting structure as the first array.

For example:

# should return True
same_structure_as([ 1, 1, 1 ], [ 2, 2, 2 ] )
same_structure_as([ 1, [ 1, 1 ] ], [ 2, [ 2, 2 ] ] )

# should return False 
same_structure_as([ 1, [ 1, 1 ] ], [ [ 2, 2 ], 2 ] )
same_structure_as([ 1, [ 1, 1 ] ], [ [ 2 ], 2 ] )

# should return True
same_structure_as([ [ [ ], [ ] ] ], [ [ [ ], [ ] ] ] )

# should return False
same_structure_as([ [ [ ], [ ] ] ], [ [ 1, 1 ] ] )
"""
# Clever method


def same_structure_as(a, b):
    return (False if not (isinstance(a, list) and isinstance(b, list)) or len(a) != len(b)
            else all(same_structure_as(c, d) for c, d in zip(a, b) if isinstance(c, list)))

# My method

"""
def same_structure_as(original, other):
    struct1 = check(original, "")
    struct2 = check(other, "")
    return struct1 == struct2


def check(arr, current):
    if type(arr) == list:
        current += '['
        for a in arr:
            if type(a) == list:
                current += check(a, "")
            else:
                current += '*'
        current += ']'
    return current
"""

# should return True
print same_structure_as([1, 1, 1], [2, 2, 2])
print same_structure_as([1, [1, 1]], [2, [2, 2]])

# should return False
print same_structure_as([1, [1, 1]], [[2, 2], 2])
print same_structure_as([1, [1, 1]], [[2], 2])

# should return True
print same_structure_as([[[], []]], [[[], []]])

# should return False
print same_structure_as([[[], []]], [[1, 1]])
