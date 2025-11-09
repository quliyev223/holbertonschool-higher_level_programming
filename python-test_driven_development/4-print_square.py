#!/usr/bin/python3
"""Function that prints a square with the character #"""

def print_square(size):
    """Prints a square with the character #

    Args:
        size (int): size of the square
    
    Raises:
        TypeError: if size is not an integer
        ValueError: if size is < 0
    """
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for _ in range(size):
        print("#" * size)
