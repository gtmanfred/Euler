import maths

def Euler_20(num = 100):
    f = maths.fact(100)
    ret = maths.sumdigs(f)
    return ret

if __name__=='__main__':
    print(Euler_20())
