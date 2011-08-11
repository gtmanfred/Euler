#! /usr/bin/env python3
# Solution to http://projecteuler.net/?section=problems&id=118
from itertools import permutations
from isprime import isprime as is_prime

def generate_digit_partitions(n):
    groups = [0] * n
    counter = [0] * n
    counter[0] = n
    nearest = 0
    while True:
        yield digit_partition(groups)
        if nearest == n:
            break
        g = groups[nearest]
        groups[nearest] += 1
        counter[g] -= 1
        counter[g + 1] += 1
        i = 0
        while i < nearest:
            g = groups[i]
            groups[i] = 0
            counter[g] -= 1
            counter[0] += 1
            i += 1
        i = 0
        while i < n:
            if counter[groups[i]] >= 2:
                break
            i += 1
        nearest = i

def digit_partition(groups):
    temp = {}
    for d, g in enumerate(groups, 1):
        temp.setdefault(g, []).append(str(d))
    return (''.join(x) for x in temp.values())

def primes_w_specific_digits(digits):
    if sum(int(d) for d in digits) % 3 == 0:
        primes = {3} if digits == '3' else set()
    else:
        numbers = (int(''.join(p)) for p in permutations(digits))
        primes = {p for p in numbers if is_prime(p)}
    return primes

def e118():
    dprimes_by_digits = {}
    count = 0
    for partition in generate_digit_partitions(9):
        subcount = 1
        for s in partition:
            if s not in dprimes_by_digits:
                dprimes_by_digits[s] = primes_w_specific_digits(s)
            subcount *= len(dprimes_by_digits[s])
            if subcount == 0:
                break
        count += subcount
    return count
if __name__=='__main__':
    print(e118())
