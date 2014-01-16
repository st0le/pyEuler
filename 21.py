#Project Euler 21
#http://projecteuler.net/problem=21

from utils import *
import operator as op

def solve():
    lst = map(lambda n : sdiv(n) - n, xrange(10001))
    s = 0
    for i in xrange(10001):
        if lst[i] < 10001 and i < lst[i] and lst[lst[i]] == i:
            s += i + lst[i]
    return s
    
print "Solution #21 :",solve()
