from memorize import *
times = ['O','A','L']
top = 0
test={}
@memorize
def e191(n, a, l):
    if n == 0:
        return 1
    ret = e191(n - 1, 0, l)
    if l == 0:
        ret += e191(n - 1, 0, 1)
    if a < 2:
        ret += e191(n - 1, a + 1, l)
    return ret

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
    print(e191(30, 0, 0))
