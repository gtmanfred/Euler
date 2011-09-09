#! /usr/bin/env python3
# Solution to http://projecteuler.net/?section=problems&id=51
from script.maths import nextprime
from script.math2 import digits, digits_to_number
from script.isprime import isprime 


def solve():
    p = 1
    while True:
        p = nextprime(p)
        digs = digits(p)
        numdigs = len(digs)
        uniquedigs = list(set(digs))
        uniquedigs.sort()
        indexes = [None] * 10
        for i in range(numdigs):
            d = digs[i]
            if indexes[d] is None:
                indexes[d] = []
            indexes[d].append(i)
        for d in uniquedigs:
            # The first member of a family have recurring digits,
            # each of which is one of 0, 1, and 2.
            if d > 2:
                continue
            inds = indexes[d]
            # If the number of recurring digits is not a multiple of 3 or
            # one of the digits is the least significant, then the family
            # can't have 8 members.
            if len(inds) % 3 == 0 and inds[-1] != numdigs - 1:
                start = 1 if inds[0] == 0 else 0
                numgenerated = 10 - start
                numprimes = 0
                numcomposites = 0
                # Generate family candidates
                for e in range(start, 10):
                    for i in inds:
                        digs[i] = e
                    number = digits_to_number(digs)
                    if isprime(number):
                        numprimes += 1
                    else:
                        numcomposites += 1
                    if numcomposites > numgenerated - 8:
                        break
                if numprimes == 8:
                    return p

print(solve())
