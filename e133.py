from sieve import sieve
def e133():
    L, q, s = 100000, pow(10, 20), 5
    for p in sieve(L)[1:]:
        if pow(10, q, p) != 1: s += p
    return s
if __name__=='__main__':
    print(e133())
