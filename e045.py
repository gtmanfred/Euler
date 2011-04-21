'''
Triangle, pentagonal, and hexagonal numbers are generated by the following
formulae:

    Triangle        Tn=n(n+1)/2     1, 3, 6, 10, 15, ...
    Pentagonal      Pn=n(3n1)/2     1, 5, 12, 22, 35, ...
    Hexagonal       Hn=n(2n1)       1, 6, 15, 28, 45, ...
    It can be verified that T285 = P165 = H143 = 40755.

    Find the next triangle number that is also pentagonal and hexagonal.
'''
import maths
n = 100000
n2 = 100001
alist = list(x for x in range(n2))

tnums = list((i*(i+1))//2 for i in range(286,n2))
pnums = list((i*(3*i-1))//2 for i in range(100,n2))
hnums = list((i*(2*i-1)) for i in range(100,n2))


pendict = dict.fromkeys(pnums,1)

hexdict = dict.fromkeys(hnums,1)

def Euler_45():
    for t in tnums:
        if pendict.get(t) and hexdict.get(t):
            return t


if __name__=='__main__':
    print(Euler_45())