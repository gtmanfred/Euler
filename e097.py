def Euler_97(a=28433,b=7830457,digs=10):
    return str((a*pow(2,b,10**digs)+1)%10**digs)

if __name__=='__main__':
    print(Euler_97())
