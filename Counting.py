

if __name__ == '__main__' :
	passnum = 0
	failnum = 0
	for counter in range(10) :
		print 'Enter result (1 = pass, 2 = fail) : '
		inputnumber = input()
		if(inputnumber == 1) :
			passnum += 1
		elif(inputnumber == 2) :
			failnum += 1
	print 'Passed = %d' % passnum
	print 'Failed = %d' % failnum