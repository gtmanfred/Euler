from itertools import combinations_with_replacement as cwr
from script.allsieve import soe
from math import log
from functools import reduce
from operator import mul
def e204(top,n):
    print(cham(top,n))
def cham(num,n):
    aset = set([1])
    exp = int(log(num)/log(2))
    primes = soe(n+1)
    count = 2
    combos = [cwr(primes,i) for i in range(1,exp)]
    for i in range(1,exp):
        print(i*1.0/exp)
        for combo in cwr(primes,i):
            tmp = reduce(mul,combo)
            if tmp<=num:
                count+=1
                #aset.add(tmp)
            else:
                tests = list(combo)[0]**len(combo)
                if tests>num:
                    print(combo,len(combo))
                    break
    print(count)
    #return len(aset)+1
'''
def test204(top,n):
    return len(ham(top,n))
def countham(top,n):
    count = 0
    for i in range(1,top+1):
        if ham(i,n):
            count+=1
    return count
def ham(num,n):
    if num==1:
        return True
    if isprime(num):
        if num<=n:
            return True
        else:
            return False
    if max([i[0] for i in primetree(num)])<=n:
        return True
    return False
'''
if __name__=='__main__':
    import sys
    a = sys.argv
    if len(a)==3:
        print(cham(int(a[1]),int(a[2])))
    else:
        print(cham(1000,5))
