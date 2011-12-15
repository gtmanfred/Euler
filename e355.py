from script.maths import euclgcd,mulgcd
from itertools import product;
def e355(num=10):
    ret=0
    maxret=0
    for i in range(num,0,-1):
        alist = [i]
        for j in range(num-1,0,-1):
            if i==j:
                continue;
            if all(euclgcd(j,a)==1 for a in alist): 
                alist+=[j];
        ret=sum(alist)
        if maxret<ret:
            print(alist,ret)
            maxret=ret
    return maxret;
if __name__=='__main__':
    print(e355())
    print(e355(30))
    print(e355(100))
    print(e355(200000))
