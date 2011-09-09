from script import maths

def Euler_36(num=10**6):
    count = 0
    for x in range(num):
        if x ==num//2:print(x)
        b = bin(x)
        if maths.ispal(int(b[2:])) and maths.ispal(x):
            count+=x
    return count
def ispal(n):
    ns = str(n)
    mid = len(ns)//2
    if ns[:mid]==ns[-mid:][-1::-1]:return True
    else:return False


if __name__=='__main__':
    print(Euler_36())
