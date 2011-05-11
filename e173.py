from time import time
t = time()
def e173(top = 10**6):
    tt = t
    count =0
    countodd=0
    counteven=0
    print(top//4+2)
    for i in range(3,top//4+2):
        if i%10**3==0:f = time();print(i,f-tt,f-t);tt=f
        if i%2:
            for j in range(i-2,0,-2):
                if i**2-j**2<=top:countodd+=1
                else:break
        else:
            for j in range(i-2,1,-2):
                if i**2-j**2<=top:counteven+=1
                else:break
        count = counteven+countodd
    return count

if __name__=='__main__':
    print(e173())
