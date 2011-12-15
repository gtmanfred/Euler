from math import floor
from script.newton import new2
#from sympy import *
#from scipy.optimize import fsolve
g = lambda x,n:x**3-2**n*x**2+n
gprime = lambda x,n:3*x**2-2**n*2*x
f = lambda x,n:x**4/4-2**n*x**3/3+n*x
def e356(start=1,end=30):
    a = pow(3,987654321,10**8)

#    b = pow(new2(g,gprime,2,100)-3+1,987654321)

#    ret = 0
#    for i in range(start,end+1):
#        print(i)
#        ret+=pow(fsolve(g,x0=10**100,args=(i)),987654321,10**8)
#    return ret
if __name__=='__main__':
    print(e356())
