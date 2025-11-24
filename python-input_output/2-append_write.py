#!/usr/bin/python3
"""This module provides a function to append text to a UTF-8 file.
If the file does not exist, it will be created.
"""


def append_write(filename="", text=""):
    """Appends a string at the end of a UTF-8 text file and returns
    the number of characters added.

    Args:
        filename (str): The name of the file to write to.
        text (str): The text to append to the file.

    Returns:
        int: The number of characters added to the file.
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)

