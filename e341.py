from math import *
from time import time
from bisect import bisect
from decimal import Decimal
def e341(target = 10**3):
    tot = 0
    mini = 1000
    t = time()
    #keys = [i**3 for i in range(1,target)]
    for j in range(1,target):
        i = j**3
#        if j > mini:print(j/target,time()-t);t = time();mini+=1000
        tot+=g(i)
    print()
    return tot

phi = (1+5**.5)/2
def g(n):
    ret = phi**(2-phi)*n**(phi-1)+E(n)
    if ret%1>=.5:return ceil(ret)
    else:return floor(ret)

def E(n):
    return 0
    return n**(phi-1)/log(n)

def findNthGolumb(n, x, upto) :
    return bisect(x, n, 1, upto) - 1

def golumb(n) :
    x = [0]*1000000
    x[1], x[2] = 1, 2
    cur, start = 2, 3

    while x[start - 1] < n :
        times = bisect(x, cur, 1, start) - 1#findNthGolumb(cur, x, start)
        while times :
            x[start] = x[start - 1] + cur
            start += 1
            times -= 1
        cur += 1

    return findNthGolumb(n, x, start)

def e341_test(target = (10**3)):
    t = time()
    n = {1:1,3:2,5:3,8:4,11:5,15:6,19:7}
    nx = [list(i) for i in zip(n.keys(),n.values())]
    i = 8
    j = [nx[i][0] for i in range(len(n))].index(i)
    mini=1000000000
    while nx[-1][0]<target**3:
        if nx[-1][0]>mini:print(len(nx),nx[-1][0]/target**3);mini+=1000000000
        nx+=[[nx[-1][0]+nx[j][1],i]]
        i+=1
        if i>nx[j][0]:
            j +=1 
    tot = 0
    keys = [i[0] for i in nx]
    print('start',time()-t)
    te = 0
    t = time()
    mini = 10
    for i in range(1,target):
        if i>mini:mini+=10;print(i/target,time()-t);t = time()
        test = i**3
        for k in keys[te:]:
            if test<=k:x = k;break
        te = keys.index(x)
        tot+=nx[te][1]
    print()
    return tot
from memorize import memo
from time import time
@memo
def a(n):
    if n == 1:return 1
    else:
        return 1+a(n - a(a(n-1)))

s = lambda n: cache.get(n) and cache.get(n) or 1+s(n - s(s(n-1)))
cache = {1:1}
def e341_2(target = 1000):
    global cache
    tot = 0
    mini = 100000
    i = 1
    t = time()
    while i<target**3:
        if i>mini:print(i,(time()-t)*10000);t = time();mini+=100000
        cache[i] = s(i)
        i+=1
    for i in range(1,target):
        tot+=s(i**3)
    return tot
if __name__=='__main__':
    print(e341_test())
