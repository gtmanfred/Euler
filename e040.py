def Euler_40(num = 1000000):
    alist = list(range(1,num//5))
    val = "1"
    i = 1
    while len(val)<=num:
        val = val+str(alist[i])
        i+=1 
    ret =int(val[0])*int(val[9])*int(val[99])*int(val[999])*int(val[9999])*int(val[99999])*int(val[999999])
    return ret


if __name__=='__main__':
    print(Euler_40())
