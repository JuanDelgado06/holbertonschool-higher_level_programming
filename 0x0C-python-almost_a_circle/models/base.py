#!/usr/bin/python3
""" 
Base Class.
"""
import json


class Base:
    """ Base Class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """ Initialize a Base"""
        if id is  not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Return the JSON string representation of list_dictionaries."""
        if not list_dictionaries or list_dictionaries is None:
            return '[]'
        return json.dumps(list_dictionaries)
