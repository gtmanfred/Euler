#from script import maths
#primes = maths.primesd(10**6)
from script.allsieve import soe
primes = dict.fromkeys(soe(10**6),1)

def Euler_37():
    ret = 0
    b = 0
    for x in primes.keys():
        if b ==0:print('start');b=1
        if primes.get(x) and int(x)>10:
            if primlandr(x):ret+=int(x)
    return ret
            
def primlandr(test):
    test = str(test)
    ret = True
    for i in range(1,len(test)):
        if primes.get(int(test[i:])):ret = True
        else: return False
        if primes.get(int(test[:-1-i+1])):ret = True
        else: return False
    return ret

if __name__=='__main__':
    print(Euler_37())
