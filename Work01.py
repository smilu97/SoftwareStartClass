def sum(a, b) :
	return a + b

def func(n) :
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

print(func(input()))