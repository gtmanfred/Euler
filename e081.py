from e067 import e067
def e081(name = 'script/matrix.txt'):
    with open(name) as fil:
        f = list(x.split(',') for x in fil.read().split('\n'))[1:-1]
    r = len(f);c = len(f[0])
    tmp = []
    for i in f:
        tmp.append( [int(x) for x in i])
    f = tmp
    r -=1;c-=1
    for i in range(r,-1,-1):
        for j in range(c,-1,-1):
            if (i==r and j==c): continue   
            if (j==r): minx = f[i+1][j]
            elif (i==c): minx = f[i][j+1]
            else: minx = min(f[i+1][j], f[i][j+1])
            f[i][j] += minx
    return f[0][0]
def e081_slow(fil=0):
    if fil:
        return evaluate(fil)
    else:
        with open('script/matrix.txt') as fil:
            f = list(x.split(',') for x in fil.read().split('\n'))[1:-1]
        return evaluate(f)
def evaluate(f):
    tmp = []
    for i in f:
        tmp.append( [int(x) for x in i])
    f = tmp
    r = len(f)-1;c = len(f[0])-1
    tri1 = []
    for x in range(r):
        tmp = []
        ic = 0
        ir = x
        while ir>=0 and ic<=x:
            tmp+=[f[ir][ic]]
            ic+=1
            ir-=1
        tri1.append(tmp)
    tri2 = []
    for x in range(r-1,-1,-1):
        tmp = []
        ic = r-1
        ir = x
        while ir<=r-1 and ic>=x:
            tmp+=[f[ir][ic]]
            ic-=1
            ir+=1
        tri2.append(tmp)
    return e067(tri1)+e067(tri2)
if __name__=='__main__':
    print(e081())
