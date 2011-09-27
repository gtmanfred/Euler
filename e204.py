from itertools import combinations_with_replacement as cwr
from script.allsieve import soe
from math import log
from functools import reduce
from operator import mul
def e204(top,n):
    print(cham(top,n))
def cham(top,n):
    ret = 0
    for i in range(1,top):
        if test(i,n):
            print(i)
            yesno=1
        else:
            yesno=0
        ret+=yesno
    return ret
def test(num,n):
    p = soe(n+1)+[0]
    j = 0
    while p[j]!=0:
        if num%p[j]==0:
            num=num//p[j]
        else:
            j+=1
    if num<n:
        return True
    else:
        return False

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
        print(cham(10**8,5))
