from maths import pandigs, isprime2
def Euler_49():
    r = {}
    ret = []
    for nums in range(1000,10000):
        pans = pandigs(str(nums),4)
        itr = [x for x in pans if isprime2(int(x)) and x.find('0')!=0]
        for i in itr:
            for j in itr:
                if j!=i:
                    for k in itr:
                        if k!=i and k!=j:
                            if int(k)-int(j)==int(j)-int(i) and not r.get(i) and not r.get(j) and not r.get(k):
                                r[i] = 1
                                ret += [i+j+k]
                                if len(ret)>1:
                                    return ret
    return ret

def rotatestr(num):
    if len(num)<2:
        return int(num)
    ret = num[1:]+num[0]
    return ret


if __name__=='__main__':
    print(Euler_49())
