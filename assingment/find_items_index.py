def find(word,letter):
	index = 2
	while index < len(word):
		if word[index] == letter:
			return index
		index = index +1
	return "Character not in sequence"
print(find("Python", "Z"))