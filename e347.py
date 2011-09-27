from math import ceil, log
from script.allsieve import soe
from itertools import combinations,combinations_with_replacement as cwr
from operator import mul
from functools import reduce
from script.memo import memo
def M(p,q,N):
    exp = ceil((log(N)-log(max([p,q])))/log(min([p,q])))
    tmp = [0]
    for e in range(1,exp+1):
        combos = cwr([p,q],e)
        nums = []
        for i in combos:
            if p in i and q in i:
                j = reduce(mul,i)
                if j<=N:
                    nums+=[j]
        #nums = [j for j in reduce(mul,i) for i in combos if j<=N and p in i\
        #and q in i]
        if nums:
            tmp+=[max(nums)]
        #if N in tmp:return N
    return max(tmp)

def S(N):
    primes = soe(N//2+10)#[-1::-1]
    s = 0
    tmp = 0
    tmp2 = 0
    tmpp = 0
    mini = 0
    count = False
    for p,q in combinations(primes,2):
        #if p>3162:break
        if p==tmpp:continue
        if p*q>N:
            if count and p!=tmpp:
                #break
                pass
            else:
                tmpp = p
                count = True
                continue
        else:
            count = False
            tmpp=0
        if tmp2!=p:
            mini=0
            tmp2=p
            print()
        if q>mini:
            mini+=3000
            print(p,q,end='\r')
        t = M(p,q,N)
        s+=t
    print()
    return s
if __name__=='__main__':
    #print(M(2,3,100))
    #print(M(3,5,100))
    print(S(100))
    #print(S(10000000))
