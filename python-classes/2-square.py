#!/usr/bin/python3
"""This module defines a Square class with validated size."""


class Square:
    """Represent a square with a private validated size attribute."""

    def __init__(self, size=0):
        """Initialize the square with optional size and validate it."""
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size
