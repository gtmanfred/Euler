from itertools import product
def ev(i,j):
    tot = i**j
    res = {}
    pos = product(range(1,i+1),repeat = j)
    for i in pos:
        tots = sum(i)
        res[tots] = res.setdefault(tots, 0) +1
    return dict([(x,(y/tot)) for x,y in res.items()])

def Euler_205():
    peter = ev(4,9)
    colin = ev(6,6)
    p2w=0
    for i in peter.items():
        colinthrow = 0 
        for j in colin.items():
            if j[0] >= i[0]: break
            colinthrow += j[1]
        p2w += colinthrow*i[1]
    return p2w

if __name__=='__main__':
    print(Euler_205())
