#!/usr/bin/python3
"""Module 1-rectangle
Defines a Rectangle class.
"""


class Rectangle:
    """Rectangle class defined by width and height."""


    def __init__(self, width=0, height=0):
        """Initializes a Rectangle instance.


        Args:
            width: width of the rectangle
            height: height of the rectangle
        """

        self.width = width
        self.height = height


    @property
    def width(self):
        """Retrieves the width of a Rectangle instance"""
        return self.__width


    @width.setter
    def width(self, value):
        """sets the width of a rectangle instance"

        Args:
            value: value of the width, must be a positive integer
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be positive; >= 0")
        self.__width = value


    @property
    def height(self, value):
        """sets the height of a rectangle instance
        Args:
            value: value of the height, must be a positive integer
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value


