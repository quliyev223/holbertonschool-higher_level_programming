#!/usr/bin/python3
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

    if line.strip():
        print(line.strip())
