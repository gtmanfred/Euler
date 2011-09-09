from script.maths import ispan

def Euler_32():
    a = set()
    l = 0
    t = 0
    for x in range(1,100):
        if x%10==0:print(x)
        for y in range(x,2000):
            test = str(x)+str(y)+str(x*y)
            if len(test)==9:
                if ispan(test):a.add(x*y);t +=1
                length = len(a)
                if length>l:print(a);l = length
        if t==9:break
    print(a)
    ret = 0
    while a:
        ret+=a.pop()
    return ret
if __name__=='__main__':
    print(Euler_32())
