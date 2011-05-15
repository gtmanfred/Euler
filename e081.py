from e067 import e67
def e081(fil = open('matrix.txt')):
    f = list(x.split(',') for x in fil.read().split('\n'))[:-1]
    r = len(f);c = len(f[0])
    tmp = []
    for i in f:
        tmp.append( [int(x) for x in i])
    f = tmp
    r -=1;c-=1
#    f = mat
#    r = len(f);c = len(f[0])
  #  print(f)
    for i in range(r,-1,-1):
        for j in range(c,-1,-1):
            if (i==r and j==c): continue   
            if (j==r): minx = f[i+1][j]
            elif (i==c): minx = f[i][j+1]
            else: minx = min(f[i+1][j], f[i][j+1])
            f[i][j] += minx
    return f[0][0]
def e081_slow(fil = open('matrix.txt')):
    f = list(x.split(',') for x in fil.read().split('\n'))[:-1]
    for i in f:
        tmp.append( [int(x) for x in i])
    f = tmp
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
    print(len(tri1))
    print(len(tri2))
    return e67(tri1)+e67(tri2)
if __name__=='__main__':
    print(e081())
