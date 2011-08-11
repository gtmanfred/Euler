from script.math2 import binomial_coefficient, count_permutations


def combinations_with_limit(a, b, limit):
    c = [b] * a
    n = len(c)
    s = sum(c)
    while 1:
        yield tuple(c)
        if s < limit:
            c[-1] += 1
            s += 1
        elif n == 1:
            return
        else:
            i = n - 1
            k = 1
            while i >= 0:
                s -= k * c[i]
                i -= 1
                c[i] += 1
                s += k * c[i] + 1
                k += 1
                if s <= limit:
                    break
            if i == -1:
                return
            else:
                for j in range(i + 1, n):
                    c[j] = c[i]


def f(m, n):
    num_ways = 1
    for b in range(1, (n + 1) // (m + 1) + 1):
        lim = n - b + 1
        for c in combinations_with_limit(b, m, lim):
            p = n - sum(c) + 1
            num_ways += binomial_coefficient(p, b) * count_permutations(c)
    return num_ways
