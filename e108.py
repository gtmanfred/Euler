from maths import num_factors
from time import time
t = time()
def Euler_108(sols = 10**3):
    n = 120121
    test = 100
    maxc = 0
    while True:
        count = (num_factors(n*n)+1)//2
        if count>=sols:return n
        if count>maxc:maxc = count;print(maxc,n)
        #if count>test:print('n: ',n,'time: ',time()-t,'counts:',count);test+=(count//100*100-test+100)
        #if n%1000==0:print(n)
        #if (num_factors(n*n)+1)//2>=sols:return n
        n+=1
    return n
'''
#        if n%100==0:print(n)
        count = 0
        for i in range(n+1,n*2):
            y = (i*n)/(i-n)
            if y%1==0:count+=1
        if count >= sols:return n
        n+=1
    return 'not finished'
'''
if __name__=='__main__':
    print(Euler_108())
