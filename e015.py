import maths
def Euler_15(i=20,j=20):
    ret = maths.fact(i+j)//maths.fact(i)//maths.fact(j)#binomial coefficients
    return ret


if __name__=='__main__':
    print(Euler_15())
