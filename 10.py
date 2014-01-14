#Project Euler 10
#http://projecteuler.net/problem=10

from utils import *

def solve():
	return sum(filter(is_prime,xrange(2000000)))

print "Solution #10 :",solve()