# Secret knock
"""
Description:

Perform the secret knock() to enter...
"""

import inspect
import dis

# what am i dealing with?
print 'knock is function?', inspect.isfunction(knock)
# (could have been a class or something else callable) but no,
# it is a function

# try to get some hints about what it does even though i
# will only understand a fraction of it
dis.dis(knock)

# there's a string in there, let's try that as an argument,
# do i get anything back?
print 'type of returned value:', type(knock('"Knock knock"'))
# why doesn't that print anything?
# has that name been hidden?
from __builtin__ import type
print 'type of returned value:', type(knock('"Knock knock"'))
# still nothing, no idea why i'm getting nothing printed from this

# but this will let me know if something interesting comes back
print knock('"Knock knock."') is None
# nope, no return value

# any hints in its parameters?
print 'parameters:', inspect.getargspec(knock)
# just a single parameter called args, not much to go by

# let's look at the byte code again
# ..it says:
#   30 39 LOAD_FAST 0 (arg)
#   42 LOAD_GLOBAL 0 (knock)
#   45 COMPARE_OP 2 (==)
# i know the arg is the argument from inspect.getargspec(knock),
# and i believe that knock is the function itself
# so let's try:
res = knock(knock)
print 'knock(res) is None:', knock(res) is None
# bingo, something was returned

# what though? what can i do with it?
print 'dir(res):', dir(res)
# it has a __call__ attribute, so call it:
resres = res()
print 'dir(resres):', dir(resres)
# another __call__ attribute
resres()
# apparently that was it
print '### STOP ###'
