#!/usr/bin/python3
"""
This is the "write file" module.
"""


def write_file(filename="", text=""):
    """Write a string to a text file."""
    with open(filename, 'w') as f:
        return f.write(str(text))
