from time import time
from math import *
t = time()
def e094(N = 10**9):
    a = 2
    b = 1
    ret = 0
    while True:
        a, b = a * 2 + b * 3, a + b * 2
        if a% 3 == 1:
            s = a + 1
        else:
            s = a - 1
        if s * 2> N:
            return ret
        ret += s*2

def e094_slow(top = int(pow(10,9))):
    from scipy.optimize import fsolve
    sup = lambda x:(x*3+1)/2
    sdown = lambda x:(x*3-1)/2
    areaup = lambda x,s:(s*(s-x)**2*(s-x-1))**.5
    areadown = lambda x,s:(s*(s-x)**2*(s-x+1))**.5
    tot = 0
    to = 1000000
    for i in range(3,top//3+1):
        if i>to:print(i,time()-t);to+=1000000
        perup = i*3+1
        perdown = i*3-1
        area1 = areaup(i,perup/2)
        area2 = areadown(i,perdown/2)
        if area1==int(area1):tot+=perup
        elif area2==int(area2):tot+=perdown
        if tot>518408346:break
    return tot
    '''
    func1 = lambda x,a:(a+1)/sin(x)-a/sin((180-x)/2)
    func2 = lambda x,a:(a-1)/sin(x)-a/sin((180-x)/2)
    cosinerule = lambda x,angle:(x/sin((180-angle)/2))*sin(angle)   #(x**2+x**2-(2*x*x)*cos(angle))
    tot = 0
    for a in range(1,10**9):
        if a%1000==0:print(a)
        per1 = a*2+a+1
        per2 = a*2+a-1
        if per1>top:return tot
        angle1 = fsolve(func1,30,(a))
        angle2 = fsolve(func2,30,(a))
        test1 = float(str(cosinerule(a,angle1))[:2])
        test2 = float(str(cosinerule(a,angle2))[:2])
        if test1 == a+1:
            tot+=per1
            print('uptot:',tot)
        if test2 == a-1:
            tot+=per2
            print('downtot:',tot)
    '''

if __name__=='__main__':
    print(e094())
