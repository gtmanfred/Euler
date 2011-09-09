from script.maths import primesd
from script.allsieve import soe
from math import sqrt
primes = soe(10**6)
pd = dict.fromkeys(primes,1)
nprime = [x for x in range(1,10**6,2) if not pd.get(x)] 
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

