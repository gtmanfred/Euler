from memorize import *
from maths import *
primes = []
def e204(n=10**9):
    count = 0
    for i in range(2,n):
        print(i)
        b = True
        for j in primedivs(n):
            if j>100:b=False
        if b:count+=1
    return count
            

@memorize
def primedivs(n):
    global primes
    divs = []
    if isprime2(n):return [n]
    for i in primesd3(n):
        if n%i==0:
            divs+=[i]
            divs+=primedivs(n//i)
            break
    return divs

if __name__=='__main__':
    print(e204())
