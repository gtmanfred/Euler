times = ['O','A','L']
top = 0
test={}
def e191(left,nl,na):
    if(nl>=3): return 0
    if(na>1): return 0
    if(left<=0): return 1
 
    key="%d %d %d"%(left,nl,na)
    if(key in test): return test[key]
 
    total=0
    total+=e191(left-1,0,na)
    total+=e191(left-1,nl+1,na)
    total+=e191(left-1,0,na+1)
 
    test[key]=total
    return total

def e191_rec(n=30):
    global top
    top = n//2
    count = 0
    for p in times:
        print(p)
        count+=combo(p,n-1)
    return count
def combo(p,n):
    count = 0
    if n == 0 and tester(p):
        return 1
    if n==top:
        print(p)
    if tester(p):
        for i in times:
            count += combo(p+i,n-1)
        return count
    else:return 0
        

def tester(p):
    if p.count('L')>1:return False
    elif 'AAA' in p:return False
    else:return True

if __name__=='__main__':
    print(e191(30,0,0))
