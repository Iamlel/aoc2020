# regex is slow but I wanted to use it
import re

valid = 0
for line in open("input.txt", "r"):
    password = re.split("[- :]+", line)
    if ((password[3][int(password[0]) - 1] == password[2]) ^ (password[3][int(password[1]) - 1] == password[2])):
        valid += 1
print(valid)
