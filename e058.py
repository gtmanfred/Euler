#from script.maths import isprime2
from script.isprime import isprime as isprime2

def Euler_58():
    width, diag,inc, base,prime = 3,1,2,4,0
    mini = 100
    while 1:
        if base>mini:
            print(prime/(base//4+1),end='\r');mini+=100
        #print(prime/(base//4+1),end='\r');mini+=100
        for i in range(0,4):
            diag +=inc
            if isprime2(diag):prime+=1
        p = prime*10
        base = base+4
        if p<base:
            return width
        width +=2
        inc = width-1


if __name__=='__main__':
    print(Euler_58())
