#Euler Utilities

def fib(limit=None):
	a,b = 0,1
	while True:
		if limit != None and a > limit : break
		yield a
		a,b = b,a+b

def prime_factors(n):
	if n == 0 : return 
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
	
def is_prime(n):
	if n <= 3 or n % 2 == 0 or n % 3 == 0 : return n == 2 or n == 3
	for i in xrange(5,int(n**.5) + 1,6):
		if n % i == 0 or n % (i + 2) == 0 : return False
	return True

def ndiv(n):
	cnt = 1
	for pf,c in prime_factors(n):
		cnt *= (c + 1)
	return cnt

def sdiv(n):
    if n == 0: return 0
    s = 1
    for pf,c in prime_factors(n):
        s *= (pf**(c+1) - 1) / (pf - 1)
    return s