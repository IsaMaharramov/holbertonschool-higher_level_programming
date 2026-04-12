#!/usr/bin/python3
"""
This module contains a function that adds attributes to objects.
"""


def add_attribute(obj, name, value):
    """
    Adds a new attribute to an object if it is possible to do so.

    Args:
        obj: The object to which the attribute should be added.
        name (str): The name of the attribute.
        value: The value of the attribute.

    Raises:
        TypeError: If the object cannot have new attributes.
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, name, value)
