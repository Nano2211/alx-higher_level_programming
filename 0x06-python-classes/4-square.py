#!/bin/usr/python3

"""Define a class Square"""

class Square:
    """REpresents square"""

    def __init__(self, size=0):
        """init new square.
        Args:
        size(int): the size of square
        """
        self.size = size

    @property
    def size(self):
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

        def area(self):
            """Return area"""
            return (self.__size * self.__size)
