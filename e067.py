def e067(tri = 0):
    if not tri:
        with open('script/triangle.txt') as f:
            tri=[[int(x) for x in j] for j in [i.split(' ') for i in \
                f.read().split('\n')][1:-1]]
    return tot(tri)

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
    print(e067())
