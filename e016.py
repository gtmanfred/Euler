def Euler_16(dig=2,exp=1000):
    var = sums(str(dig**exp))
    '''
    ret =int(var[-1]) 
    while len(var)>1:
        var = var[:-1] 
        print(len(var))
        ret+=int(var[-1])
    ret+=int(var[0])
    '''
    return var
def sums(num):
    ret=0
    for i in range(len(num)):
        ret+=int(num[i])
    return ret

if __name__=='__main__':
    print(Euler_16())
