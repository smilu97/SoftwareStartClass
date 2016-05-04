from math import *

def next(x) :
	return x + (3*cos(x) - x - 1) / (3*sin(x) + 1)

def f(x) :
	return 3*cos(x) - x - 1

val = -3
for i in range(10) :
	print val
	val = next(val)
print f(val)