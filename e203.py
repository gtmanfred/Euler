from script.maths import *
def e203(top = 51):
    pasc = pascal()
    n = pasc[-1][len(pasc)//2-1]
    count = set()
    count2 = 0
    print('start')
    sqrs = [[],[4]]
    lastn = 0
    last2n = 0
    for i in range(len(pasc)):
        for j in range(len(pasc[i])):
            x = pasc[i][j]
            if i>1:
                print('i',i,'j',j,'x',x)
                sqrs = sqrfree(x,sqrs[1])
                if sqrs[0]:count.add(j);count2+=j
    return [sum(count),count2]

def sqrfree(n,sqrs = [4]):
    if n%4==0 or n%9==0 or n%25==0 or n%49==0 or n%121==0:return [False,sqrs]
    if n%13**2==0 or n%17**2==0 or n%19**2==0 or n%23**2==0 or n%29**2==0:return [False,sqrs]
    if n%31**2==0 or n%37**2==0 or n%41**2==0 or n%43**2==0 or n%47**2==0:return [False,sqrs]
    if len(sqrs) and sqrs[-1]>n//2+1:
        if n in sqrs:return [False,sqrs]
        else:
            for b in sqrs:
                if n%b==0:return [False,sqrs]
                else:return [True,sqrs]
    j = sqrs[-1]
    while j<n//2+1:
        sqrs +=[j]
        sqrs = sorted(sqrs)
        if sqrs[-1]>n:
            if n == j:return [False,sqrs]
            if n%j==0:return [False,sqrs]
            if j>n//2+1:return [True,sqrs]
        i = nextprime(int(pow(j,.5)))
        j = i**2
    return [True,sqrs]

def pascal():
    alist = [[1],[1,1],[1,2,1]]
    while len(alist)<51:
        alist.append([1])
        for i in range(len(alist[-2][1:])):
            alist[-1].append(alist[-2][i]+alist[-2][i+1])
        alist[-1].append(1)
    print(len(alist[-1]))
    print(len(alist[-1])/2)
    print(fact(51))
    return alist




if __name__=='__main__':
    print(e203())
