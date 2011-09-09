from script.extra import elist
def e345(file = 'script/e345.txt'):
    with open(file) as f:
        matrix = f.read().split('\n')[:-1]
        matrix = [i.split(' ') for i in matrix]
    matrix = [[1000-int(i) for i in j] for j in matrix]
    matrixrev = [[matrix[i][j] for i in range(len(matrix))] for j in\
            range(len(matrix))]
    return hungarian(matrix,matrixrev)

def hungarian(m,mr):
    l = len(m)
    rowmin = [min(line) for line in m]
    mprime = [[i[k]-rowmin[j] for k in range(l)] for j,i in enumerate(m)]
    '''
    mrprime = [[mprime[i][j] for i in range(l)] for j in range(l)]
    colmin = [min(line) for line in m]
    mrprime = [[i[k]-colmin[j] for k in range(l)] for j,i in enumerate(mrprime)]
    mprime = [[mrprime[i][j] for i in range(l)] for j in range(l)]
    '''
    newm = [elist(i).index(0) for i in mprime]
    return newm
if __name__=='__main__':
    print(e345())
