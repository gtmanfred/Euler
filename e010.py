from script import maths 
from script.allsieve import primesfrom2to as p,soe as sieve

def e010(top=2*10**6):
    return sum(sieve(top))

def Euler_10(top = 2*10**6):
    
    return sum(maths.primesd3(top))

if __name__=='__main__':
    print(e010())
    #print(Euler_10())
