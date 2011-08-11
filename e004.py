from script.maths import ispal
def e004(d=3):
    pals = []
    tmp = list(range(999,100,-1))
    for i,x in enumerate(tmp):
        for y in tmp[i:]:
            if ispal(x*y):pals+=[x*y]
    return max(pals)

def oneline():
    return max([x*y for x in range(999,99,-1) for y in range(999,99,-1) if ispal(x*y)])

def Euler_4(d=3):
    n = 10**d
    n2 =n//10 
    n = n-1
    ans = 0 
    for i in range(n2,n):
        for j in range(n2,n):
            if ispal(i*j):
                if ans<i*j:
                    ans = i*j
    return ans

def ispal1(num):
    num = str(num)
    while len(num)>1:
        if num[0] is not num[len(num)-1]:
            return False
        num = num[1:len(num)-1]
    return True


if __name__=='__main__':
    print(e004())
    #print(Euler_4())
