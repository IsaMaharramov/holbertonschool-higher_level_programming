#!/usr/bin/python3
"""
This module defines a class MyList that inherits from the built-in list.
"""


class MyList(list):
    """
    A custom list class that provides additional sorting functionality.
    """

    def print_sorted(self):
        """
        Prints the elements of the list in ascending sorted order.
        The original list remains unchanged.
        """
        print(sorted(self))
