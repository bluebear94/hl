import io
import re

kls = [set() for i in range(0, 9)]
t = re.compile(" G(\d+)")

def rd(p):
	f = open(p, "r")
	for l in f:
		c = l[0]
		r = 8
		if c != '#':
			m = t.search(l)
			if m:
				s = int(m.group(1))
				r = [0, 1, 2, 3, 4, 5, 9, 6, 7, 7][s - 1]
			kls[r].add(c)
	f.close()

def wd(p):
	f = open(p, "w")
	for kl in kls:
		for k in kl:
			f.write(k)
		f.write('\n')
	f.close()

rd("kanjidic-utf8.txt")
wd("kls.txt")