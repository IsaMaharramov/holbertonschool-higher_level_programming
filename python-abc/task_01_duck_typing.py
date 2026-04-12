#!/usr/bin/env python3
"""
This module defines an abstract class Shape and its subclasses
Circle and Rectangle to demonstrate ABCs and duck typing in Python.
"""
from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """
    Abstract class that defines the blueprint for geometric shapes.
    """

    @abstractmethod
    def area(self):
        """
        Abstract method to calculate the area of the shape.
        """
        pass

    @abstractmethod
    def perimeter(self):
        """
        Abstract method to calculate the perimeter of the shape.
        """
        pass


class Circle(Shape):
    """
    Concrete class representing a circle that inherits from Shape.
    """

    def __init__(self, radius):
        """
        Initializes a new Circle instance with a given radius.
        """
        self.radius = radius

    def area(self):
        """
        Calculates and returns the area of the circle.
        """
        return math.pi * (self.radius ** 2)

    def perimeter(self):
        """
        Calculates and returns the perimeter of the circle.
        """
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    """
    Concrete class representing a rectangle that inherits from Shape.
    """

    def __init__(self, width, height):
        """
        Initializes a new Rectangle instance with width and height.
        """
        self.width = width
        self.height = height

    def area(self):
        """
        Calculates and returns the area of the rectangle.
        """
        return self.width * self.height

    def perimeter(self):
        """
        Calculates and returns the perimeter of the rectangle.
        """
        return 2 * (self.width + self.height)


def shape_info(shape):
    """
    Prints the area and perimeter of a given shape using duck typing.

    Args:
        shape: An object that should have area and perimeter methods.
    """
    print("Area: {}".format(shape.area()))
    print("Perimeter: {}".format(shape.perimeter()))
