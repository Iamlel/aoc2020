with open("input.txt", "r") as fp:
	numbers = [int(x) for x in fp.readlines()]

for num in numbers:
	if (2020 - num) in numbers:
		print((2020 - num) * num)
		exit()
