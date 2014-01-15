#Project Euler 16
#http://projecteuler.net/problem=16

from utils import *



def solve():
	return sum(map(int,str(2**1000)))

print "Solution #16 :",solve()
