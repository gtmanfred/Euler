from time import *
t = time()
from maths import gcd
from math import *
def e75(top=1500000):
    count = 0
    alist = [0]*top
    tops = int(sqrt(top))
    for i in range(1,int(tops),2):
        for j in range(2,int(tops)-i,2):
            if i+j>top:break
            if gcd(i,j)==1:
                x = abs(j*j-i*i)
                y = 2*i*j
                z = j*j+i*i
                s = x+y+z
                for p in range(s,top,s):alist[p]+=1
    return alist.count(1)
    '''
    alist = [i for i in range(top+1)]
    adict = dict.fromkeys(alist,0)
    sqrs = {i**2:i for i in range(top//2+1)}
    print(type(sqrs))
    #sqrsd = dict.fromkeys(sqrs,1)
    #sqrsd[12]=1
    num = 0
    for i in sqrs.keys():
        num+=1;print(num)
        if i!=0:
            x = sqrs.get(i)
            for j in sqrs.keys():
                if j !=i and j>i:
                    y = sqrs.get(j)
                    if x+y>top:break
                    k = i+j
                    if sqrs.get(k):
                        z = sqrs.get(k)
                        index = x+y+z
                        if index>top:break
                        adict[index] = adict.get(index)+1
    blist = [1 for i in adict.keys() if adict.get(i)==1]
    return sum(blist)
             
    alist = [i for i in range(top)]
    adict = dict.fromkeys(alist,0)
    for i in range(3,top+1):
        print(i)
        if i%10**4==0:print(i,time()-t)
        for j in range(i+1,top+1):
            if gcd(j,i)!=1:continue
            if i+j>top:break
            k =pow(i**2+j**2,.5)
            if (i+j+k)>top:break
            if k%1==0:print('add');adict[i+j+k]=adict.get(i+j+k)+1
    alist = [1 for i in adict.keys() if adict.get(i)==1]
    return sum(alist)
    '''

if __name__=='__main__':
    print(e75())
