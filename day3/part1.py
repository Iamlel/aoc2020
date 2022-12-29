file = open("input.txt", "r")

countx = trees = 0
charscount = len(file.readline()) - 1
for line in file.readlines():
	countx = (countx + 3) % charscount
	if (line[countx] == '#'):
		trees += 1
print(trees)
file.close()
