from maths import ispal
def Euler_55(d = 10000):
    tot = 0
    for i in range(1,d):
        x = i
        for j in range(1,51):
            x = str(x)
            xb = ''.join(x[y] for y in range(len(x)-1,-1,-1))
            t = int(x)+int(xb) 
            if ispal(t):break
            else:x = t
            if j == 50:tot+=1
    return tot

if __name__=='__main__':
    print(Euler_55())
