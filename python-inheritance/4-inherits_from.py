#!/usr/bin/python3
"""
Module 4-inherits_from
Contains a function that returns True if an object is an instance
of a class that inherited from a specified class, otherwise False.
"""


def inherits_from(obj, a_class):
    """Return True if obj is an instance of a subclass of a_class.
    False if obj is an instance of a_class itself or not related.
    """
    return isinstance(obj, a_class) and type(obj) is not a_class
