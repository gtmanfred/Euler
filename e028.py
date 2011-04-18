def Euler_28(num=1001):
    diag1 = 1
    diag2 = 0
    for x in range(3,num+1,2):
        diag1 += x**2
        diag2 += x**2-x+1
        diag1 += x**2-2*x+2
        diag2 += x**2-3*x+3
    ret = diag1+diag2
    return ret

if __name__=='__main__':
    print(Euler_28())
