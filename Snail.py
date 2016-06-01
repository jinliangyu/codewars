"""
Snail Sort

Given an n x n array, return the array elements arranged from
outermost elements to the middle element, traveling clockwise.

array = [[1,2,3],
         [4,5,6],
         [7,8,9]]
snail(array) #=> [1,2,3,6,9,8,7,4,5]
For better understanding, please follow the numbers of the next
array consecutively:

array = [[1,2,3],
         [8,9,4],
         [7,6,5]]
snail(array) #=> [1,2,3,4,5,6,7,8,9]
"""
# clever method


# def snail(array):
#     return list(array[0]) + snail(zip(*array[1:])[::-1]) if array else []


def snail(array):
    n = len(array)
    if n == 1:
        return array[0]
    if n == 0:
        return []
    res = []
    for j in range(n):
        res.append(array[0][j])
    for i in range(1, n):
        res.append(array[i][n - 1])
    for j in range(n - 1):
        res.append(array[n - 1][n - 2 - j])
    for i in range(n - 2):
        res.append(array[n - 2 - i][0])
    new_array = [a[1:-1] for a in array[1:-1]]
    new_res = snail(new_array)
    for k in range(len(new_res)):
        res.append(new_res[k])
    return res
    # test
array = [[1, 2, 3, 1],
         [4, 5, 6, 4],
         [7, 8, 9, 7],
         [7, 8, 9, 7]]

# array = [[1, 2, 3],
#          [4, 5, 6],
#          [7, 8, 9]]

print snail([[]])
