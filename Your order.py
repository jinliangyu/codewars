def order(sentence):
    # code here
    senlist = sentence.split()
    res = {}
    for w in senlist:
        for i in w:
            if i.isdigit():
                res[int(i)] = w
    reslist = []
    for i, k in res.items():
        reslist.append(k)
    print reslist
    return " ".join(reslist)

# clever method
"""
def order(sentence):
    return " ".join(sorted(sentence.split(), key=lambda \
    x: int(filter(str.isdigit, x))))
"""
# clever method
"""
def order(words):
  return ' '.join(sorted(words.split(), key=lambda w:sorted(w)))
"""


print order("is2 Thi1s T4est 3a")
