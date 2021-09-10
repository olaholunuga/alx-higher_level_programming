#!/usr/bin/python3
if __name__ == "__main__":
    """Print the addition of all arguments."""
    from sys import argv
    argv = argv[1:]
    num = 0
    for i in argv:
        num += int(i)
print("{:d}".format(num))
