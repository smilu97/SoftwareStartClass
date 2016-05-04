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

board = '' # board ex) _____ a_pp_e
ml = '' # missed letters
cl = '' # correct letters
ans = ''
cc = 0 # correct count
limitmc = len(HANGMANPICS)

if __name__ == '__main__' :
  while True :
    print 'Welcome to Hangman!'
    ans = words[random.randint(0,len(words))]
    board = '_'*len(ans)
    ml = ''
    cl = ''
    cc = 0
    while True :
      print HANGMANPICS[len(ml)]
      print 'Missed Letters :',
      for c in ml :
        print c,
      print
      for c in board :
        print c,
      print
      inp = ''
      while True :
        inp = raw_input('Input a character : ').lower()
        if len(inp) != 1 :
          continue
        ordinp = ord(inp)
        if ord('a') > ordinp or ordinp > ord('z') :
          continue
        if inp in ml or inp in cl :
          continue
        break
      if inp in ans :
        cl += inp
        for i in range(len(ans)) :
          if ans[i] == inp :
            board = board[:i] + inp + board[i+1:]
            cc += 1
      else :
        ml += inp
      if cc == len(ans) :
        print 'you win!'
        print 'The answer was %s' % ans
        break
      if len(ml) >= limitmc :
        print 'you lose!'
        print 'The answer was %s' % ans
        break
    inp = ''
    while len(inp) == 0 :
      inp = raw_input('Do you want to play again? : ')    
    if inp[0] != 'y' :
      break



  

