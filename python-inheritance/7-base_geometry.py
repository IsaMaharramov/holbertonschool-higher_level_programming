#!/usr/bin/python3
"""
This module defines the BaseGeometry class with validation methods.
"""


class BaseGeometry:
    """
    A class used as a base for geometry-related calculations and validation.
    """

    def area(self):
        """
        An unimplemented method for calculating area.

        Raises:
            Exception: Always, with the message 'area() is not implemented'.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates that a value is a positive integer.

        Args:
            name (str): The name of the parameter being validated.
            value (int): The value to validate.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than or equal to 0.
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
