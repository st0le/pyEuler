#Project Euler 17
#http://projecteuler.net/problem=17

from utils import *

def spell_number(n):

	data = {0:'', 1:'one',2:'two',3:'three',4:'four',5:'five',6:'six',7:'seven',8:'eight',9:'nine',10:'ten',11:'eleven',12:'twelve',13:'thirteen',
			14:'fourteen',15:'fifteen',16:'sixteen',17:'seventeen',18:'eighteen',19:'nineteen',20:'twenty',30:'thirty',40:'forty',50:'fifty',60:'sixty',
			70:'seventy',80:'eighty',90:'ninety'}
	bases = {2:'hundred',3:'thousand',6:'million'}
	if n == 0: return 'zero'
	def spell_it(n):
		if n in data:
			return data[n]
		elif n < 100:
			return "%s %s" % (data[n - n % 10], data[n % 10])
		else:
			for b in sorted(bases,reverse=True):
				if n >= 10**b:
					if n % 10**b == 0:
						return "%s %s" % (spell_it(n / 10**b), bases[b])
					else:
						return "%s %s and %s" % (spell_it(n / 10**b), bases[b], spell_it(n % 10**b))
			return None
	return spell_it(n)

def solve():	
	return len(''.join (map(spell_number,xrange(1,1001))).replace(' ',''))


print "Solution #17 :",solve()
