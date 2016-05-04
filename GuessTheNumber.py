import random

print 'Hello! What is your name?'
username = raw_input()
print 'Well, %s, I am thinking of a number between 1 and 20' % username
# print 'Well, ' + username + ', I am thinking of a number between 1 and 20'
answer = random.randint(1,20)
# print answer
input_answer = -1
count = 0
while answer != input_answer :
	print 'Take a guess.'
	input_answer = int(input())
	count += 1
	if input_answer > answer :
		print 'Your guess is too high.'
	elif input_answer < answer :
		print 'Your guess is too low.'
	elif input_answer == answer :
		print 'Good job, %s! You guessed my number in %d guesses!' % (username, count)
		# print 'Good job, ' + username + '! You guessed my number in ' + str(count) + ' guesses!'
