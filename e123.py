from time import time
t = time()
from maths import *
from math import *
from scipy.optimize import fsolve
def e123(top = 10**6):
    p = primesd1(10**6)
    print(len(p))
    print('start')
    sums = lambda x,y,z:((x-1)**y+(x+1)**y)%z**2-10**10
    rem = lambda s,t:s%t**2
    num = 7030
    while num<21100:
        i = p[num]
        s = sums(i,num)
        r = rem(s,i)
        if r>10**10:return num
        num+=5
        if num%1000==0:print(num,time()-t)
    return 'none'

if __name__=='__main__':
    print(e123())
