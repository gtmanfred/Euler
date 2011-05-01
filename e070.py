from primes import Primes
from maths import primetree
p = Primes(10**7)
twos = [2**i for i in range(1000) if 2**i<10**7]
print('start')
def phi(num):
    if p.isPrime(num):return num-1
    elif num in twos:return num//2
    else: 
        x = primetree(num)
        ret = [1 for j in range(1,num)]
        for i in x:
            ite = i
            while i < num:
                ret[i] = 0
                i+=ite
        return sum(ret)


def Euler_70():
    print('start')
    n = 0
    maxp = 10**7
    for i in range(10,10**7):
        if i%1000==0:print(i//1000)
        phi1 = phi(i)
        phis = str(phi1)
        stri = str(i)
        iphi = i/phi1
        if sorted(phis)==sorted(stri) and len(set(stri)) ==len(stri) and iphi<maxp:
            ret = i
            maxp = iphi
            print('i:',i,'phi:',phi1,'i/phi:',iphi)
    return ret
if __name__=='__main__':
    print(Euler_70())
