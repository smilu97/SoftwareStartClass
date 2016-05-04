import time

strNotStrawberry = ' '
strStrawberry = 'S'

def problemDescription() :
	print '''
	************************
	I Like Strawberries
	Author: Kim YoungJin
	ID: 2016025241
	************************
	'''
waitTime = 0.1

def strawberry_when4under(val) :
	for i in range(4-val) :
		print strNotStrawberry,
		time.sleep(waitTime)
	for i in range(val) :
		print strStrawberry,
		time.sleep(waitTime);
	print
def strawberry_when4over(val) :
	for i in range(4) :
		print strStrawberry,
		time.sleep(waitTime)
	for i in range(8-val) :
		print strNotStrawberry,
		time.sleep(waitTime)
	for i in range(val-4) :
		print strStrawberry,
		time.sleep(waitTime)
	print

def sayBerry(val) :
	if val <= 4 :
		strawberry_when4under(val)		
	elif 4 < val :
		strawberry_when4over(val)

def DoStrawberry() :
	count = 0
	while count < 30 :
		for i in range(1, 8) :
			sayBerry(i)
			count += 1
		for i in range(8, 1, -1) :
			sayBerry(i)
			count += 1

def __main__() :
	problemDescription()
	DoStrawberry()

if __name__ == '__main__' :
	__main__()