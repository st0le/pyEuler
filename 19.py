#Project Euler 19
#http://projecteuler.net/problem=19

from utils import *
import datetime

def solve():
    return len(filter(lambda dt : dt.weekday() == 6, [datetime.date(year=y,month=m,day=1) for y in xrange(1901,2001) for m in xrange(1,13)]))
    
print "Solution #19 :",solve()
