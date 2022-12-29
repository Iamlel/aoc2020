highestID = 0
with open("input.txt", "r") as fp:
	for line in fp.readlines():
		ID =  int(line.replace('F', '0').replace('B', '1').replace('L', '0').replace('R', '1'), 2)
		if (ID > highestID):
			highestID = ID
print(highestID)
