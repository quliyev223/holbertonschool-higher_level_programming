#!/usr/bin/python3
"""
Module that provides a function to create a Python object
from a JSON file.
"""

import json


def load_from_json_file(filename):
    """
    Create a Python object from a JSON file.

    Args:
        filename (str): The name of the JSON file to read.

    Returns:
        object: The Python data structure obtained from the JSON content.

    Note:
        - No exceptions are handled inside this function.
        - If the file doesn't exist, FileNotFoundError will be raised.
        - If the JSON is invalid, JSONDecodeError will be raised.
    """
    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)
