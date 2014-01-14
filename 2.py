#Project Euler 2
#http://projecteuler.net/problem=2

from utils import *

def solve():
	return sum(f for f in fib(4000000) if f % 2 == 0)

print "Solution #2 :",solve()