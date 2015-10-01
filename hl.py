import io
import sys
import unicodedata

kls = [set() for i in range(0, 9)]

def rd(p):
	f = open(p, "r")
	r = 0
	for l in f:
		for c in l:
			kls[r].add(c)
		r += 1
	f.close()

def cl(c):
	if not unicodedata.name(c, "CJK UNIFIED IDEOGRAPH").startswith("CJK UNIFIED IDEOGRAPH"):
		return -1
	for i in range(0, 9):
		if c in kls[i]: return i
	return 9

def oht(s):
	o = ""
	r = -1
	def f():
		nonlocal o
		if (r != -1):
			print(end = '<span class="k{0}">'.format(r + 1))
		print(end = o)
		if (r != -1):
			print(end = "</span>")
		o = ""
	for l in s:
		for c in l:
			if c == '\n': continue
			nr = cl(c)
			if r != nr: f()
			r = nr
			o += c
		f()
		r = -1
		print("<br>")

rd("kls.txt")
print('<html><head><link rel="stylesheet" type="text/css" href="ds.css"></head><body>')
oht(sys.stdin)
print('</body></html>')