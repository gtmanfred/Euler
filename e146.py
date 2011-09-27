from script.maths import nextprime,isprime2
def e146(top = 10**6):
    ret = 0
    x1 = lambda n:n**2+1
    x2 = lambda n:n**2+3
    x3 = lambda n:n**2+7
    x4 = lambda n:n**2+9
    x5 = lambda n:n**2+13
    x6 = lambda n:n**2+27
    test = [x1,x2,x3,x4,x5,x6];
    mini = 1000
    for i in range(1,top+1):
        if i>mini:
            print(i)
            mini+=1000
        z = 0
        yesno = i
        for j in test:
            y = j(i)
            if z:
                if y!=z:
                    yesno = 0
                    break
            if not isprime2(y):continue
            z = nextprime(y)
        ret +=yesno
    return ret
if __name__=='__main__':
    print(e146())
