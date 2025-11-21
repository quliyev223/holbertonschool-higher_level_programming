#!/usr/bin/python3
"""
Module 1-my_list
Defines class MyList that inherits from list
"""


class MyList(list):
    """Custom list class inheriting from list"""

    def print_sorted(self):
        """
        Prints the list, but sorted in ascending order
        Does NOT modify the original list
        """
        print(sorted(self))
