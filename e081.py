alist = list(x for x in open('e081.txt').read().split('\n'))
blist = list(alist[alist.index(y)].split(',') for y in alist)
clist = []
for z in blist[:-1]:
    clist.append(list(int(x) for x in z))
print(len(clist))
for i in range(78,-1,-1):
    clist[79][i] += clist[79][i+1]
    clist[i][79] += clist[i+1][79]

    for i in range(78,-1,-1):
        for j in range(78,-1,-1):
            clist[i][j] += clist[i][j+1] if (clist[i][j+1] < clist[i+1][j]) else clist[i+1][j]
    print(clist[0])
