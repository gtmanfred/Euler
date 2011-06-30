from fractions import gcd
from functools import reduce
from math import factorial, modf, sqrt
from operator import mul


def product(iterable):
    return reduce(mul, iterable, 1)


def digits(n, base=10):
    """Return a list of digits of n in base b notation.

    digits(1437[, 10]) --> [1, 4, 3, 7]
    digits(0xf7, 16) --> [15, 7]
    """
    lst = rdigits(n, base)
    lst.reverse()
    return lst


def rdigits(n, base=10):
    """Return a list of digits of n in base b notation in reversed order.
    If the order of digits does not matter, use this instead of digits()
    for better performance.

    rdigits(1437[, 10]) --> [7, 3, 4, 1]
    rdigits(0367, 8) --> [7, 6, 3]
    """
    lst = []
    if n == 0:
        lst.append(0)
    while n:
        n, d = divmod(n, base)
        lst.append(d)
    return lst


def digits_to_number(iterable, base=10):
    n = 0
    for d in iterable:
        n *= base
        n += d
    return n


def is_square(n):
    return modf(sqrt(n))[0] == 0


def is_pentagonal(n):
    return modf((1 + sqrt(1 + 24 * n)) / 6)[0] == 0


def is_hexagonal(n):
    return modf((1 + sqrt(1 + 8 * n)) / 4)[0] == 0


def continued_fraction(n):
    "Return the continued fraction of the positive square root of n."
    r = sqrt(n)
    a0 = int(r)
    cycle = []
    if a0 < r:
        a = a0
        b = 1
        # remainder = (sqrt(n) - a) / b
        while b != 1 or not cycle:
            b = (n - a ** 2) // b
            x = int((r + a) // b)
            cycle.append(x)
            a = x * b - a
    return (a0, tuple(cycle))


def generate_convergents(a0, iterator):
    n1, n0 = 1, a0
    d1, d0 = 0, 1
    for x in iterator:
        yield (n0, d0)
        n1, n0 = n0, x * n0 + n1
        d1, d0 = d0, x * d0 + d1


def binomial_coefficient(n, k):
    return factorial(n) // factorial(k) // factorial(n - k)


def multinomial_coefficient(n, ks):
    "Precondition: sum(ks) == n (not checked in this function)"
    c = factorial(n)
    for k in ks:
        c //= factorial(k)
    return c


def count_permutations(iterable):
    """Return the number of permutations of the sequence. The sequence
    must be sorted so that equal elements are not seperated by other
    elements in the sequence.

    The result of this function with a sequence can be also obtained by
    counting equal elements in the sequence and using
    multinomial_coefficient().

    count_permutations([0, 1, 2, 3, 4]) --> 120
    count_permutations([1, 2, 2, 3, 3]) --> 30
    """
    n = 1
    m = 1
    last_item = None
    for k, item in enumerate(iterable, 1):
        n *= k
        if item != last_item:
            m = 1
        else:
            m += 1
            n //= m
        last_item = item
    return n


def solve_linear_congruence(a, c, m):
    c = c % m
    d = gcd(a, c)
    e = gcd(d, m)
    if e > 1:
        a //= e
        c //= e
        m //= e
        d //= e
    if d > 1:
        a //= d
        c //= d
    ai = inverse_mod(a, m)
    return ((ai * c) % m, m) if ai is not None else None


def inverse_mod(a, m):
    y2 = 0
    y1 = 1
    n = m
    while a:
        q, r = divmod(n, a)
        y = y2 - q * y1
        y2 = y1
        y1 = y
        n = a
        a = r
    return y2 % m if n == 1 else None
