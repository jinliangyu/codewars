"""
Create a function taking a positive integer as its parameter and returning a
string containing the Roman Numeral representation of that integer.

Modern Roman numerals are written by expressing each digit separately starting
with the left most digit and skipping any digit with a value of zero. In Roman
numerals 1990 is rendered: 1000=M, 900=CM, 90=XC; resulting in MCMXC. 2008 i
written as 2000=MM, 8=VIII; or MMVIII. 1666 uses each Roman symbol in
descending order: MDCLXVI.
"""


# clever method
"""
def solution(n):
    roman_numerals = {1000:'M',
                      900: 'CM',
                      500: 'D',
                      400: 'CD',
                      100: 'C',
                      90: 'XC',
                      50: 'L',
                      40: 'XL',
                      10: 'X',
                      9: 'IX',
                      5: 'V',
                      4: 'IV',
                      1: 'I'
    }
    roman_string = ''
    for key in sorted(roman_numerals.keys(),reverse=True):
        while n >= key:
            roman_string += roman_numerals[key]
            n -= key
    return roman_string
"""


# clever method 2
"""
vals = zip(('M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I'),
           (1000, 900, 500,  400, 100,   90,  50,   40,  10,    9,   5,    4,   1))

def solution(n):
    if n == 0: return ""
    return next(c + solution(n-v) for c,v in vals if v <= n)
"""


def solution(Num):
    if Num < 1 or Num > 3999:
        print 'The Num must in 1-3999'
    else:
        NumDic = {
            '1': ('I', 'IV', 'V', 'IX'),
            '2': ('X', 'XL', 'L', 'XC'),
            '3': ('C', 'CD', 'D', 'CM'),
            '4': ('M')
        }
        items = sorted(NumDic.items())
        retstr = ''
        for item in items:
            str = ''
            (Num, modNum) = divmod(Num, 10)
            if modNum != 0:
                if item[0] != '4':
                    if modNum <= 3:
                        while modNum > 0:
                            str = str.join(['', item[1][0]])
                            modNum -= 1
                    elif modNum < 5:
                        str = item[1][1]
                    elif modNum == 5:
                        str = item[1][2]
                    elif modNum < 9:
                        str = item[1][2]
                        while modNum > 5:
                            str = str.join(['', item[1][0]])
                            modNum -= 1
                    else:
                        str = item[1][3]
                else:
                    while modNum > 0:
                        str = str.join(['', item[1][0]])
                        modNum -= 1
                retstr = str.join(['', retstr])
        return retstr


# test

print solution(4)
