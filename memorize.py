def memorize(f):
    cache = {}
    def helper(x):
        if x not in cache:
            cache[x] = f(x)
        return cache[x]
    return helper
def memo(f):
    cache = {}
    def helper(x):
        if x not in cache:
            cache[x] = f(x)
        return cache[x]
    return helper
def memorize3(f):
    cache = {}
    def helper(x,y,z):
        p = str(x)+' '+str(y)+' '+str(z)
        if p not in cache:
            cache[p] = f(x,y,z)
        return cache[p]
    return helper
def memorize2(f):
    cache = {}
    def helper(x,y):
        p = str(x)+' '+str(y)
        if p not in cache:
            cache[p] = f(x,y)
        return cache[p]
    return helper
