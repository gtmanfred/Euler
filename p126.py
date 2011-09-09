from math import sqrt
from script.memorize import memo
from script.helpers import divs 
#divs = memo(divs)
divs=memo(divs)
def c(n):
    if n % 2:
        return 0
    count = 0
    p = -2
    q = n // 2 + p + p
    for w in range(1, int(sqrt((n - 2) / 4)) + 1):
        p += 2
        q += 4 - p - p
        s = p + 2
        t = p * p + p + q + 1
        while s * s <= t:
            ds = divs(t)
            for i, d in enumerate(ds):
                if d >= s:
                    break
            mid = (len(ds) + 1) // 2
            if i < mid:
                count += mid - i
            s += 2
            t += s - 1
    return count
 
if __name__=='__main__':
    maxi = 1
    n = 6
    tmp = c(n)
    while tmp != 1000:
        if tmp>maxi:maxi=tmp;print(maxi,n)
        n += 2
        tmp=c(n)
    print(n)
