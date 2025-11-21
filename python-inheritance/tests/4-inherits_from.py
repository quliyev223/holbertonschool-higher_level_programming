#!/usr/bin/python3
def inherits_from(obj, a_class):
    """Return True if obj is an instance of a subclass of a_class.
    False if obj is an instance of a_class itself or not related.
    """
    return isinstance(obj, a_class) and type(obj) is not a_class
