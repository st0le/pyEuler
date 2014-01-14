#Project Euler 1
#http://projecteuler.net/problem=1

def solve():
	return sum(i for i in xrange(1000) if i % 3 == 0 or i % 5 == 0)
	
print "Solution #1 :",solve()