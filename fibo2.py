
__author__ = 'Kim Young Jin'
__ID__ = '2016025241'

fiboArray = [0, 1]
menuString = '*'*20+'\n1.Calculate\n2.Show it!\n3.Initialize\n4.Quit\n'+'*'*20

if __name__ == '__main__' :
	while True :
		print menuString
		inputString = raw_input('Input : ')
		if inputString == '1' :
			arrayNum = int(raw_input('Input the number : '))
			if arrayNum > 20 or arrayNum <= 0 :
				print 'too big number'
				continue
			while len(fiboArray) <= arrayNum :
				fiboArray.append(fiboArray[-2] + fiboArray[-1])
		elif inputString == '2' :
			for num in fiboArray :
				print num,
			print
		elif inputString == '3' :
			fiboArray = [0, 1]
		elif inputString == '4' :
			break
