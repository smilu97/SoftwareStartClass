import random

__author__ = 'Kim Young Jin'
__ID__ = '2016025241'

encDic = {}
words = 'game high shoes automatics author cat dog notebook macbook professor door quick projector screen computer language sublime ide worst worry \
words encrypt decrypt md sha base hash potato password document video music window linux mac unix'.split()

def problemDescription() :
	print '*'*20 + '\nHack the password\nAuthor: %s\nID: %s\n'% (__author__, __ID__) + '*'*20

def shuffle(li) :
	numtochange = random.randint(len(li), 3*len(li)) # the number to change (length(list) ~ 3 * length(list))
	for i in range(numtochange) :
		a = random.randint(0, len(li)-1) # randomly select a
		b = random.randint(0, len(li)-1) # randomly select b
		while a == b :
			b = random.randint(0, len(li)-1) # b must not be equal to a
		tmp = li[a]
		li[a] = li[b]
		li[b] = tmp # change two values [a], [b]
	return li

def encrypt(s) :
	ns = ''
	for ch in s :
		if encDic.get(ch) != None : # is exists in dictionary?
			if type(encDic[ch]) == type('s') : # is alphabetical?
				ns += encDic[ch]
			else : 
				ns += '*' # there is an error
		else :
			ns += ch # if not exists in dictionary, don't change
	return ns

def decrypt(s) :
	ns = ''
	for ch in s :
		for finder in range(ord('a'), ord('z')+1) : # find what pointing the character
			if encDic[chr(finder)] == ch :
				ns += chr(finder)
				break
		if ord(ch) < ord('a') or ord('z') < ord(ch) : 
			ns += ch # if not alphabetical, don't change
	return ns

def makeDic() :
	before = ''
	dic = {}
	for ch in range(ord('a'), ord('z')+1) : # 'a' to 'z'
		before += chr(ch)
	after = ''.join(shuffle(list(before))) # shuffle 
	for ch in range(26) :
		dic[chr(ord('a')+ch)] = after[ch] # apply to dictionary
	return dic 

beforeWords = []

if __name__ == '__main__' :
	encDic = makeDic()
	problemDescription()
	# for ch in range(ord('a'), ord('z')+1) :
	# 		print '%s : %s' % (chr(ch), encDic[chr(ch)]) # print dictionary
	for level in range(5) :
		wordtosay = words[random.randint(0,len(words))] # word to hint
		while wordtosay in beforeWords :
			wordtosay = words[random.randint(0,len(words))] # already suggested
		beforeWords.append(wordtosay)
		print 'A said, \'%s\'' % wordtosay # give hint
		encw = encrypt(wordtosay)
		print 'B said, \'%s\'' % encw # give encrypted hint
		print
		if level == 4 : # don't get input at 5th
			break
		inp = ''
		while inp != 'n' and inp != 'y' :
			inp = raw_input('Do you know the password? (yes or no) : ').lower() # get input, only n or y
		if inp == 'n' :
			continue
		elif inp == 'y' :
			break
	answer = words[random.randint(0,len(words))] # word to test
	while answer in beforeWords :
		answer = words[random.randint(0,len(words))] # already suggested?
	inp = raw_input('What you enter the answer \'%s\' : ' % answer).lower()
	uanswer  = encrypt(answer)
	if inp == uanswer :
		print 'Got it. You are GENIUS' # Answer
	else :
		print 'Answer is <%s>' % uanswer
		print 'Your answer\'s decryption: ' + decrypt(inp) # Not answer

