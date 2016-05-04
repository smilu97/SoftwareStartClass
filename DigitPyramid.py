import sys

__author__ = 'Kim young jin'
__ID__ = '2016025241'

def printDescription() :
	print '*'*30
	print 'Digit Pyramid'
	print 'Author: ' + __author__
	print 'ID: ' + __ID__
	print '*'*30

class PyramidDrawer :
	def __init__(self) :
		self.CONST_PYRAMID_HEIGHT_MIN = 1
		self.CONST_PYRAMID_HEIGHT_MAX = 20

	def printPyramid(self, height) :
		print 
		for line in range(height) :
			blanknum = height - line - 1
			blankstr = '  '*blanknum
			sys.stdout.write(blankstr)
			for i in [val%10 for val in range(line+1)] :
				print i,
			for i in range(line-1, -1, -1) :
				print (i%10),
			print
	def getHeightInput(self, message, errmsg) :
		while True :
			try :
				buf = int(raw_input(message))
			except :
				print errmsg
				continue;
			if  self.CONST_PYRAMID_HEIGHT_MIN <= buf and buf <= self.CONST_PYRAMID_HEIGHT_MAX :
				return buf
			else :
				print errmsg

def __main__() :
	printDescription()
	drawer = PyramidDrawer()
	drawer.printPyramid(drawer.getHeightInput('Input the height: ', 'Input Error!'))
	
if __name__ == '__main__' :
	__main__()