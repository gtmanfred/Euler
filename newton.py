from time import time
from math import *
def newton(fn=0,fp=0,x=.1,mn = 0):
    t = time()
    test = 0
    if not fn and not fp:
        from scipy.misc import derivative
        func = input("equation(use x as unknown):")
        fn = lambda x:eval(func)
        fp = lambda x:derivative(fn,x)
        print('div')
    elif not fp:
        from scipy.misc import derivative
        fp = lambda x:derivative(fn,x)
    if mn:
        while fn(x,mn)!=0:
            if fp(x,mn)==0:x+=1;print('error');test+=1;print(test);break
            x,lastx = x-(fn(x,mn)/fp(x,mn)),x
    else:
        while fn(x)!=0 or rerr>10**-12:
            x,lastx = x-(fn(x)/fp(x)),x
            rerr = abs(lastx-x)/x
    return x

if __name__=='__main__':
    t = time()
    print(newton(),time()-t)
    t = time()
    fn = lambda x: x**2+3*x+1
    fp = lambda x:eval('2*x+3')
    print(newton(fn,fp),time()-t)
    t = time()
    print(newton(fn),time()-t)
