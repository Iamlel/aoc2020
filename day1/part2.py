numbers = [int(x) for x in open("input.txt", "r").readlines()]
	
for x in numbers:
	for y in numbers:
		if (2020 - x - y) in numbers:
			print((2020 - x - y) * x * y)
			exit()
