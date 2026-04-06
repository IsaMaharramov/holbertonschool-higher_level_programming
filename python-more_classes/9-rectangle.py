#!/usr/bin/python3
"""
This module defines a Rectangle class with a class method to create a square.
"""


class Rectangle:
    """Defines a rectangle with tracking, comparison, and square factory."""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initializes a new Rectangle."""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Retrieves width."""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets width with validation."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Retrieves height."""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets height with validation."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Returns the rectangle area."""
        return self.width * self.height

    def perimeter(self):
        """Returns the rectangle perimeter."""
        if self.width == 0 or self.height == 0:
            return 0
        return (self.width * 2) + (self.height * 2)

    def __str__(self):
        """Returns string representation of the rectangle."""
        if self.width == 0 or self.height == 0:
            return ""
        rect_lines = []
        for i in range(self.height):
            rect_lines.append(str(self.print_symbol) * self.width)
        return "\n".join(rect_lines)

    def __repr__(self):
        """Returns string representation to recreate the instance."""
        return "Rectangle({:d}, {:d})".format(self.width, self.height)

    def __del__(self):
        """Decrements instance counter and prints message on deletion."""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Compares two rectangles based on area."""
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2

    @classmethod
    def square(cls, size=0):
        """Returns a new Rectangle instance with width == height == size."""
        return cls(size, size)
