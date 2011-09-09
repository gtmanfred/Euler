#from scipy.optimize import fsolve
from script.newton import new2
from itertools import product
from script.helpers import divs
from script.memorize import memo
divs = memo(divs)

def C(n):
    #if n&1:
    #    return 0
    x0 = int(find(n,1,1))+1
    alist = set()
    count = lambda x,y,z,l:2*(x*y+y*z+z*x)+4*(l-1)*(x+y+z+l-2)
    for i,j,k in product(list(range(1,x0)),range(1,x0),range(1,x0)):
        if i<j or i<k:continue
        if j<k:continue
        l = 1
        tmp = sorted([i,j,k])
        '''
        if calc(i,j,k,1)==n:
            alist.add(str(tmp[0])+'x'+str(tmp[1])+'x'+str(tmp[2]))
        l+=1
        '''
        t = count(i,j,k,l)#calc(i,j,k,l)
        while t<=n:
            if t==n:
                alist.add(str(tmp[0])+'x'+str(tmp[1])+'x'+str(tmp[2]))
            if t>n:break
            l+=1
            t = count(i,j,k,l)#calc(i,j,k,l)
    return len(alist)
    '''
    while True:
        x = find(n,y,1)
        tmp = sorted([x,y,z])
        if calc(x,y,z)==n:
            alist.add(str(tmp[0])+'x'+str(tmp[1])+'x'+str(tmp[2]))
            print(alist)
        if x==0:
            return [len(alist),alist]
        if y>n**(1/3):
            y = z
            z+=1
        y+=1
    '''
def find(n,y,z):
    args = [y,z,n]
    fn = lambda x,args:x*args[0]*2+x*args[1]*2+args[0]*args[1]*2-args[2]
    #return int(fsolve(fn,1,args))
    fp = lambda x,args:args[0]*2+args[1]*2
    return new2(fn,fp,args)
def calc(x,y,z,l):
    c = lambda x,y,z:x*y*2+x*z*2+z*y*2
    if l == 1:
        return c(x,y,z)
    else:
        a = (l-1)*2-1
        return x*4*a+y*4*a+z*4*a+calc(x,y,z,l-1)
        '''
        tmp = c(x,y,z)
        for i in range(2,l+1):
            #tmp += c(x,y,z)
            a = (i-1)*2-1
            tmp+=x*4*a+y*4*a+z*4*a
        return tmp
        '''
if __name__=='__main__':
    x = 10
    i=2
    while True:
        if C(i)==x:break
        print(i)
        i+=2
    print(i)
