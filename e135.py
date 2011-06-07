sqrs = {i:i**2 for i in range(1,10**6+1)}
print(len(sqrs))
cache = [0]*10**6
def e134():
    last = -1
    alist = list(sqrs.values())
    for i in range(1,10**6):
        if cache[1155]!=last:
            print(cache[1155])
            last = cache[1155]
        for j in range(1,10**6):
            if i-j<0:break
            for k in range(1,10**6):
                tmp = i-j-k
                if tmp<0:break
                if tmp<=10**6:
                    cache[tmp]+=1
    return cache.count(10)
if __name__=='__main__':
    print(e134())
