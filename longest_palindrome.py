# -*- coding:utf-8 -*-
# longest_palindrome
"""
Longest Palindrome

Find the length of the longest substring in the given string s that is the
same in reverse.

As an example, if the input was “I like racecars that go fast”, the
substring (racecar) length would be 7.

If the length of the input string is 0, return value must be 0.

Example:

"a" -> 1
"aab" -> 2
"abcde" -> 1
"zzbaabcd" -> 4
"" -> 0
"""


def longest_palindrome(s):
    p = [0] * 100
    mx = 0
    idx = 0
    for i in range(len(s)):
        if mx > i:
            p[i] = min(p[2 * idx - i], mx - i)
        else:
            p[i] = 1
        while (s[i + p[i]] == s[i - p[i]]):
            p[i] += 1
        if i + p[i] > mx:
            mx = i + p[i]
            idx = i
    return max(p)

# test

print longest_palindrome('zzbaabcd')
