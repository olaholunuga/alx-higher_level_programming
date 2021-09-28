#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        for i in range(x):
            print(my_list[i], end="")
        print()
        return x
    except:
        u = 0
        for i in my_list:
            u += 1
        print()
        return u
