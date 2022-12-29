import numpy

file = open("input.txt", "r")
SLOPES = ((1, 1), (1, 3), (1, 5), (1, 7), (2, 1))

slopes = [0] * len(SLOPES)
charscount = len(file.readline()) - 1
for k, line in enumerate(file):
	for i, s in enumerate(SLOPES):
		if ((k + 1) % s[0] == 0):
			if (line[int((k + 1) * s[1] / s[0]) % charscount] == '#'):
				slopes[i] += 1

print(numpy.product(slopes))
file.close()
