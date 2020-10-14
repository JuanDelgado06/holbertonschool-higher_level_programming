#!/usr/bin/python3
""" 
Base Class.
"""
import json
import csv


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
    
    @staticmethod
    def from_json_string(json_string):
        """Return the list of the JSON string representation."""
        if not json_string or json_string is None:
            return []
        return json.loads(json_string)

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Write the CSV representation of list_objs to a file."""
        filename = cls.__name__ + '.csv'
        if list_objs is not None:
            if cls.__name__ == 'Rectangle':
                data = [[obj.id, obj.width, obj.height, obj.x, obj.y]
                        for obj in list_objs]
            else:
                data = [[obj.id, obj.size, obj.x, obj.y] for obj in list_objs]
            with open(filename, 'w', newline='') as f:
                writer = csv.writer(f)
                writer.writerows(data)
