#!/usr/bin/python3



class Square:

    def __init__(self, __size=0):
        self.__size = __size

    @property
    def size(self):
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("__size must be an integer")
        elif value < 0:
            raise ValueError("__size must be >= 0")
        self.__size = value

    def area(self):
        return (self.__size * self.__size)

    def __eq__(self, other):
        return (self.__size * self.__size) == (other.__size * other.__size)

    def __gt__(self, other):
        return (self.__size * self.__size) > (other.__size * other.__size)

    def __ge__(self, other):
        return (self.__size * self.__size) >= (other.__size * other.__size)

    def __lt__(self, other):
        return (self.__size * self.__size) < (other.__size * other.__size)

    def __le__(self, other):
        return (self.__size * self.__size) <= (other.__size * other.__size)
