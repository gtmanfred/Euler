from sieve import sieve
def f(n):
    q = sieve(int(2 ** 0.5 * n))
    s = [False] * (n + 1)
    l = 0
 
    for p in q:
        if p < 7: continue
        a = (p + 1) // 2
        if legendre(a, p) == -1: continue
        z = sqrtmod(a, p)
        if z >= a: z = p - z
        for i in range(p - z, n + 1, p):
            if not s[i]:
                s[i] = True
                l += 1
        for i in range(p + z, n + 1, p):
            if not s[i]:
                s[i] = True
                l += 1
 
    return n - l - 1
 
print(f(50000000))