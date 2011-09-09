from random import randint
from fractions import gcd
from math import ceil
import math, time
def isprime(n):
    if type(n)==str:
        n = int(n)
    if n in (1,0):
        return False
    elif n<4:
        return True
    elif not n&1:
        return False
    elif n<9:
        return True
    elif not n%3:
        return False
    else:
        r=int(math.sqrt(n))
        f = 5
        while f<=r:
            if not n%f:
                return False
            if not n%(f+2):
                return False
            f = f+6
        return True

def isprime2(number):
    start=time.clock()
    fnum = [1,]
    last = int(math.ceil(math.sqrt(number)))
    for p in range(2, last + 1):
        if (number % p) == 0:
            return False
            fnum.append(p)
            fnum.append(number / p)
    # Remove duplicates, sort list
    fnum = list(set(fnum))
    fnum.sort()
    end=time.clock()
    if len(fnum) > 1:     
        return False
    else:
        return True
'''
print "Prime or factor calculator v3 using sqrt(n)"
print #

num =int(raw_input("Enter number: "))

print isprime(num)
'''
def isprime1(number):
    if number<=1:
        return False
    check=2
    maxneeded=number
    while check<maxneeded+1:
        maxneeded=number/check
        if number%check==0:
            return False
        check+=1
    return True


 
def test(n):
    k = ceil(n*3/4)
    it = 0
    while True:
        try:
            return miller(n,k)
        except:
            it+=1
            if it>n**.5:
                return True
def miller(n, k): #miller_rabin
  if n < 5:
    if n in [2, 3]:
      return True
    else:
      return False
 
  s = 0
  d = n - 1
  while d % 2 == 0:
    d = d / 2
    s = s + 1
 
  def not_witness(a):
    x = pow(a, d, n)
    if x == 1:
      return True
    for r in range(s):
      if x == n - 1:
        return True
      x = pow(x, 2, n)
    return False
 
  for i in range(k):
    a = randint(2, n - 2)
    if gcd(a, n) != 1:
      return False
    if not not_witness(a):
      return False
 
  return True
