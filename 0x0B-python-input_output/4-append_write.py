#!/usr/bin/python3
"""
This is the "append write" module.
"""


def append_write(filename="", text=""):
    """Append a string at the end of a text file."""
    with open(filename, 'a') as f:
        return f.write(str(text))
