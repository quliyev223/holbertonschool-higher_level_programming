#!/usr/bin/python3
"""Defines a Rectangle class with width, height, area, perimeter,
and string representation using '#' characters.
"""

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
        """Width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Return the area of the rectangle."""
        return self.width * self.height

    def perimeter(self):
        """Return the perimeter of the rectangle.

        If either width or height is 0, perimeter is 0.
        """
        if self.__width == 0 or self.height == 0:
            return 0
        return 2 * (self.width + self.height)

    def __str__(self):
        """Return the rectangle as a string of '#' characters.

         If width or height is 0, return an empty string.
        """
        if self.width == 0 or self.height == 0:
            return ""
        return "\n".join(["#" * self.width for _ in range(self.height)])

    def __repr__(self):
        """Return a string representation of the rectangle object."""
        return f"<{__name__}.Rectangle object at {hex(id(self))}>"
