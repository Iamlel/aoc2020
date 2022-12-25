file = open("input.txt", "r")
#CHARCOUNT = 31 - use this for softcode

file.readline()
countx = trees = 0
for line in file.readlines():
	countx = (countx + 3) % 31 #CHARCOUNT
	if (line[countx] == '#'):
		trees += 1
print(trees)
