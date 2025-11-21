#!/usr/bin/python3
"""
Module 2-is_same_class
Contains a function that returns True if an object is exactly
an instance of a specified class, otherwise False.
"""

def is_same_class(obj, a_class):
    """Return True if obj is exactly an instance of a_class."""
    return type(obj) is a_class
