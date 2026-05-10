#!/usr/bin/python3
"""This module defines the class Square."""


class Square:
    """This is documentation of class Square by size."""
    def __init__(self, size=0):
        self.__size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, size):
        "This is setter for size"
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size

    def area(self):
        area = self.__size * self.__size
        return area
