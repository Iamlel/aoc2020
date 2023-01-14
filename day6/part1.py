usedLetters, total = [], 0
for line in open("input.txt", "r"):
	if (line[0] == '\n'):
		total += len(usedLetters)
		usedLetters.clear()
	for c in line[:-1]:
		if not (c in usedLetters):
			usedLetters.append(c)

print(total + len(usedLetters))
