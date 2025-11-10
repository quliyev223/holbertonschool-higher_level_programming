#!/usr/bin/python3
"""
This module contains the function text_indentation:
prints a text with 2 new lines after '.', '?' and ':'
"""

def text_indentation(text):
    """Prints a text with 2 new lines after '.', '?' and ':'"""
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    chars = ['.', '?', ':']
    line = ""

    for c in text:
        line += c
        if c in chars:
            print(line.strip())
            print()
            line = ""

    # Print any remaining text that doesn't end with ., ?, :
    if line.strip():
        print(line.strip(), end="")
