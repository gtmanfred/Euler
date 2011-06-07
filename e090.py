from itertools import combinations
def e90():
    atup = combinations('0123456789',6)
    alist = []
    tmp = [str(i**2) for i in range(1,10)]
    for i in range(len(tmp)):
        if len(tmp[i])==1:tmp[i]='0'+tmp[i]
    sqrs = set(i for i in tmp)
    alist =[''.join(i) for i in atup]
    count = 0
    for x in range(len(alist)):
        i = alist[x]
        if '6' in i and not '9' in i:i+='9'
        elif '9' in i and not '6' in i:i+='6'
        for j in alist[x:]:
            test = set()
            if '6' in j and not '9' in j:j+='9'
            elif '9' in j and not '6' in j:j+='6'
            for ki in i:
                for kj in j:
                    test.update([ki+kj,kj+ki])
            if sqrs.issubset(test):count+=1
    return count

if __name__=='__main__':
    print(e90())
