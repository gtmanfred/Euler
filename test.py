from e341 import g
try:
    r = 1
    gns = [1,2,2]
    i = 3
    tot = t =0
    b = True
    while t!=0 or b:
        if len(gns)>=10**8:break
        gns+=[i]*gns[i-1]
        t += gns[i-1]-g(i)
        if t == 0:print(i);b = True
        else:b = False
        i+=1
    '''
    for i in range(1,100001):
        if gns[i-1]!=g(i):
            print(i,gns[i-1],g(i))
            t+=gns[i-1]-g(i)
            tot+=1
    '''
except:print(i,t)
