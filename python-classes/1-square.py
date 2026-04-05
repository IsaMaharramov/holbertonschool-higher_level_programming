#!/usr/bin/python3
"""Module that defines a Square class with a private size attribute."""


class Square:
    """Class that defines a square."""

    def __init__(self, size):
        """Initializes a new Square.

        Args:
            size: The length of a side of the square.
        """
        self.__size = size
