#!/usr/bin/python3
"""
This module provides a function to write text to a file in UTF-8 encoding.
The file will be created if it does not exist, and overwritten if it does.
"""


def write_file(filename="", text=""):
     """
    Writes a string to a UTF-8 encoded text file and returns
    the number of characters written.

    Args:
        filename (str): The name of the file to write to.
        text (str): The text content to write.

    Returns:
        int: The number of characters written to the file.
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
