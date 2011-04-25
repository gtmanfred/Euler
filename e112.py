def Euler_112(perc = 99/100):
    bouncy = 0
    num = 99
    count = 0
    while bouncy<perc:
        num+=1
        tmp = [int(x) for x in str(num)]
        last = tmp[0]
        down = False
        up = False
        for i in tmp[1:]:
            if last>i:down = True
            if last<i:up = True
            last = i
        if up and down:count+=1
        bouncy = count/num
        if bouncy>.98:print(bouncy)
    return num

if __name__=='__main__':
    print(Euler_112())
