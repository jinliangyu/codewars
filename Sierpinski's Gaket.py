# Sierpinski's Gasket
"""
Write a function that takes an integer n and returns the nth iteration of the
fractal known as Sierpinski's Gasket.

Here are the first few iterations. The fractal is composed entirely of L and
white-space characters; each character has one space between it and the next
(or a newline).
"""


def sierpinski(n):
    if n == 0:
        return 'L'
    # elif n == 1:
    #     return 'L\nL L'
    else:
        x = sierpinski(n - 1)
        m = 2**(n - 1)
        s = x + '\n'
        y = x.split('\n')
        for i in range(m):
            # s += y[i] + ' ' * (2 * m - 1 - 2 * i) + y[i]
            s += y[i].ljust(2**n) + y[i]
            if i != m - 1:
                s += '\n'
        return s
        # return sierpinski(n - 1) + '\n' + "\n".join(
        #     [sierpinski(n - 1).split('\n')[i].ljust(2**n) +
        #      sierpinski(n - 1).split('\n')[i] for i in
        #      range(2**(n - 1))])


# test

print sierpinski(0)
print "==============="
print sierpinski(1)
print "==============="
print sierpinski(2)
print "==============="
print sierpinski(3)

# clever method
"""
def sierpinskiRows(n):
  if not n:
    return [ 'L' ]
  last = sierpinskiRows(n - 1)
  return last + [ row.ljust(2 ** n) + row for row in last ]

def sierpinski(n):
  return '\n'.join(sierpinskiRows(n))
"""
# clever method 2
"""
def sierpinski(n):
    r = ['L']
    for i in range(n):
        l = len(r)
        for j in range(l):
            r.append(r[j].ljust(l * 2) + r[j])
    return '\n'.join(r)
"""

# My method for short
"""
def sierpinski(n):
    if n == 0:
        return 'L'

    else:
        return sierpinski(n - 1) + '\n' + "\n".join(
            [sierpinski(n - 1).split('\n')[i].ljust(2**n) +
             sierpinski(n - 1).split('\n')[i] for i in
             range(2**(n - 1))])
"""
