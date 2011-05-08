import e067t
def Euler_67():
    return tot(e067t.tri)

def tot(triangle):
    while len(triangle)>1:
        reducetri(triangle)
    return triangle[0][0]

def reducetri(triangle):
    lastrow=triangle[-1]
    for index in range(len(triangle)-1):
        triangle[-2][index] += max(lastrow[index:index + 2])
    del triangle[-1]

if __name__=='__main__':
    print(Euler_67())
