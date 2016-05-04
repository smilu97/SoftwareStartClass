def problemDescription() :
	print '********************'
	print 'Number of divisors'
	print '********************'

def numOfDivisors(n) :
	result = 1
	val = int(n)
	k = 2
	while val != 1 :
		kcount = 0
		while val%k == 0 :
			kcount += 1
			val /= k
		result *= kcount + 1
		k += 1
	return result

problemDescription()
num1 = int(raw_input('Input the first number : ')) # Get 2 intergers 
num2 = int(raw_input('Input the second number  : '))
nd_num1 = numOfDivisors(num1) # the number of divisors of num1
nd_num2 = numOfDivisors(num2) # the number of divisors of num2
sumOfNd = nd_num1 + nd_num2 # Calculate the sum of nd_num1 and nd_num2
print 'Number of divisors of first number is ' + str(nd_num1)
print 'Number of divisors of second number is ' + str(nd_num2)
print 'Result is : ' + str(sumOfNd)

a = a  + b
a += b
a = a - b
a -= b

