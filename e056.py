import maths
def Euler_56(n = 100):
    alist = [a**b for a in range(100) for b in range(100)]
    print(len(alist))
    Max = 0
    for i in range(len(alist)):
        a = maths.sumdigs(alist[i])
        if a>Max:Max = a
    return Max
if __name__=='__main__':
    print(Euler_56())
