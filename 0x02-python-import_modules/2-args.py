#!/usr/bin/python3
if __name__ == "__main__":
    """Print the number of and list of arguments."""
    from sys import argv
    argv = argv[1:]
    if len(argv) == 0:
        print("0 argument.")
    elif len(argv) == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(len(argv)))

for i in range(len(argv)):
    print("{}: {}".format(int(i + 1), argv[i]))
