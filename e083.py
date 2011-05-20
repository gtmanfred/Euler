def e083(m = 'matrix.txt'):
    M = [[int(y) for y in x.strip().split(',')] for x in open(m).readlines()]
    N = [[1000000 for x in range(len(M))] for y in range(len(M))]
    N[0][0] = M[0][0]
    change, iters = True, 0
    while change:
        change, iters = False, iters+1
        for i in range(len(M)):
            for j in range(len(M)):
                paths = []
                if (i-1)>=0: paths.append(N[i-1][j])
                if (i+1)<len(M): paths.append(N[i+1][j])
                if (j-1)>=0: paths.append(N[i][j-1])
                if (j+1)<len(M): paths.append(N[i][j+1])
                mp = min(paths)
                if mp+M[i][j] < N[i][j]:
                    N[i][j] = mp + M[i][j]
                    change = True
    return [N[-1][-1], iters]

if __name__=='__main__':
    print(e083())
