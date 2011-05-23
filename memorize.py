def memorize(f):
    cache = {}
    def helper(x,y,z):
        p = str(x)+' '+str(y)+' '+str(z)
        if p not in cache:
            cache[p] = f(x,y,z)
        return cache[p]
    return helper
