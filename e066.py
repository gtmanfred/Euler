from script.maths import *
def Euler_66(top = 1000):
    p = primes(top)
    ret = [0 for i in range(top+1)]
    for d in p:
        #execute Chakravala method
        tmp=1;x1=1;y=0;k=1;dsqrt=d**.5
        while k!=1 or y==0:
            tmp = k*(tmp//k+1)-tmp
            tmp = tmp-int((tmp-dsqrt)/k)*k
            x = (tmp*x1+d*y)/abs(k)
            y = (tmp*y+x1)/abs(k)
            k = (tmp*tmp-d)//k
            x1 = x
        ret[d] = x
    return ret.index(max(ret))

if __name__=='__main__':
    print(Euler_66())
