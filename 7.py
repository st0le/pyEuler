#Project Euler 7
#http://projecteuler.net/problem=7

from utils import *

def solve():
	return filter(is_prime,xrange(150000))[10000]

print "Solution #7 :",solve()