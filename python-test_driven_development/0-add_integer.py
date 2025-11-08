#!/usr/bin/python3
"""
This module provides a function that adds two integers.
"""

def add_integers(a, b=98):
    """
    Adds two integers or floats (which are cast to integers).


    Args:
        a (int or float): First number.
        b (int or float): Second number.Defaults to 98.

    Returns:
        int: The addition of a and b as integers.

    Raises:
        TypeError: If a or b is not an integer or float.
    """
    if type(a) not in (int, float):
        raise TypeError("a must be an integer")
    if type(b) not in (int,float):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
