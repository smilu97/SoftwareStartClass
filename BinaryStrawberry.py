import time

strStrawberry = 'S'
strNotStrawberry = '.'
waitTime = 0.1

def BinaryStrawberry(val) :
	for i in range(3,-1,-1) :
		if val & (1 << i) :
			print strStrawberry,
		else :
			print strNotStrawberry,
		time.sleep(waitTime)
	print

def DoBinaryStrawberry() :
	while True :
		for i in range(1, 15) :
			BinaryStrawberry(i)
		for i in range(15, 1, -1) :
			BinaryStrawberry(i)

def __main__() :
	DoBinaryStrawberry()

if __name__ == '__main__' :
	__main__()