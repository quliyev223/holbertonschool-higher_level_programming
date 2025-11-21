#!/usr/bin/python3
"""
Module 3-is_kind_of_class
Contains a function that returns True if an object is an instance of,
or inherits from, a specified class; otherwise False.
"""

def is_kind_of_class(obj, a_class):
    """Return True if obj is an instance of a_class or a subclass of a_class."""
    return isinstance(obj, a_class)
