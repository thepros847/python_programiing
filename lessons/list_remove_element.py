numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(numbers)
numbers.remove(5)
print(numbers)
del numbers[7]
print(numbers)


def histogram(seq):
	d = dict()
	for element in seq:
		if element not in d:
			d[element] = 1
		else:
			d[element] += 1
			return d
			h = histogram('brontosaurus')
			Print(h)