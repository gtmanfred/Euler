import e067t
def e67(tri = e067t.tri):
    return tot(tri)

def tot(triangle):
    while len(triangle)>1:
        reducetri(triangle)
    return triangle[0][0]

def reducetri(triangle):
    lastrow=triangle[-1]
    for index in range(len(triangle)-1):
        triangle[-2][index] += min(lastrow[index:index + 2])
    del triangle[-1]

if __name__=='__main__':
    print(e67())
