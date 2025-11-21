#!/usr/bin/python3
from abc import ABC, abstractmethod
import math


#Abstract base class Shape
class Shape(ABC):
    @abstractmethod
    def area(self):
        """Return the area of the shape"""
        pass

    @abstractmethod
    def perimeter(self):
        """Return the perimeter of the shape"""
        pass


# Rectangle class, inherits from Shape
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        # Area formula: width * height
        return self.width * self.height

    def perimeter(self):
        # Perimeter formula: 2 * (width + height)
        return 2 * (self.width + self.height)


# Circle class, inherits from Shape
class Circle(Shape):
    def __init__(self, radius):
        self.radius = abs(radius)

    def area(self):
        # Area formula: p * r^2
        return math.pi * (self.radius ** 2)

    def perimeter(self):
        #Perimeter formuls: 2 * p * r
        return 2 * math.pi * self.radius


# Function using duck typing to print shape info 
def shape_info(shape):
    # We assume the object has area() and perimeter methods
    print(f"Area: {shape.area()}")
    print(f"Perimeter: {shape.perimeter()}")

# Testing the classes and function
if __name__ == "__main__":
    circle = Circle(radius=5)
    rectangle = Rectangle(width=4, height=7)


    shape_info(circle)
    shape_info(rectangle)
