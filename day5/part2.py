seats = []
with open("input.txt", "r") as fp:
	for line in fp.readlines():
		seats.append(int(line.replace('F', '0').replace('B', '1').replace('L', '0').replace('R', '1'), 2))

for seat in seats:
    if not (seat + 1) in seats:
        if (seat + 2) in seats:
            print(seat + 1)
            exit()
