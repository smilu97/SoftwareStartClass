import random

__author__ = 'Kim Young Jin'
__ID__ = '2016025241'

encDic = {}
words = 'game high shoes automatics author cat dog notebook macbook professor door quick projector screen computer language sublime ide worst worry \
words encrypt decrypt md sha base document video music window linux mac unix'.split()

def problemDescription() :
	print '*'*15 + '\nHack the password\nAuthor: %s\nID: %s\n'% (__author__, __ID__) + '*'*15

def shuffle(li) :
	numtochange = random.randint(len(li), 3*len(li))
	for i in range(numtochange) :
		a = random.randint(0, len(li)-1)
		b = random.randint(0, len(li)-1)
		while a == b :
			b = random.randint(0, len(li)-1)
		tmp = li[a]
		li[a] = li[b]
		li[b] = tmp
	return li

def encrypt(s) :
	ns = ''
	for ch in s :
		if encDic.get(ch) != None :
			if type(encDic[ch]) == type('s') :
				ns += encDic[ch]
			else :
				ns += '*'
		else :
			ns += '*'
	return ns

def decrypt(s) :
	ns = ''
	for ch in s :
		for finder in range(ord('a'), ord('z')+1) :
			if encDic[chr(finder)] == ch :
				ns += chr(finder)
				break
	return ns

def makeDic() :
	before = ''
	dic = {}
	for ch in range(ord('a'), ord('z')+1) :
		before += chr(ch)
	after = ''.join(shuffle(list(before)))
	for ch in range(26) :
		dic[chr(ord('a')+ch)] = after[ch]
	return dic 

encDic = makeDic()
beforeWords = []

if __name__ == '__main__' :
	problemDescription()
	for ch in range(ord('a'), ord('z')+1) :
			print '%s : %s' % (chr(ch), encDic[chr(ch)])
	for level in range(5) :
		wordtosay = words[random.randint(0,len(words))]
		while wordtosay in beforeWords :
			wordtosay = words[random.randint(0,len(words))]
		beforeWords.append(wordtosay)
		print 'A said, \'%s\'' % wordtosay
		encw = encrypt(wordtosay)
		print 'B said, \'%s\'' % encw
		print
		if level == 4 :
			break
		inp = ''
		while inp != 'n' and inp != 'y' :
			inp = raw_input('Do you know the password? (yes or no) : ').lower()
		if inp == 'n' :
			continue
		elif inp == 'y' :
			break
	answer = words[random.randint(0,len(words))]
	while answer in beforeWords :
		answer = words[random.randint(0,len(words))]
	inp = raw_input('What you enter the answer \'%s\' : ' % answer).lower()
	uanswer  = encrypt(answer)
	if inp == uanswer :
		print 'Git it. You are GENIUS'
	else :
		print 'Answer is <%s>' % uanswer
		print 'Your answer\'s decryption: ' + decrypt(inp)

