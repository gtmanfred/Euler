from memorize import memo
def e014(num=10**6):
    maxlen = 1
    for i in range(1,num+1):
        length = chainrec(i)
        if length>maxlen:maxlen=length;maxi=i
    return maxi
@memo
def chainrec(num=13):
    if num==1:
        return 1
    else:
        if num%2:
            return 1+chainrec(3*num+1)
        else:
            return 1+chainrec(num//2)
def Euler_14(num=10**6):
    maxlen=1
    for i in range(num//2,num):
        print(i/num,end='\r')
        a=chainlen(i)
        if a>maxlen:
            maxlen,j=a,i
        if i ==num//4*3:
            print(i)
    return j

def chainlen(num=13):
    length=1
    while num != 1:
        num=3*num+1 if num%2 else num//2
        length+=1
    return length

if __name__=='__main__':
    print(e014())
    #print(Euler_14()) really slow, other is 20 seconds(netbook)
