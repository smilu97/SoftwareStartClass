__author__ = 'Kim Young Jin'

def problemDescription() :
	print '*'*30
	print '369 Multiplication Table'
	print 'Author : ' + __author__
	print 'ID : 2016025241'
	print '*'*30
	print ''
	
def clapDetector(n) :
	val = n
	count = 0
	while val != 0 :
		first = val % 10
		if first == 3 or first == 6 or first == 9 :
			count += 1
		val /= 10
	if count == 0 :
		return n
	else :
		return 'clap'*count

def getIntInput() :
	while True :
		excepted = False
		try :
			val = int(raw_input('Input the number(1~30): '))
		except :
			print 'Input error.'
			excepted = True
		if excepted == False :
			if 1 <= val and val <= 30 :
				return val;
			print 'Input error.'

if __name__ == '__main__' :
	problemDescription()
	dan = getIntInput()
	print '*'*14 + str(dan) + 'dan' + '*'*14
	for i in range(1,10) :
		print '%4s * %4s = %4s' % (str(clapDetector(dan)), str(clapDetector(i)), str(clapDetector(dan*i)))
