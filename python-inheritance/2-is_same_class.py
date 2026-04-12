#!/usr/bin/python3
"""
This module provides a function to verify the exact class of an object.
"""


def is_same_class(obj, a_class):
    """
    Determines if an object is exactly an instance of a specific class.

    Args:
        obj: The object to check.
        a_class: The class to compare against.

    Returns:
        True if the object is exactly an instance of the class;
        otherwise False.
    """
    return type(obj) is a_class
