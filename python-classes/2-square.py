#!/usr/bin/python3
"""Square class definition."""


class Square:
    """Class that defines a square."""

    def __init__(self, size=0):
        """Initialize a square.

        Args:
            size (int): size of the square (default is 0).

        Raises:
            TypeError: if size is not an integer.
            ValueError: if size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
