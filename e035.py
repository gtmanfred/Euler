from script.isprime import isprime
from script.allsieve import soegen
def Euler_35(num=10**6):
    i = 0
    for x in soegen(num):
        b = True
        y = str(x)
        if evendig(y):continue
        yn = rotatestr(y)
        while yn!=y:
            b = isprime(int(yn))
            if not b:break
            yn = rotatestr(yn)
        if b:
            i+=1
    return i
def evendig(n):
    if n=='2':return False
    return any(not int(x)&1 for x in n)
def rotatestr(num):
    if len(num)<2:
        return num 
    ret = num[1:]+num[0]
    return ret

if __name__=='__main__':
    print(Euler_35())
