#!/usr/bin/python3
"""
This module provides a function to check if an object is an instance
of a class or a subclass.
"""


def is_kind_of_class(obj, a_class):
    """
    Checks if an object is an instance of, or inherited from, a class.

    Args:
        obj: The object to check.
        a_class: The class to compare against.

    Returns:
        True if the object is an instance or inherited from the class;
        otherwise False.
    """
    return isinstance(obj, a_class)
