from maths import primedivs
from time import *
t = time()
def Euler_179(top = 10**7):
    divs = primedivs(top,t)
    count = 1 #starts at one for 2 and 3 which are skipped because they are prime
    print('start')
    for i in range(1,top):
        if i%10**5==0:print(i//10**5,time()-t)
        if len(divs[i])==1 or len(divs[i+1])==1:continue
        if findnumdivs(divs[i])==findnumdivs(divs[i+1]):count+=1
    return count

def findnumdivs(x):
    y = set(x)
    ret = 1
    while len(y):
        ret*=x.count(y.pop())+1
    return ret

if __name__=='__main__':
    print(Euler_179(),time()-t)
