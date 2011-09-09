from script import maths
Max = 28123
abund = [x for x in range(10,Max) if sum(maths.all_factors(x))>x+x]
abundict=dict.fromkeys(abund,1)

def Euler_23():
    tot = 0
    for i in range(1,Max):
        sums = 1
        for j in abund:
            if j>i:break
            if abundict.get(i-j):
                sums=0 
                break
        if sums:
            tot+=i
    return tot

if __name__=='__main__':
    print(Euler_23())
