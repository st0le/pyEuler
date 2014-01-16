#Project Euler 20
#http://projecteuler.net/problem=20

from utils import *
import operator as op

def solve():
    return sum(map(int,str(reduce(op.mul,xrange(1,101),1))))
    
print "Solution #20 :",solve()
