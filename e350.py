from script.maths import mulgcd as gcd,mullcm as lcm
from itertools import permutations as combos#combinations_with_replacement as combos
def e350():
    G = 10
    L = 100
    N=2
    return f(G,L,N)

def f(g,l,n):
    count = 0
    for combo in combos(range(1,l+1),n):
        if g<=gcd(combo) and l>=lcm(combo):
            count +=1
    return count

if __name__=='__main__':
    print(e350())
