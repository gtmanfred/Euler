from helpers import totient4 as t
def memo(f):
    cache={}
    def helper(x):
        if cache.get(x):pass
        else:cache[x]=f(x)
        return cache.get(x)
    return helper
@memo
def e342(top=10000):
    result = 0
    for n in range(2,top):
        if n%10000==0:print(n,end='\r')
        x = t(n**2)
        if round(x**(1/3))**3==x:result+=n
    print()
    return result
if __name__=='__main__':
    print(e342(10**10))
