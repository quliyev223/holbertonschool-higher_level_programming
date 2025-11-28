#!/usr/bin/python3
"""Defines class and serializes it"""
import pickle


class CustomObject:
    """Class that represents a custom object with attributes:
    Args:
        name: string
        age: integer
        is_student: boolean
    """
    def __init__(self, name, age, is_student):
        """Initializes the CustomObject instance"""
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """Prints out the attributes of the object"""
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        """Serializes the current instance of the object to a file"""
        try:
            with open(filename, "wb") as f:
                pickle.dump(self, f)
        except (IOError, pickle.PicklingError) as e:
            print(f"Error during serialization: {e}")
            return None

    @classmethod
    def deserialize(cls, filename):
        """Deserializes an object from a file and returns an instance"""
        try:
            with open(filename, "rb") as f:
                return pickle.load(f)
        except (FileNotFoundError, pickle.UnpicklingError, IOError) as e:
            print(f"Error during deserialization: {e}")
            return None
