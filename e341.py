def e341(target = (10**3)):
    n = {1:1,3:2,5:3,8:4,11:5,15:6,19:7}
    nx = [list(i) for i in zip(n.keys(),n.values())]
    i = 8
    j = [nx[i][0] for i in range(len(n))].index(i)
    while nx[-1][0]<target**3:
        nx+=[[nx[-1][0]+nx[j][1],i]]
        i+=1
        if i>nx[j][0]:
            j +=1 
    tot = 0
    print(len(nx),target**3)
    for i in range(1,target):
        test = i**3
        x = [test<=k for k in nx
    return tot
if __name__=='__main__':
    print(e341())
