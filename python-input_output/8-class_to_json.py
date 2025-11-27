#!/usr/bin/python3
"""Function that returns a dictionary description for JSON serialization."""


def class_to_json(obj):
    """Return a dictionary of simple data structure attributes of obj."""
    return obj.__dict__.copy()
