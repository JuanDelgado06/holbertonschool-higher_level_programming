#!/usr/bin/python3
""" 
Rectangle class
"""
from models.base import Base


class Rectangle(Base):
    """Rectangle class."""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize Rectangle"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    def integer_validator(self, name, value):
        """Validate value."""
        if type(value) != int:
            raise TypeError('{} must be an integer'.format(name))
        if value <= 0 and (name == 'width' or name == 'height'):
            raise ValueError('{} must be > 0'.format(name))
        if value < 0 and (name == 'x' or name == 'y'):
            raise ValueError('{} must be >= 0'.format(name))
    
    def area(self):
        """Return the area of the rectangle."""
        return self.__width * self.__height

    @property
    def width(self):
        """Get the width."""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width."""
        self.integer_validator('width', value)
        self.__width = value

    @property
    def height(self):
        """Get the height."""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height."""
        self.integer_validator('height', value)
        self.__height = value

    @property
    def x(self):
        """Get x."""
        return self.__x

    @x.setter
    def x(self, value):
        """Set x."""
        self.integer_validator('x', value)
        self.__x = value

    @property
    def y(self):
        """Get y."""
        return self.__y

    @y.setter
    def y(self, value):
        """Set y."""
        self.integer_validator('y', value)
        self.__y = value
