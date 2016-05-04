import random
import time

# STRING_INTRO (string) : Intro message printed in the start of game.
STRING_INTRO = '''You are in a land full of dragons. In front of you.
you see two caves. In one cave, the dragon is friendly.
and will share his treasure with you. The other dragon
is greedy and hungry, and will eat you on sight
'''

CAVE_SELECTEE = ['1', '2']
PLAYAGAIN_INITIAL = 'yes'
PLAYAGAIN_SELECTEE = ['yes', 'y']
CHARACTER_DEFAULT_NAME = 'unknown'
PLAYER_DEFAULT_NAME = 'Player'
FIGHT_MYATTACK_MESSAGE = 'You attacked %s (Damage : %d)'
FIGHT_MYHP_DISPLAY = 'Your hp is %d'
FIGHT_ENEMYATTACK_MESSAGE = '%s attacked you (Damage : %d)'
FIGHT_ENEMYHP_DISPLAY = '%s\'s hp is %d'
FIGHT_WIN_MESSAGE = 'You win!'
FIGHT_LOSE_MESSAGE = 'You lose!'
STRING_CAVE_QUESTION = 'Which cave will you go into? (1 or 2) ' # Question for cave to go
STRING_TEXT = ['You approach the cave...', 'It is dark and spooky...', \
					'A large dragon jumps out in front of you! He opens his jaws and...']
STRING_SUCCESS = 'Gives you his treasure.'
STRING_FAIL = 'Gobbles you dodwn in one bite!'
STRING_REPLAY_QUESTION = 'Do you want to play again? (yes or no) '
STRING_GUESSNUMBER_INTRO = 'I\'ll guess your number!'
STRING_GUESSNUMBER_TRY = 'The number is %d'
STRING_GUESSNUMBER_SUCCESS = 'Success!'
STRING_GUESSNUMBER_WRONGANSWER = 'What?'
STRING_GUESSNUMBER_LYING = 'You\'re lying'
STRING_GUESSNUMBER_ANSWER = ['low', 'high', 'correct']

textWaitTime = 0.1

class Character :
	def __init__(self) :
		self.hp = 100
		self.maxhp = 100
		self.atk = 10
		self.name = CHARACTER_DEFAULT_NAME
	def fightWith(self,enemy) :
		while self.hp >= 0 and enemy.hp >= 0 :
			dmg = random.randint(1,self.atk)
			print FIGHT_MYATTACK_MESSAGE % (enemy.name, dmg)
			enemy.hp -= dmg
			print FIGHT_ENEMYHP_DISPLAY % (enemy.name, enemy.hp)
			time.sleep(textWaitTime)
			print
			if enemy.hp <= 0 :
				break
			dmg = random.randint(1,enemy.atk)
			print FIGHT_ENEMYATTACK_MESSAGE % (enemy.name, dmg)
			self.hp -= dmg
			print FIGHT_MYHP_DISPLAY % self.hp
			time.sleep(textWaitTime)
			print
			if self.hp <= 0 :
				break
		if self.hp <= 0 :
			print FIGHT_WIN_MESSAGE
		elif enemy.hp <= 0 :
			print FIGHT_LOSE_MESSAGE

class DragonRealm :
	def __init__(self) :
		self.player = Character()
		self.name = PLAYER_DEFAULT_NAME
	def displayIntro(self) :
		print STRING_INTRO

	def chooseCave(self) :
		cave = ''
		while not cave in CAVE_SELECTEE :
				cave = raw_input(STRING_CAVE_QUESTION)
		return cave

	def playWithDragon(self) :
		print STRING_SUCCESS
		print STRING_GUESSNUMBER_INTRO
		min = 1
		max = 31
		while True :
			mid = (min + max) / 2
			print STRING_GUESSNUMBER_TRY % mid
			msg = raw_input()
			if msg == STRING_GUESSNUMBER_ANSWER[0] :
				max = mid
			elif msg == STRING_GUESSNUMBER_ANSWER[1] :
				min = mid
			elif msg == STRING_GUESSNUMBER_ANSWER[2] :
				print STRING_GUESSNUMBER_SUCCESS
				break
			else :
				print STRING_GUESSNUMBER_WRONGANSWER
			if max-min <= 1 :
				print STRING_GUESSNUMBER_LYING
				print STRING_GUESSNUMBER_SUCCESS
				break

	def fightWithDragon(self) :
		dragon = Character()
		dragon.atk = 10
		dragon.name = 'Unvisible Dragon'
		self.player.fightWith(dragon)

	def checkCave(self, chosenCave) :
		for strings in STRING_TEXT :
			print strings
			time.sleep(textWaitTime)
		print
		time.sleep(textWaitTime)
		friendlyCave = random.randint(1,2)
		if chosenCave == str(friendlyCave) :
			self.playWithDragon()
		else :
			self.fightWithDragon()
	def Run(self) :
		playAgain = PLAYAGAIN_INITIAL
		while playAgain in PLAYAGAIN_SELECTEE :
			self.player.hp = 100
			self.displayIntro()
			caveNumber = self.chooseCave()
			self.checkCave(caveNumber)
			print STRING_REPLAY_QUESTION
			playAgain = raw_input()

if __name__ == '__main__' :
	dr = DragonRealm()
	dr.Run()