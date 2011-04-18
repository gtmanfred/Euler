import maths

def Euler_36(num=10**6):
    count = 0
    for x in range(num):
        if x ==num//2:print(x)
        b = bin(x)
        if maths.ispal(int(b[2:])) and maths.ispal(x):
            count+=x
    return count

if __name__=='__main__':
    print(Euler_36())
