from math import *
from maths import isprime2 as isPrime
from time import *
def hform(prime_list, exp_list, lim, bound, count, hcount):
    for element in range(exp_list[count-1]+1):
        lim[count-1] = element              # List to carry exponents
        num = 1
        for x in range(len(prime_list)):    # Determine size of number
            num = num*(prime_list[len(prime_list)-1-x]**lim[len(prime_list)-1-x])
            if num > bound: break
        if count != len(prime_list):        # Only add to hcount at end of list
            count += 1
            hcount = hform(prime_list, exp_list, lim, bound, count, hcount)
            count -= 1  
        elif num > bound: break             # Need to break loop if number too large
        else:
            hcount += 1                     # Continue to count the Hamming numbers
            if hcount % 10000 == 0: print(hcount, lim, clock())
    return hcount                           # Return the last calculated Hamming Number

def hamming(smooth,power):

    bound = 10**power

    prime_list = []                         # Generate the prime numbers
    for i in range(smooth+1):
        if isPrime(i):
            prime_list.append(i)
            
    prime_list.reverse()                    # Speeds up calculation

    exp_list = []                           # Determine the maximum exponents can be
    for prime in prime_list:
        exp_list.append(int(log(bound)/log(prime)))
    #print(exp_list

    hcount, count = 0, 1
    lim = [0]*len(prime_list)               # List to carry exponents
    final = hform(prime_list, exp_list, lim, bound, count, hcount)
    
    print('\nThere are %s Hamming numbers of type %s not exceeding 10^%s' % (final, smooth, power))
    print('\tFound in %s seconds' % clock())
    print('\tThere are %s Primes that include: %s' % (len(prime_list),prime_list))
    print('\tThe calculated Exponent limits: %s\n' % exp_list)

if __name__ == '__main__':

    #hamming(5,8) # 1105, 0.01s
    hamming(100,9)
    
# limits - [4, 4, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 5, 6, 6, 6, 7, 7, 8, 8, 10, 12, 18, 29]
# 358275 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 3, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0] 
# 360855 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0]
# 429858 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 2, 1, 2, 0, 0, 0, 0, 0, 0, 0, 0]
