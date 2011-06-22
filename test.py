from itertools import *
 
def div_pow(n, d):
    while n % d == 0:
        n /= d
    return n
 
def sieve(N):
    a = range(N + 2)
    b = [ 1 ] * (N + 2)
    for p in ifilter(lambda m: a[m] == m,
                takewhile(lambda m: m * m < N + 2, count(2))):
        for n in xrange(p * 2, N + 2, p):
            a[n] = div_pow(a[n], p)
            b[n] = p
 
    for n in xrange(2, N + 2):
        if a[n] != 1:
            b[n] = a[n]
    return b
 
def sieve2(N):
    a = [ n * n - n + 1 for n in xrange(N + 1) ]
    b = [ 1 ] * (N + 1)
    for m in ifilter(lambda m: a[m] != 1, xrange(2, N + 1)):
        p = a[m]
        if p > N:
            continue
        d = (p - m * 2 + 1) % p
        for n in xrange(m + p, N + 1, p):
            a[n] = div_pow(a[n], p)
            b[n] = max(b[n], p)
 
        for n in xrange(m + d, N + 1, p):
            a[n] = div_pow(a[n], p)
            b[n] = max(b[n], p)
 
    for n in xrange(2, N + 1):
        if a[n] != 1:
            b[n] = max(b[n], a[n])
    return b
 
def F(n):
    return max(max_factor(n + 1), max_factor(n * n - n + 1)) - 1
 
#N = 10 ** 6 * 2
#a = sieve(N)
#b = sieve2(N)
#print sum(max(a[n+1], b[n]) for n in xrange(1, N + 1)) - N