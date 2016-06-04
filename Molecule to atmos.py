# Molecule to atoms
"""
For a given chemical formula represented by a string, count the number of atoms
of each element contained in the molecule and return an object.

For example:

water = 'H2O'
parse_molecule(water)                 # return {H: 2, O: 1}

magnesium_hydroxide = 'Mg(OH)2'
parse_molecule(magnesium_hydroxide)   # return {Mg: 1, O: 2, H: 2}

var fremy_salt = 'K4[ON(SO3)2]2'
parse_molecule(fremySalt)             # return {K: 4, O: 14, N: 2, S: 4}
As you can see, some formulas have brackets in them. The index outside the
brackets tells you that you have to multiply count of each atom inside the
bracket on this index. For example, in Fe(NO3)2 you have one iron atom, two
nitrogen atoms and six oxygen atoms.
"""

import re
groupnumber = re.compile(r'(.*)(\[.*\]|\(.*\)|\{.*\})(\d+)(.*)')
pattern = re.compile(r'([A-Z][a-z]{0,2})(\d+|)')


def mutipleItem(formula, count):
    l = []
    atoms = pattern.findall(formula)
    for i in range(len(atoms)):
        l.append(atoms[i][0])
        if atoms[i][1] == '':
            l.append(str(count))
        else:
            l.append(str(int(atoms[i][1]) * count))
    return ''.join(l)


def parse_molecule(formula):
    g = groupnumber.match(formula)
    if g is not None:
        return parse_molecule(g.group(1) +
                              mutipleItem(g.group(2), int(g.group(3))) +
                              g.group(4))
    else:
        d = dict()
        for e in pattern.findall(formula):
            if e[0] in d:
                if e[1] != '':
                    d[e[0]] += int(e[1])
                else:
                    d[e[0]] += 1
            else:
                if e[1] != '':
                    d[e[0]] = int(e[1])
                else:
                    d[e[0]] = 1
        return d

# clever method 1
"""
from collections import Counter
import re

COMPONENT_RE = (
    r'('
        r'[A-Z][a-z]?'
        r'|'
        r'\([^(]+\)'
        r'|'
        r'\[[^[]+\]'
        r'|'
        r'\{[^}]+\}'
    r')'
    r'(\d*)'
)


def parse_molecule(formula):
    counts = Counter()
    for element, count in re.findall(COMPONENT_RE, formula):
        count = int(count) if count else 1
        if element[0] in '([{':
            for k, v in parse_molecule(element[1:-1]).items():
                counts[k] += count * v
        else:
            counts[element] += count
    return counts
"""
# test
print parse_molecule('M4K3O2Mg4')
print parse_molecule('Mg(OH)2')
print parse_molecule('K4[ON(SO3)2]2')
