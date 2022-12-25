highestID = 0
for line in open("input.txt", "r"):
	ID =  int(line.replace('F', '0').replace('B', '1').replace('L', '0').replace('R', '1'), 2)
	if (ID > highestID):
		highestID = ID
print(highestID)
