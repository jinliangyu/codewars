# Pick peaks
"""
In this kata, you will create an object that returns the positions and the
values of the "peaks" (or local maxima) of a numeric array.

For example, the array arr = [ 0 , 1 , 2 , 5 , 1 , 0 ] has a peak in
position 3 with a value of 5 (arr[3] = 5)

The output will be returned as an object with two properties: pos and peaks.
Both of these properties should be arrays. If there is no peak in the given
array, then the output should be {pos: [], peaks: []}.

Example: pickPeaks([3,2,3,6,4,1,2,3,2,1,2,3]) returns {pos:[3,7],peaks:[6,3]}

All input arrays will be valid numeric arrays (although it could still be
empty), so you won't need to validate the input.

The first and last elements of the array will not be considered as peaks
(in the context of a mathematical function, we don't know what is after and
before and therefore, we don't know if it is a peak or not).
"""


def pick_peaks(arr):
    pos = []
    peaks = []

    up = False
    down = False
    found = False
    k = 0
    for i in range(1, len(arr)):
        if arr[i] >arr[i - 1]:
            up = True
            k = i
        if up and arr[i] < arr[i - 1]:
            down = True
        if up and down:
            found = True
        if found:
            up = False
            down =  False
            found = False
            pos.append(k)
            peaks.append(arr[k])

        
    return dict(pos=pos, peaks=peaks)


# clever method
"""
def pick_peaks(arr):
    pos = []
    prob_peak = False
    for i in range(1, len(arr)):
        if arr[i] > arr[i-1]:
            prob_peak = i
        elif arr[i] < arr[i-1] and prob_peak:
            pos.append(prob_peak)
            prob_peak = False
    return {'pos':pos, 'peaks':[arr[i] for i in pos]}
"""

print pick_peaks([3, 2, 3, 6, 4, 1, 2, 3, 2, 1, 2, 2, 2, 1])
print pick_peaks([2, 1, 3, 1, 2, 2, 2, 2])
