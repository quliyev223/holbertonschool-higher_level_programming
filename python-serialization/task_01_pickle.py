#!/usr/bin/python3
import pickle


class CustomObject:
    """class displays attributes
    Args:
        name: string
        age: integer
        is_student: boolean
    """
    def __init__(self, name, age, is_student):
        self.name = name
        self.age = age
        self.is_student

    def display(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        """Serializes the current instance and saves it to a file."""
        try:
            with open(filename, 'wb') as f
                pickle.dump(self, f)
        except:
            return None


    @classmethod
    def deserialize(cls, filename):
        """method returns instance of custom object"""
        try:
            with open(filename, "rb") as f:
                ret = pickle.load(f)
                return ret
        except:
            return None

         

