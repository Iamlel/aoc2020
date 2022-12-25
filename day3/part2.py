import numpy

file = open("input.txt", "r")
#CHARCOUNT = 31
SLOPES = ((1, 1), (1, 3), (1, 5), (1, 7), (2, 1))

slopes = [0] * len(SLOPES)

file.readline()
for k, line in enumerate(file):
	for i, s in enumerate(SLOPES):
		if ((k + 1) % s[0] == 0):
			if (line[int((k + 1) * s[1] / s[0]) % 31] == '#'): # CHARCOUNT
				slopes[i] += 1

print(numpy.product(slopes))
