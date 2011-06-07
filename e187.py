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
    print('start',time()-ti)
    b = True
    for i in range(1,len(alist)):
        tx = time()-ti
        m = tx//60
        s = tx-(m*60)
        if i<10**5:print(i,'{}min {}sec'.format(m,s),end='\r') 
        if i%10**5==0:print(i,'{}min {}sec'.format(m,s),end='\r')
        for j in range(i,len(alist)):
            if alist[i]*alist[j]>10**8:break
            count+=1
    return count
if __name__=='__main__':
    print(e187())
