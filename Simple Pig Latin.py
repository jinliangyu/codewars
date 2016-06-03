# Simple Pig Latin
"""
Move the first letter of each word to the end of it, then add 'ay' to the end
of the word.

pig_it('Pig latin is cool') # igPay atinlay siay oolcay
"""


def pig_it(text):
    text = text.split()
    new_text = []
    for word in text:
        if word.isalpha():
            new_text.append(word[1:] + word[0] + 'ay')
        else:
            new_text.append(word)
    return " ".join(new_text)


# clever method
"""
def pig_it(text):
    lst = text.split()
    return ' '.join( [word[1:] + word[:1] + 'ay' if word.isalpha() else word \
        for word in lst])
"""
# test
print pig_it('Pig latin is cool')
