'''
n**3+n**2*p=k**3
n+p = k**3/n**2
m**3+p = k**3/m**6
(m+1)**3 = k**3/m**6
'''
from script.maths import isprime2
def e131(top = 10**6):
    i = 1
    j = 2
    count = 0
    while True:
        p = j**3-i**3
        if p>=top:break
        if isprime2(p):count+=1
        i,j = j,j+1
    return count
if __name__=='__main__':
    print(e131(10**9))
