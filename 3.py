#Project Euler 3
#http://projecteuler.net/problem=3

from utils import *

def solve():
	return max(prime_factors(600851475143))[0]

print "Solution #3 :",solve()