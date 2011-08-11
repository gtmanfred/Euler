def ncrrow(row,lc=-1):
    if lc==-1:lc=row+1
    if lc<row+1 and lc>row//2:
        lc = row-lc
        print(lc)
    r = row+1
    vc = [1]
    c = 1
    mini = 10000
    while True:
        if len(vc)>mini:
            print(lc,len(vc)/(lc),end='\r')
            mini+=10000
        vc.append(vc[-1]*(r-c)//c)
        if len(vc)>lc:return vc[-1]
        if vc[-1]==1:return vc
        c+=1

def ncr(n):
    x=[[1]]
    for i in range(n+1):
        x.append([sum(i) for i in zip([0]+x[-1],x[-1]+[0])])
    return x
