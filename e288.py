def e288(p, q, e):
    m = p ** e
    s = 290797
    r = 0
    k = 0
    mini = 10000
    for n in range(q + 1):
        if n>mini:print(n/q,end='\r');mini+=10000
        t = s % p
        s = s * s % 50515093
        r = (r + t * k) % m
        if n < e:
            k += p ** n
    print()
    return r % m
if __name__=='__main__':
    print(e288(61,10**7,10))
