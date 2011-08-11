from script.memorize import *
from script.maths import isprime2
ps = [2,3,5,7,11,13,17,19]
top = 0
@memo
def nextprime(p):
    if p%2==0:p+=1
    while not isprime2(p):
        p+=2
    if p>=top:return []
    return [p]+nextprime(p+1)

def changetop():
    global top
    top +=1000

def primes(x):
    if x>1000:x = x//1000
    global top
    top = 1000
    p = [2,3]
    s = 1
    while s<=x:
        p+=nextprime(p[-1]+2)
        changetop()
        s+=1
    return p
if __name__=='__main__':
    i = (primes(10**6))

