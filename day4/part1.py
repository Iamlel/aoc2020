cpass, valid = 0, 0
with open("input.txt", "r") as fp:
    for line in fp.readlines():
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
