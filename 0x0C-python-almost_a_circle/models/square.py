#!/usr/bin/python3
"""
Square class.
"""
from models.base import Base
from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class."""
    def __init__(self, size, x=0, y=0, id=None):
        """Initialize a Square instance."""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Print the square attributes."""
        return ('[Square] (' + str(self.id) + ') ' + str(self._Rectangle__x) +
                '/' + str(self._Rectangle__y) + ' - ' +
                str(self._Rectangle__width))
