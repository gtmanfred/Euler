def e174():
    ret = 0
    for n in range(1,11):
        ret += N(n)
    return ret
def N(n):
    top = 10**6
    ret = 0
    mini = 1000
    for t in range(1,top+1):
        if t>mini:
            mini+=1000
            print(t)
        if L(t)==n:
            ret+=1
    return ret
def L(t):
    maxs = t//4+1
    ret = 0
    hole =(maxs-2)
    if (maxs-1)*4==t:
        ret+=1
    for i in range(1,hole):
        if int((t+i)**.5)**2==t+i:
            ret+=1
    return ret
if __name__=='__main__':
    print(N(15))
