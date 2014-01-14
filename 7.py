#Project Euler 7
#http://projecteuler.net/problem=7

from utils import *

def solve():
	R = range(101)
	return sum(R)**2 - sum(map(lambda n:n**2,R))

print "Solution #7 :",solve()