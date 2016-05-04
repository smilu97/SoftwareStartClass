
__author__ = 'Kim Young Jin'

def vectorMultiply(a, b) :
	retMatrix = [[0,0],[0,0]]
	retMatrix[0][0] = a[0][0] * b[0][0] + a[0][1] * b[1][0]
	retMatrix[0][1] = a[0][0] * b[0][1] + a[0][1] * b[1][1]
	retMatrix[1][0] = a[1][0] * b[0][0] + a[1][1] * b[1][0]
	retMatrix[1][1] = a[1][0] * b[0][1] + a[1][1] * b[1][1]
	return retMatrix

fiboBaseMatrix = [[0,1],[1,1]]
fiboMatrix = [fiboBaseMatrix]

def log2(n) :
	count = 0
	a = 1
	while a < n :
		a <<= 1
		count += 1
	return count

def get2ExpChain(n) :
	retArray = []
	chnum = 1
	while chnum < n :
		chnum <<= 1
	while n != 0 :
		while chnum > n :
			chnum >>= 1
		retArray.append(chnum)
		n -= chnum
	return retArray

def fiboNumber(n) :
	expChain = get2ExpChain(n)
	maxExp = log2(expChain[0])
	while len(fiboMatrix) <= maxExp :
		fiboMatrix.append(vectorMultiply(fiboMatrix[-1],fiboMatrix[-1]))
	retMatrix = [[1,0],[0,1]]
	for e in expChain :
		retMatrix = vectorMultiply(retMatrix, fiboMatrix[log2(e)])
	return retMatrix


if __name__ == '__main__' :
	num = int(raw_input('Input : '))
	print fiboNumber(num)[0][1]

	


