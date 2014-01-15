#Project Euler 12
#http://projecteuler.net/problem=12

from utils import *
import operator as op

def solve():
	a = 0
	while True:
		if a % 2 == 0:
			cnt = ndiv(a/2) * ndiv(a+1)
		else:
			cnt = ndiv(a) * ndiv((a+1)/2)
		if cnt > 500:
			return ( a * (a+1) ) / 2
			break
		a += 1
	return None

print "Solution #12 :",solve()