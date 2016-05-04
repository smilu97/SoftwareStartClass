def quicksort(x) :
	if len(x) <= 1:
		return x
	pivot = x[len(x)/2]
	less = []
	more = []
	equal = []
	for a in x :
		if a < pivot :
			less.append(a)
		elif a > pivot :
			more.append(a)
		else :
			equal.append(a)

	return quicksort(less) + equal + quicksort(more)

if __name__ == '__main__' :
	num = input('input N : ')
	arraylist = []
	for i in range(num) :
		arraylist.append(input())
	sortedlist = quicksort(arraylist)
	resultstr = 'Result : '
	for i in sortedlist :
		resultstr += str(i) + ' '
	print resultstr