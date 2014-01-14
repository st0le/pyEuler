#Project Euler 9
#http://projecteuler.net/problem=9

from utils import *
import operator as op

def solve():
	return reduce(op.mul,[(a,b,1000-a-b) for a in xrange(1,1000) for b in xrange(a,1000) if a*a + b*b == (1000-a-b)**2][0])

print "Solution #9 :",solve()