import random

if __name__ == '__main__' :
	fromnum = 1
	tonum = 100
	guessesTaken = 1
	print 'Hello! What is your name?'
	myName = raw_input()

	number = random.randint(fromnum, tonum)

	print 'Well, %s, I am thinking of a number between %d and %d' % (myName, fromnum, tonum)
	# print 'Well, ' + myName + ', I am thinking of a number between 1 and 20'

	# Game loop
	while guessesTaken < 6 :
		print 'Take a guess. '

		guess = raw_input()
		guess = int(guess)

		if guess > number :
			print 'Your guess is too high'
		elif guess < number :
			print 'Your guess is too low'
		elif guess == number :
			break;
		guessesTaken = guessesTaken + 1
	# At the end of game, Check if the user corrected the number
	if guess == number :
		guessesTaken = str(guessesTaken)
		# print 'Good job, %s! you guessed my number in %s guesses!' % (myName, guessesTaken)
		print 'Good job, ' + myName + '! you guessed my number in ' + guessesTaken + ' guesses!'
	elif guess != number :
		number = str(number)
		# print 'Nope. The number I was thinking of was %s' % number
		print 'Nope. The number I was thinking of was ' + number
