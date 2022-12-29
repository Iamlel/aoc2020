# regex slow but I wanted to use it
import re

valid = 0
with open("input.txt", "r") as fp:
	for line in fp.readlines():
        password = re.split("[- :]+", line)
        if (int(password[0]) <= password[3].count(password[2]) <= int(password[1])):
            valid += 1
print(valid)
