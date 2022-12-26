import re

valid = 0
for line in open("input.txt", "r"):
    password = re.compile("[- :]+").split(line)
    if (int(password[0]) <= password[3].count(password[2]) <= int(password[1])):
        valid += 1
print(valid)
