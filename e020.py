import maths
from maths import fact
def e020(num=100):
    return sum([int(i) for i in str(fact(num))])

def Euler_20(num = 100):
    f = maths.fact(100)
    ret = maths.sumdigs(f)
    return ret

if __name__=='__main__':
    print(e020())
    #print(Euler_20())
