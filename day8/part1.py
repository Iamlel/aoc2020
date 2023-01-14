acc, status = 0, []
instructions = open("input.txt", "r").readlines()
i = 0
while True:
	status.append(i)
	match (instructions[i][:3]):
		case "acc":
			acc += int(instructions[i][4:-1])
		case "jmp":
			if (i + int(instructions[i][4:-1]) in status):
				break
			else:
				i += int(instructions[i][4:-1]) - 1
	i += 1
print(acc)
