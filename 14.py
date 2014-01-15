#Project Euler 14
#http://projecteuler.net/problem=14

from utils import *

cache = {0:0,1:1}
def collatz(n):
	try:
		return cache[n]
	except :
		cache[n] = c = 1 + collatz(n/2 if n %2 == 0 else 3*n+1)
		return c

def solve():
	return max( (collatz(i), i) for i in xrange(1000000,-1,-1) )

print "Solution #14 :",solve()
