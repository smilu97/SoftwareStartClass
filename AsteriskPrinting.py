import sys
__author__ = 'Kim Young Jin'

def problemDescription() :
	print '*'*30
	print 'Name : Asterisk Printing'
	print 'author : %s' % __author__
	print 'ID : 2016025241'
	print '*'*30

def lncr(hgt) :
	for i in range(1, hgt+1) :
		print '*' * i

def decr(hgt) :
	for line in range(1, hgt+1) :
		sys.stdout.write(' '*(hgt-line))
		print '*'*line
def circle(size) :
	size2 = size**2
	for y in range(size, -size-1, -1) :
		printed = False
		for x in range(-size, size+1) :
			x2y2 = x**2 + y**2
			if size2 - 4 <= x2y2 and x2y2 <= size2 + 4 :
				sys.stdout.write('*')
				printed = True
			else :
				sys.stdout.write(' ')
		if True :
			sys.stdout.write('\n')

if __name__ == '__main__' :
	problemDescription()
	val = int(raw_input('Height : '))
	lncr(val)
	decr(val)
	circle(val)