#!/usr/bin/python3
"""This module defines the class Square."""


class Square:
    """This is documentation of class Square by size."""

    def __init__(self, size=0, position=(0, 0)):
        """storing private attribute, size and position in object self."""
        self.size = size
        self.position = position

    @property
    def size(self):
        """Getter for read access to size."""
        return self.__size

    @size.setter
    def size(self, size):
        """Setter for write access to modify size."""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    @property
    def position(self):
        """Getter for position read access."""
        return self.__position

    @position.setter
    def position(self, position):
        if (
            not isinstance(position, tuple) or
            len(position) != 2 or
            not all(isinstance(i, int) and i >= 0 for i in position)
        ):
            raise TypeError("position must be tuple of two positive integers")
        else:
            self.__position = position

    def area(self):
        area = self.__size * self.__size
        return area

    def my_print(self):
        if self.__size == 0:
            print("")
        else:
            if self.__position[1] > 0:
                for k in range(self.__position[1]):
                    print("")
            for i in range(self.__size):
                print("#" * self.__size + " " * self.__position[0])
