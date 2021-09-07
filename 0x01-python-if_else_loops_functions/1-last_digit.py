#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
num1 = str(number)
num2 = num1[-1:]
num = int(num2)
if num > 5:
    print("Last digit of {:d} is {:d} and is greater than {:d}".format(number, num, 5))
elif num == 0:
    print("Last digit of {:d} is {:d} and is {:d}".format(number, num, 0))
else:
    print("Last digit of {:d} is {:d} and is less than {:d} and not {:d}".format(number, num, 6, 0))
