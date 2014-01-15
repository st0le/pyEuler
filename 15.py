#Project Euler 15
#http://projecteuler.net/problem=15

from utils import *



def solve():
	cache = {}
	def ways(x,y):
		if (x,y) in cache: return cache[(x,y)]
		if x == 0 or y == 0:
			return 1
		else:
			cache[(x,y)] = r  = ways(x - 1, y) + ways(x, y - 1)
			return r

	return ways(20,20)

print "Solution #15 :",solve()
