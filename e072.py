from fractions import Fraction
def Euler_72(L = 10**6):
    phi = list(range(L+1))
    for n in range(2, L+1):
        if phi[n] == n:
            for k in range(n, L+1, n):
                phi[k] *= (n - 1)/n;
    return int(sum(phi)-1)
                         
'''
    count = set()
    for d in range(1,den+1):
        for n in range(1,d):
            frac = Fraction(n,d)
            count.add(frac)
    return len(count)
'''
if __name__=='__main__':
    print(Euler_72())
