from scipy.optimize import fsolve
from decimal import Decimal
from math import *
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
