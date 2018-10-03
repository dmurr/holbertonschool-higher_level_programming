#!/usr/bin/python3
class Square:

    def __init__(self, size=0):
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        return self.__size ** 2

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def my_print(self):
        if self.size > 0:
            for col in range(self.__size):
                for row in range(self.__size):
                    if row < self.__size - 1:
                        print("#", end="")
                    else:
                        print("#")
        else:
            print()
