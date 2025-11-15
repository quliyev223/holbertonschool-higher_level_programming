#!/usr/bin/python3
"""Defines a Rectangle class with width and height attributes,
including property getters and setters with validation."""


class Rectangle:
    """Represent a rectangle with private width and height."""

    def __init__(self, width=0, height=0):
        """Initialize a new Rectangle instance.

        Args:
            width (int, optional): Width of the rectangle. Defaults to 0.
            height (int, optional): Height of the rectangle. Defaults to 0.

        Raises:
            TypeError: If width or height is not an integer.
            ValueError: If width or height is less than 0.
        """
        self.width = width
        self.height = height

        @property
        def width(self):
            """Width of the rectangle.

            Raises:
                TypeError: If width is not an integer.
                ValueError: If width is less than 0.
            """
            return self.__width

        @width.setter
        def width(self, value):
            if not isinstance(value, int):
                raise TypeError("widyh must be an integer")
            if value < 0:
                raise ValueError("width must be >+ 0")
            self.__width = value

        @property
        def height(self):
            """Height of the rectangle.

            Raises:
                TypeError: If height is not an integer.
                ValueError: If height is less than 0.
            """
            return self.__height

        @height.setter
        def height(self, value):
            if not isinstance(value, int):
                raise TypeError("height must be an integer")
            if value < 0:
                raise ValueError("height must be >= 0")
            self.__height = value
