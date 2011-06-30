from maths import *


def Euler_12(num=500):
    facts=[1]
    i=1
    b=True
    while b:
        n = i*(i+1)//2
        if numfacts(n)>num:
            b=False
            return n
        i +=1

if __name__=='__main__':
    print(Euler_12())
