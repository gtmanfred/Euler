class Primes:
	''' This class provides numerous functions for prime numbers
	'''

	def __init__(self, num=0):
		self.maxPrime = 0
		self.pSieve2 = []
		self.plist = []
		self.default = num
		return

	def sieve(self, num=-1):
		''' Create a data structure with all the primes up to num
			The data structure that stores this is internal and
			subject to change
		'''
		if num is -1:
			num = self.default
		if self.maxPrime >= num:
			return
		oldMax, self.maxPrime = self.maxPrime, num
		listEnd = self.maxPrime//2
		if oldMax is 0:
			self.pSieve2 = [True for i in range(0, listEnd+1)]
			self.pSieve2[0] = False # set 1 as not prime
		else:
			self.pSieve2.extend([True for i in range(oldMax//2, listEnd+1)])
			print(len(self.pSieve2))
		for ind in range(1,listEnd):
			lowVal = 2 * (ind**2 + ind)
			if lowVal > listEnd:
				break
			if self.pSieve2[ind] is True:
				while lowVal <= oldMax//2:
					lowVal += 2*ind + 1
				for x in range(lowVal, listEnd+1, 2*ind + 1):
					self.pSieve2[x] = False
		return

	def pList(self, num=-1,minval=0):
		''' Generate a list of prime numbers
		'''
		if num is -1:
			num = self.default
		if self.maxPrime < num:
			self.sieve(num)
		if len(self.plist) is 0:
			self.plist.append(2)
			self.plist.append(3)
			lowVal = 7
		else:
			lowVal = 6 * (self.plist[-1]//6) + 7
			if lowVal-2 == self.plist[-1]:
				if self.isPrime(lowVal):
					self.plist.append(lowVal)
				lowVal += 6
		for x in range(lowVal, num+1, 6):
			if self.isPrime(x-2):
				self.plist.append(x-2)
			if self.isPrime(x):
				self.plist.append(x)
		for x in range(self.plist[-1]+1, num+1, 1):
			if self.isPrime(x):
				self.plist.append(x)
		if minval:bot=self.plist.index(minval)
		else:bot = 0
		return self.plist[bot:]

	def isPrime(self,num):
		''' Test if a single input number is prime
		'''
		if type(num)==type('str'):num = int(num)
		if num <= self.maxPrime:
			if num % 2 is 0:
				return True if num is 2 else False
			if num <= self.maxPrime:
				return self.pSieve2[num//2]
		if num < 10:
			if num < 2:
				return False
			if num < 4:
				return True
			if num % 2 is 0:
				return False
			if num < 9:
				return True
			return False
		if num % 2 is 0:
			return False
		if num % 3 is 0:
			return False
		if num % 5 is 0:
			return False
		tmp = 7
		while tmp**2 <= num:
			if num % tmp is 0:
				return False
			tmp += 4
			if num % tmp is 0:
				return False
			tmp += 2
			if num % tmp is 0:
				return False
			tmp += 4
			if num % tmp is 0:
				return False
			tmp += 2
			if num % tmp is 0:
				return False
			tmp += 4
			if num % tmp is 0:
				return False
			tmp += 6
			if num % tmp is 0:
				return False
			tmp += 2
			if num % tmp is 0:
				return False
			tmp += 6
		return True

class PosPrimes:
	''' Iterator that returns only possible primes using wheel factorization
		far too slow
	'''

	def __init__(self, num=float('inf')):
		self.maxVal = num
		return

	def __iter__(self):
		# (1, 7, 11, 13, 17, 19, 23, 29)
		self.difflist = (4, 2, 4, 2, 4, 6, 2, 6)
		self.initial = (2, 3, 5, 7)
		self.current = 0
		self.diffpoint = 0
		return self

	def __next__(self):
		if self.current < self.initial[-1]:
			if self.current is 0:
				self.current = self.initial[0]
			else:
				self.current = self.initial[self.initial.index(self.current)+1]
			if self.current > self.maxVal:
				raise StopIteration
			return self.current
		self.current += self.difflist[self.diffpoint]
		self.diffpoint = (self.diffpoint + 1) % len(self.difflist)
		if self.current > self.maxVal:
			raise StopIteration
		return self.current


class PrimesIter:

	def __init__(self, max):
		self.max = max

	def __iter__(self):
		self.plist = [2]
		self.first = True
		return self

	def __next__(self):
		if self.first:
			self.first = False
			return self.plist[0]
		for tmp in range(self.plist[-1] + 1, self.max):
			for prime in self.plist:
				if prime**2 > tmp:
					self.plist.append(tmp)
					return tmp
				if tmp%prime is 0:
					break
		raise StopIteration
