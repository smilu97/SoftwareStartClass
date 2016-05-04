import time

name = 'Kim Young Jin'

def problemDescription() :
	print '*'*30
	print 'ReversedGuessTheNumber'
	print 'Author: ' + name
	print '2016025241'
	print '*'*30

def avg(a, b) :
	return (a+b)/2

def RevGuessTheNumber() :
	min = 2
	max = 99
	count = 0
	print 'Hi, ' + name + ', I guess the number that you think.'
	print 'Choose the number. (1 to 100)'
	answer = int(raw_input())
	print 'OK, I\'ll guess'
	while True :
		time.sleep(1)
		mid = avg(min, max)
		print 'Com :' +str(mid)
		count += 1
		if answer < mid :
			print 'Down'
			max = mid
		elif answer > mid :
			print 'Up'
			min = mid
		elif answer == mid :
			print 'Correct'
			print 'Answer : ' + str(mid)
			print 'guessed in ' + str(count) + ' times'
			break;


if __name__ == '__main__' :
	problemDescription()
	RevGuessTheNumber()