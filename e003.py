from script.maths import isprime2
from script.sieve import sieve
def e003(num=600851475143):
    p = sieve(round(num**.5))
    for i in p[::-1]:
        if num%i:continue
        else:return i

def Euler_3(num=600851475143):
    primes = []
    i=2
    while i <= num:
        if num%i ==0 and isprime2(i):
            num = num//i
            primes = primes +[i] 
            i = 2
        i+=1
    return max(primes)
 
def isprime(n):
    i = 2
    while i<n:
        if n%i ==0:
            return False
        i += 1
    return True

if __name__=='__main__':
    #print(e003())
    print(Euler_3())
