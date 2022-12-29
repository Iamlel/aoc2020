with open("input.txt", "r") as fp:
	for line in fp.readlines():
		numbers = [int(x) for x in f.readlines()]

for num in numbers:
	if (2020 - num) in numbers:
		print((2020 - num) * num)
		exit()
