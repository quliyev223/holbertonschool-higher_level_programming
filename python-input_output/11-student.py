#!/usr/bin/python3
"""Student class module with serialization/deserialization"""


class Student:
    """Defines a student"""

    def __init__(self, first_name, last_name, age):
        """Initialize a Student instance"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieves a dictionary representation of a Student instance.

        If attrs is a list of strings, only attributes contained in this list
        will be included. Otherwise, all attributes are included.
        """
        if isinstance(attrs, list) and all(isinstance(a, str) for a in attrs):
            return {a: getattr(self, a) for a in attrs if hasattr(self, a)}
        return self.__dict__.copy()

    def reload_from_json(self, json):
        """
        Replaces all attributes of the Student instance with values from json.

        json: a dictionary with key-value pairs matching attribute names and values
        """
        for key, value in json.items():
            setattr(self, key, value)
