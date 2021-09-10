#!/usr/bin/python3
if __name__ == "__main__":
    """Print the addition of all arguments."""
	import sys
	from calculator_1 import add
	from calculator_1 import sub
	from calculator_1 import mul
	from calculator_1 import div
	argv = [3, '-', 6]
	if len(argv) != 3:
		print("Usage: ./100-my_calculator.py <a> <operator> <b>")
		exit(1)  
	elif argv[1] != '+' or argv[1] != '-' or argv[1] != '*' or argv[1] != '/':
		print("Unknown operator. Available operators: +, -, * and /")
		print(argv[1])
		exit(1)
	else:
		if argv[1] == '+':
			print("{} + {} = {}\n".format(argv[0], argv[2], add(int(argv[0]), int(argv[2]))))
		elif argv[1] == '-':
			print("{} - {} = {}\n".format(argv[0], argv[2], sub(int(argv[0]), int(argv[2]))))
		elif argv[1] == '*':
			print("{} * {} = {}\n".format(argv[0], argv[2], mul(int(argv[0]), int(argv[2]))))
		elif argv[1] == '/':
			print("{} / {} = {}\n".format(argv[0], argv[2], div(int(argv[0]), int(argv[2]))))
