#Euler Utilities

def fib(limit=None):
	a,b = 0,1
	while True:
		if limit != None and a > limit : break
		yield a
		a,b = b,a+b

def prime_factors(n):
	if n % 2 == 0:
		c = 0
		while n % 2 == 0:
			n /= 2
			c += 1
		yield 2,c
	f = 3
	while n > 1:
		c = 0
		if n % f == 0:
			while n % f == 0:
				c += 1
				n /= f
			yield f,c
		f += 2

def is_palindrome(n):
	s = str(n)
	return s == s[::-1]
	
def gcd(a,b):
	while b:
		a,b = b,a%b
	return a
	
def lcm(a,b):
	return (a*b)/gcd(a,b)
	
def primes(limit=None):
	