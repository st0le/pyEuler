#Project Euler 4
#http://projecteuler.net/problem=4

from utils import *
import itertools as it

def solve():
	return max(filter(is_palindrome,map(lambda (a,b):a*b,it.product(range(1000),repeat=2))))

print "Solution #4 :",solve()