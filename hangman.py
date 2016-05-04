import random

HANGMANPICS = ['''
  +---+
  |   |
      |
      |
      |
      |
 =========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
 =========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
 =========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
 =========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
 =========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
 =========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      | 
 ========='''
 ]

words = 'ant baboon badger bat bear beaver camel cat clam cobra cougar \
coyote crow deer dog donkey duck eagle ferret fox frog goat hoose hawk \
lion lizard llama mole monkey moose mouse mule newt otter owl panda parrot \
pigeon python rabbit ram rat raven rhino salmon seal shark sheep skunk \
sloth snake spider stork swan tiger toad trout turkey turtle weasel \
whale wolf wombat zebra'.split()

def getRandomWord(wordList) :
	wordIndex = random.randint(0,len(wordList)-1)
	return wordList[wordIndex]

def displayBoard(HANGMANPICS, missedLetters, correctLetters, secretWord) :
	print HANGMANPICS[len(missedLetters)]
	print

	print 'Missed letters: '
	for letter in missedLetters :
		print letter,
	print

	blanks = '_' * len(secretWord)

	for i in range(len(secretWord)) :
		if secretWord[i] in correctLetters :
			blanks = blanks[:i] + secretWord[i] + blanks[i+1:]

	for letter in blanks :
		print letter,
	print

def getGuess(alreadyGuessed) :
	while True :
		print 'Guess a letter.'
		guess = raw_input()
		guess = guess.lower()
		if len(guess) != 1 :
			print 'Print enter a single letter'
		elif guess in alreadyGuessed :
			print 'You have already guessed that letter. Choose again'
		elif guess not in 'abcdefghijklmnopqrstuvwxyz' :
			print 'You entered a letter'
		else :
			return guess

def playAgain() :
	print 'Do you want to play again?(yes or no)'
	return raw_input().lower().startswith('y')

if __name__ == '__main__' :
	print 'H A N G M A N'
	missedLetters = ''
	correctLetters = ''
	secretWord = getRandomWord(words)
	gameIsDone = False

	while True :
		displayBoard(HANGMANPICS, missedLetters, correctLetters, secretWord)
		guess = getGuess(missedLetters + correctLetters)
		if guess in secretWord :
			correctLetters = correctLetters + guess
			foundAllLetters = True
			for i in range(len(secretWord)) :
				if secretWord[i] not in correctLetters :
					foundAllLetters = False
					break
			if foundAllLetters :
				print 'Yes! The secret is "' + secretWord + '"! You have won!'
				gameIsDone = True
		else :
			missedLetters = missedLetters + guess
			if len(missedLetters) == len(HANGMANPICS) - 1 :
				displayBoard(HANGMANPICS, missedLetters, correctLetters, secretWord)
				print 'You have run out of guesses!\nAfter ' + str(len(missedLetters)) + ' missed guesses and ' + str(len(correctLetters)) + ' correct guesses, the word was "'  + secretWord + '"'
				gameIsDone = True
		if gameIsDone :
			if playAgain() :
				missedLetters = ''
				correctLetters = ''
				gameIsDone = False
				secretWord = getRandomWord(words)
			else :
				break





