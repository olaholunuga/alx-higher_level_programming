#!/usr/bin/python3
if __name__ == "__main__":
	from sys import argv
	argv = argv[1:]
	if len(argv) == 0:
		print("{:d}".format(0))
	else:
		num = 0
		for i in argv:
			num += int(i)
		print("{:d}".format(num))
