#!/usr/bin/env python3
"""
This module defines an abstract class Shape and its subclasses
Circle and Rectangle to demonstrate ABCs and duck typing.
"""
from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """
    Abstract base class for geometric shapes.
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
    Concrete class representing a circle, inheriting from Shape.
    """

    def __init__(self, radius):
        """
        Initializes the Circle with a radius.
        """
        self.radius = radius

    def area(self):
        """
        Returns the area of the circle using the formula PI * r^2.
        """
        return math.pi * (self.radius ** 2)

    def perimeter(self):
        """
        Returns the perimeter of the circle using the formula 2 * PI * r.
        """
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    """
    Concrete class representing a rectangle, inheriting from Shape.
    """

    def __init__(self, width, height):
        """
        Initializes the Rectangle with width and height.
        """
        self.width = width
        self.height = height

    def area(self):
        """
        Returns the area of the rectangle (width * height).
        """
        return self.width * self.height

    def perimeter(self):
        """
        Returns the perimeter of the rectangle (2 * (width + height)).
        """
        return 2 * (self.width + self.height)


def shape_info(shape):
    """
    Prints the area and perimeter of a shape object using duck typing.

    Args:
        shape: An object that implements area() and perimeter() methods.
    """
    print("Area: {}".format(shape.area()))
    print("Perimeter: {}".format(shape.perimeter()))
