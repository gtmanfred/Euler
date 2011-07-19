#This is a problem from the Project Euler Website
# http://projecteuler.net/

# Euler Problem #204
#
# Problem:  How many generalised Hamming numbers of type 100 are there
#           which don't exceed 10^9?
#
# Hint:     A Hamming number is a positive number which has no prime factor
#           larger than 5.  So the first few Hamming numbers are
#           1, 2, 3, 4, 5, 6, 8, 9, 10, 12, 15.
#
#           There are 1105 Hamming numbers not exceeding 10^8.
#
#           We will call a positive number a generalised Hamming number of
#           type n, if it has no prime factor larger than n. Hence the Hamming
#           numbers are the generalised Hamming numbers of type 5.
#
# Written by Chris Gilmer
# Solved:   
# Answer:   
#
# Notes:

from isprime import isprime as isPrime
from math import *
from time import *
from allsieve import sieveOfEratosthenes as sieve

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
            if hcount % 10000 == 0: print hcount, lim, clock()
    return hcount                           # Return the last calculated Hamming Number

def hamming(smooth,power):

    bound = 10**power
    '''
    prime_list = []                         # Generate the prime numbers
    for i in range(smooth+1):
        if isPrime(i):
            prime_list.append(i)
    '''
    prime_list = sieve(smooth+1)
            
    prime_list.reverse()                    # Speeds up calculation
    exp_list = []                           # Determine the maximum exponents can be
    for prime in prime_list:
        exp_list.append(int(log(bound)/log(prime)))
    print exp_list

    hcount, count = 0, 1
    lim = [0]*len(prime_list)               # List to carry exponents
    final = hform(prime_list, exp_list, lim, bound, count, hcount)
    
    print '\nThere are %s Hamming numbers of type %s not exceeding 10^%s' % (final, smooth, power)
    print '\tFound in %s seconds' % clock()
    print '\tThere are %s Primes that include: %s' % (len(prime_list),prime_list)
    print '\tThe calculated Exponent limits: %s\n' % exp_list

if __name__ == '__main__':

    hamming(5,8) # 1105, 0.01s
    hamming(100,9)
75	    
76	# limits - [4, 4, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 5, 6, 6, 6, 7, 7, 8, 8, 10, 12, 18, 29]
77	# 358275 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 3, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0] 
78	# 360855 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0]
79	# 429858 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 2, 1, 2, 0, 0, 0, 0, 0, 0, 0, 0]
