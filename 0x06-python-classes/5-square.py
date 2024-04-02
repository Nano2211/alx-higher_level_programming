#!/usr/bin/python3
"""define a new class Square"""


class Square:
    """reps new square"""
    def __init__(self, size=0):
        """inits square
        Args:
        value (int): size of square
        """
        self.__size = size

        @property
        def size(self):
            """int: private size

            Returns:
                private size
                """
                return self.__size

            @size.setter
            def size(self, value):
                """Sets value into size, must be int.

                Args:
                value (int): size of squae.
                """
                if not isinstance(size, int):
                    raise TypeError('size must be an integer')
                elif value < 0:
                    raise ValueError('size must be >= 0')
                else:
                    self.__size = value #: size of the square

                    def area(self):
                        """returns area

                        Returns:
                        area.
                        """
                        return self.__size**2

                    def my_print(self):
                        """prints in stdout the square with char #"""

                        if self.__size != 0:
                            for i in range(self.__size):
                                for j in range(self.__size):
                                    print('#', end='')
                                    print()
                                else:
                                    print()
