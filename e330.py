from math import *
from script.maths import mullcm,primetree,factrec as fact
from script.math2 import bicoeff as bc
from script.memorize import memo
from fractions import Fraction as f
def B():
    mat = [[]]*136
def test():
    for i in range(100,9101,100):
        print(i/9100,end='\r')
        x = abi(i)
    return abi(9100)+(-2*abi(9100)+fact(9100))
@memo
def abi(n):
    ret = fact(n)
    for i in range(n):
        ret+=bc(n,i)*abi(i)
    return ret
def bbi(n,a = 0):
    if a:
        return fact(n)-2*a
    else:
        return fact(n)-2*abi(n)
def e330(n = 10**9,m=77777777):
    p = primetree(m)
    d = [n%(x*(x-1)) for x in p]
    n = max(d)
    tp = mullcm([i-1 for i in p])
    for i in range(1,max(p)+2):
        tmp=D(i)
@memo
def arec(top):
    ret = 0
    if top==0:return e-1
    for n in range(1,top+1):
        ret+=arec(top-n)/fact(n)
    ret+=(e-1)-sum([1/fact(i) for i in range(1,top+1)])
    return ret

@memo
def a(n):
    if n==0:return e-1
    if n==1:return 2*e-3
    if n==2:return 7/2*e-6
    if n<0:return 1
    x = 0
    i = 1
    while True:
        lastx,x = x,x+a(n-i)/fact(i)
        i+=1
        if lastx==x:return x
def b(n):
    return a(n)-1
@memo
def D(n):
    if n<0:return 0
    return round((fact(n)*b(n))/(e-2))
def A(n):
    return D(n)
def B1(n):
    return round(fact(n)-2*D(n))
def Bval(n):
    return fact(n)-2*A(n)
if __name__=='__main__':
    print(test())
