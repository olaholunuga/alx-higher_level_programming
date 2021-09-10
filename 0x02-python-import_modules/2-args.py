#!/usr/bin/python3
if __name__ == "__main__":
	from sys import argv
	argv = argv[1:]
	if len(argv) == 0:
		print("{} argument.".format(len(argv)))
	elif len(argv) == 1:
		print("{} argument:".format(len(argv)))
		print("1: {}".format(argv[0]))
	else:
		print("{} arguments:".format(len(argv)))
		for i in range(len(argv)):
			print("{}: {}".format(int(i + 1), argv[i]))
