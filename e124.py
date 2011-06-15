from maths import findallfactors
def Euler_124(top = 100000):
    alist = []
    for n in range(1,top+1):
        aset = set(findallfactors(n))
        rad = 1
        for i in aset:
            rad*=i
        alist.append([rad,n])
    ret = sorted(alist)
    return ret[10000-1]

if __name__=='__main__':
    print(Euler_124(100000))
