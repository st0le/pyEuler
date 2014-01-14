#Project Euler 5
#http://projecteuler.net/problem=5

from utils import *

def solve():
	return reduce(lcm,range(1,20))

print "Solution #5 :",solve()