#!/usr/bin/python3
"""
This is the "load from json file" module.
"""


def load_from_json_file(filename):
    """Create an object from a JSON file."""
    import json
    with open(filename, 'r') as f:
        return json.loads(f.read())
