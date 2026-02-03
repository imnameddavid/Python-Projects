import time

startingnum = 0
incorrectnum = set()
numberset = set()

def check_odd_even(num):
	if num % 2 == 0:
		return "Even"
	else:
		return "Odd"

while True:
	startingnum = startingnum + 1
	print(f"Starting number: {startingnum}")
	num = startingnum
	while num not in incorrectnum and num != 1:
		if num not in incorrectnum and num != 1 and num not in numberset:
			numberset.add(num)
		if num % 2 == 0:
			num = num // 2
		else:
			num = 3 * num + 1
		print(f"{num} - {check_odd_even(num)}")
	incorrectnum.update(numberset)
	numberset.clear()
	sortedincorrect = sorted(incorrectnum)