from script.maths import gcd#,primetree
from script.helpers import primetree
from operator import mul
from functools import reduce
from itertools import combinations as combo
def e127(top):
    ret = 0
    l = 0
    for a,b in combo(range(1,top),2):
        if not a&1 and not b&1:continue
        c = a+b
        if not a&1 and not c&1:continue
        if not c&1 and not b&1:continue
        if a!=l:
            print(a,b,end='\r')
            l=a
        if a>b:continue
        if gcd(a,b)!=1 or gcd(b,c)!=1 or gcd(c,a)!=1:
            continue
        if rad(a,b,c)<c:
            ret+=c
    print()
    return ret
def rad(a,b,c):
    num = a*b*c
    tree = [i[0] for i in primetree(num)]
    #tree = primetree(num)
    return reduce(mul,tree)
if __name__=='__main__':
    print(e127(1000))
