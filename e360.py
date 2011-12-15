def e360(num=45):
    ret = 0
    for x in range(num+1):
        print(x,end='\r')
        for y in range(num+1):
            tmp = num**2-x**2-y**2
            if tmp<0:
                break
            z=int(tmp**.5)
            if x**2+y**2+z**2==num**2:
                print(x,y,z)
                ret+=test3(x,y,z)
    return ret
def test3(x,y,z):
    tmp = [x,y,z]
    if all(i!=0 for i in tmp):
        return 8*sum(tmp)
    elif tmp.count(0)==1:
        return 4*sum(tmp)
    elif tmp.count(0)==2:
        return 2*sum(tmp)
if __name__=="__main__":
    print(e360(10**10))
