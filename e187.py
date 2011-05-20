from time import time
from scipy import cross
from maths import primesd3,fact
ti = time()
def e187(top = 10**8//2):
    print(time()-ti)
    #p = list(primesd2(top))
    #print(len(p))
    alist = primesd3(top)
    count = len(alist)
    print('start')
    for i in range(1,len(alist)):
        if i<10**5:print(i)
        if i%10**5==0:print(i,time()-ti)
        for j in range(i,len(alist)):
            if alist[i]*alist[j]>10**8:break
            count+=1
    print(count)
if __name__=='__main__':
    print(e187())
