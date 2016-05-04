import time

name = 'Kim Young Jin'

def problemDescription() :
	print '*'*30
	print 'ReversedGuessTheNumber'
	print 'Author: ' + name
	print 'ID: 2016025241'
	print '*'*30

def avg(a, b) :
	return (a+b)/2

def RevGuessTheNumber() :
	Min = 2
	Max = 99
	count = 0
	print 'Hi, ' + name + ', I guess the number that you think.'
	print 'Choose the number. (1 to 100)'
	answer = int(raw_input())
	print 'OK, I\' ll guess'
	while True :
		time.sleep(1)
		Mid = avg(Min, Max)
		print 'Com :' +str(Mid)
		count += 1
		if answer < Mid :
			print 'Down'
			Max = Mid
		elif answer > Mid :
			print 'Up'
			Min = Mid
		elif answer == Mid :
			print 'Correct'
			print 'Answer : ' + str(Mid)
			print 'guessed in ' + str(count) + ' times'
			break;


if __name__ == '__main__' :
	problemDescription()
	RevGuessTheNumber()