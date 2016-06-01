def recoverSecret(triplets):
    elements = {}
    for row in triplets:
        for i in range(len(row)):
            if row[i] not in elements:
                elements[row[i]] = 1
    for row in triplets:
        for i in range(len(row)-1, 0, -1):
            elements[row[i-1]] += (elements[row[i]])

    print elements

    # test case
secret = "whatisup"
triplets = [
    ['t', 'u', 'p'],
    ['w', 'h', 'i'],
    ['t', 's', 'u'],
    ['a', 't', 's'],
    ['h', 'a', 'p'],
    ['t', 'i', 's'],
    ['w', 'h', 's']
]

recoverSecret(triplets)
