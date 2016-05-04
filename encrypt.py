import random

__author__ = 'KimYoungJin'
__ID__ = '2016025241'

def makeRandomEncDic() :
	tostring = ''
	encDic = {}
	for i in range(26) :
		ch = chr(random.randint(ord('a'), ord('z')))
		while ch in tostring :
			ch = chr(random.randint(ord('a'), ord('z')))
		tostring += ch
	for i in range(ord('a'), ord('z')+1) :
		encDic[chr(i)] = tostring[i-ord('a')]
	return encDic

def encrypt(dic, rdata) :
	edata = ''
	for ch in rdata :
		if ord('a') <= ord(ch) and ord(ch) <= ord('z') :
			edata += dic[ch]
		else :
			edata += ch
	return edata

rawdata = raw_input('Input the text to encrypt : ')
encDic = makeRandomEncDic()
print encDic
lowerEncdata = encrypt(encDic, rawdata.lower())
encData = ''
for i, ch in enumerate(rawdata) :
	if ch.isalpha() :
		if ch.isupper() :
			encData += lowerEncdata[i].upper()
		else :
			encData += lowerEncdata[i]
	else :
		encData += lowerEncdata[i]
print 'Encrypted text : ' + encData

