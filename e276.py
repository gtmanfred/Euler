from script.maths import gcd
def e276(top = 10**7):
    count = 0
    for i in range(1,top):
        print(i)
        for j in range(1,top):
            if i+j>top:break
            for k in range(j-i+1,j+i+1):
                if i+j+k>top:break
                x = gcd(gcd(i,j),gcd(i,k))
                if x%1==0:count +=1
    return count

if __name__=='__main__':
    print(e276())
