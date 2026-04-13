#!/usr/bin/python3
"""
This module provides a function to look up object attributes and methods.
"""


def lookup(obj):
    """
    Returns the list of available attributes and methods of an object.

    Args:
        obj: The object to be inspected.

    Returns:
        A list object containing strings of attributes and methods.
    """
    return dir(obj)
