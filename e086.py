#!/usr/bin/env python3.2
from scipy.optimize import fsolve
from newton import newton
def e84(top = 10**5):
    count = 0
    distmin = lambda x,mn:(mn[1]**2+x**2)**.5+(mn[2]**2+(mn[0]-x)**2)**.5        
    dist = lambda x,mn:(x-mn[0])/((mn[0]-x)**2+mn[2]**2)**.5+x/(mn[1]**2+x**2)**.5
    c = 0
    m = 101
    count = 1979
    tmp = 0
    while True:
        m1 = m-1
        tmp = 0
        aset = set()
        for m2 in range(1,m):
            for m3 in range(1,m):
                m2s = str(m2)
                m3s = str(m3)
                if (m2s+m3s) in aset:continue
#                print(m1,m2,m3)
                #x = fsolve(dist,(m1/2+3/4),(m1,m2,m3))
                x = newton(distmin,dist,m1/2+3/4,[m1,m2,m3]) 
                if distmin(x,[m1,m2,m3])%1==0:tmp+=1;aset.update([m2s+m3s,m3s+m2s])
        count+=tmp
        if count>=top:return m
        m+=1
        print(count)
    return count


if __name__=='__main__':
    print(e84())
