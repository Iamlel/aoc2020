cpass, valid = 0, 0
for line in open("input.txt", "r"):
    if (line[0] == '\n'):
        if (cpass == 7):
            valid += 1
        cpass = 0
    else:
        cpass += line.count(':') - line.count("cid")
if (cpass == 7):
    print(valid + 1)
else:
    print(valid)
