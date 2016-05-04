import random

a_until = input()
b_until = 10

if a_until == 123456 :
	print 'You found a easteregg'
	print 'Try to guess my number!'
	gn = random.randint(1,10000)
	un = -1
	while gn != un :
		un = input('number? : ')
		if(un > gn) :
			print 'Too big'
		elif(un < gn) :
			print 'Too small'
		elif(un == gn) :
			print 'Yes!!'
	exit()
if a_until == 654321 :
	print 'You found a easteregg'
	print 'I will guess your number'
	min = 0
	max = 5
	findmax = True
	finded = False
	while findmax == True :
		if finded == True :
			break;
		print str(max) + '?'
		inputvalue = raw_input()
		if inputvalue == 'small' :
			findmax = False;
		elif inputvalue == 'big' :
			max = max * 2
		elif inputvalue == 'correct' :
			print 'Wow...'
			finded = True
	while finded == False :
		mid = int((min+max)/2)
		print str(mid) + '?'
		inputvalue = raw_input()
		if inputvalue == 'small' :
			max = mid
		elif inputvalue == 'big' :
			min = mid
		elif inputvalue == 'correct' :
			print 'Yes!!'
			finded = True
	exit()

def print_googoo(first, second) :
	for i in range(1,first) :
		for j in range(1, second) :
			print str(i)+'*'+str(j)+'='+str(i*j)

# print_googoo(a_until,b_until)

a = 1
while a<a_until :
	b = 1
	print '*'*10 + str(a) + 'dan' + '*'*10
	while b<b_until :
		print str(a)+'*'+str(b)+'='+str(a*b)
		b = b + 1
	a = a + 1
print '*'*24