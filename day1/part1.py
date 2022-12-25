with open("input.txt", "r") as f:
	numbers = [int(x) for x in f.readlines()]

for num in numbers:
	if (2020 - num) in numbers:
		print((2020 - num) * num)
		exit()
