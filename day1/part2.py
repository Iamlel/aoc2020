with open("input.txt", "r") as fp:
	numbers = [int(x) for x in fp.readlines()]
	
for x in numbers:
	for y in numbers:
		if (2020 - x - y) in numbers:
			print((2020 - x - y) * x * y)
			exit()
