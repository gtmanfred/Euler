primes = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79]
def Euler_77(): 
    target = 11
    while True:
        ways = [1] + [0]*target
        for i in primes:
            for j in range(i, target+1):
                ways[j] += ways[j-i]
        if ways[target] > 5000: break
        target += 1;
    return target
if __name__=='__main__':
    print(Euler_77())
