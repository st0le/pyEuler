from urllib2 import urlopen

score = lambda word : sum(ord(c) - 64 for c in word)

body = urlopen("https://projecteuler.net/project/resources/p022_names.txt").read()
print sum(score(word.strip("\"")) * (i+1) for i,word in enumerate(sorted(body.split(","))))
	

