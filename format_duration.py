# Human readable duration format
"""
Your task in order to complete this Kata is to write a function which formats
a duration, given as a number of seconds, in a human-friendly way.

The function must accept a non-negative integer. If it is zero, it just
returns "now". Otherwise, the duration is expressed as a combination of
years, days, hours, minutes and seconds.

It is much easier to understand with an example:

  format_duration(62)    # returns "1 minute and 2 seconds"
  format_duration(3662)  # returns "1 hour, 1 minute and 2 seconds"
Note that spaces are important.

Detailed rules

The resulting expression is made of components like 4 seconds, 1 year, etc.
In general, a positive integer and one of the valid units of time, separated
by a space. The unit of time is used in plural if the integer is greater than
1.

The components are separated by a comma and a space (", "). Except the last
component, which is separated by " and ", just like it would be written in
English.

A more significant units of time will occur before than a least significant
one. Therefore, 1 second and 1 year is not correct, but 1 year and 1 second is.

Different components have different unit of times. So there is not repeated
units like in 5 seconds and 1 second.

A component will not appear at all if its value happens to be zero. Hence, 1
minute and 0 seconds is not valid, but it should be just 1 minute.

A unit of time must be used "as much as possible". It means that the function
should not return 61 seconds, but 1 minute and 1 second instead. Formally,
the duration specified by of a component must not be greater than any valid
more significant unit of time.

For the purpose of this Kata, a year is 365 days and a day is 24 hours.
"""


def format_duration(seconds):
    if seconds == 0:
        return 'now'
    res1 = []

    k = [60, 60, 24, 365]
    v = ['years', 'days', 'hours', 'minutes', 'seconds']

    for i in k:
        res1.append(seconds % i)
        seconds /= i
    res1.append(seconds)
    res1.reverse()
    res2 = []
    for i in range(len(res1)):
        if res1[i] == 0:
            pass
        elif res1[i] == 1:
            res2.append(str(res1[i]) + ' ' + v[i][:-1])
        else:
            res2.append(str(res1[i]) + ' ' + v[i])
    if len(res2) == 1:
        return res2[0]
    else:
        res = ', '.join(res2[:-1])
        res += ' and ' + res2[-1]
        return res

# test
print format_duration(3662)


# clever method

"""
times = [("year", 365 * 24 * 60 * 60), 
         ("day", 24 * 60 * 60),
         ("hour", 60 * 60),
         ("minute", 60),
         ("second", 1)]

def format_duration(seconds):

    if not seconds:
        return "now"

    chunks = []
    for name, secs in times:
        qty = seconds // secs
        if qty:
            if qty > 1:
                name += "s"
            chunks.append(str(qty) + " " + name)

        seconds = seconds % secs

    return ', '.join(chunks[:-1]) + ' and ' + chunks[-1] \
    if len(chunks) > 1 else chunks[0]
"""


# RE
"""
import re
def format_duration(seconds):
    if not seconds: return 'now'
    minutes = seconds / 60
    seconds %= 60
    hours = minutes / 60
    minutes %= 60
    days = hours / 24
    hours %= 24
    years = days / 365
    days %= 365
    a = []
    for n, l in zip([years, days, hours, minutes, seconds],\
    ['year', 'day', 'hour', 'minute', 'second']):
        if n == 1:
            a.append('%d %s' % (n, l))
        elif n > 1:
            a.append('%d %ss' % (n, l))
    return re.sub(r', ([^,]*)$', lambda o: ' and ' + o.group(1), ', '.join(a))
"""
