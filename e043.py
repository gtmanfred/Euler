from itertools import permutations
def Euler_43():
    perms = ["".join(x) for x in permutations('0123456789',10)]
    ret = 0
    print('start')
    for x in perms:
        test = True
        x = int(x)
        xstr = str(x)
        if xstr[5]=='5':
            d2 = int(xstr[1:4])%2
            d3 = int(xstr[2:5])%3
            d4 = int(xstr[3:6])%5
            d5 = int(xstr[4:7])%7
            d6 = int(xstr[5:8])%11
            d7 = int(xstr[6:9])%13
            d8 = int(xstr[7:10])%17
            if d2==0 and d3==0 and d4==0 and d5==0 and d6==0 and d7==0 and d8==0:
                ret+=x
                print(ret)
        if x ==1406357289:print(ret);print(d2,d3,d4,d5,d6,d7,d8)
    return ret

if __name__=='__main__':
    print(Euler_43())
