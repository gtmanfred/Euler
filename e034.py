import maths

def Euler_34():
    ret = 0
    for i in range(3, 100000):
        if i ==sumdigfacts(i):
            print(i)
            ret+=i
    return ret


def sumdigfacts(num):
    num = str(num)
    return sum(list(maths.fact(int(x)) for x in num))

if __name__=='__main__':
    print(Euler_34())
