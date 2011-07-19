'''
from scipy.optimize import fsolve
from decimal import Decimal
'''
from math import *
def e341():
    total = 0
    arr = [i**3 for i in range(1,10**6)]
    print('start')
    arr2 = [1,2,2]
    s = 1+2*2+3*2
    index = 3
    while(s < 10**18):
        print(s/10**18,end='\r')
        l = len(arr2)
        k = len(arr2)+arr2[index-1]
        arr2 += arr2[index-1]*[index]
        s += index*((k*(k+1))/2 - (l*(l+1))/2)
        index += 1
    print()
    s1 = 0
    s2 = 0
    i = 0
    for k in arr:
        print(k/arr[-1],end='\r')
        while(s2 + arr2[i]*(i+1) < k):
            s2 += arr2[i]*(i+1)
            s1 += arr2[i]
            i += 1
        total += (s1+ int(ceil((k-s2)*1.0/(i+1))))
    print()
    return total
if __name__=='__main__':
    print(e341())
'''
phi = (1+(5**(.5)))/2
g = lambda n: round(phi**(2-phi)*n**(phi-1))
e = lambda n: round(n**(phi-1)/log(n))
res = 1
err = 0
for i in range(2,1000):
    res+=g(i**3)
    err+=e(i**3)
print(err)
print(res)
a = (153506976-res)/res
print(a)
print(res+res*a)
res2 = 1
err2 = 0
for i in range(2, 10**6):
    res2+=g(i**3)
    err2+=e(i**3)
print(err2)
print(res2)
print(Decimal(res2+res2*a))
'''
