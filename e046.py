from maths import primesd
from math import sqrt
primed = primesd(10**6)
nprime = [x for x in primed.keys() if primed.get(x) is 0 and x%2]
primes = [x for x in primed.keys() if primed.get(x) is 1]
def Euler_46():
    b = True
    t = False
    print('start')
    for check in nprime[2:]:
        for i in primes:
            if i>check:return check
            for j in range(1,(check-i)):
                if 2*j**2>(check-i+2):break
                if i+2*(j**2)==check:t = True;break
            if t:t = False;break
if __name__=='__main__':
    print(Euler_46())

