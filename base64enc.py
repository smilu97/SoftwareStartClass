import random

indexString = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'

def makeDic() :
	indexToAlpha = ''
	alphaToIndex = {}
	baseString = list('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/')
	random.shuffle(baseString)
	baseString = ''.join(baseString)
	indexToAlpha = baseString
	for i, ch in enumerate(baseString) :
		alphaToIndex[ch] = i
	return alphaToIndex, indexToAlpha

def b64enc(rdata, indexToAlpha) :
	edata = ''
	remain = len(rdata) % 3
	rdata += chr(0) * remain
	for i in range(0, len(rdata)-3, 3) :
		dat = (ord(rdata[i]) << 16) + (ord(rdata[i+1]) << 8) + ord(rdata[i+2])
		for j in range(4) :
			dat2 = dat & 63
			edata += indexToAlpha[dat2]
			dat >>= 6
	if remain == 1 :
		edata = edata[:-2] + '=='
	elif remain == 2 :
		edata = edata[:-1] + '='
	return edata

alphaToIndex, indexToAlpha = makeDic()
print 'dic : ' + indexToAlpha
rawdata = raw_input('input : ')
edata = b64enc(rawdata, indexToAlpha)
print edata