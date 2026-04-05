#!/usr/bin/python3
"""Module that defines a Square class with a print method."""


class Square:
    """Class that defines a square by its size and can print it."""

    def __init__(self, size=0):
        """Initializes a new Square instance.

        Args:
            size (int): The length of a side of the square.
        """
        self.size = size

    @property
    def size(self):
        """Retrieves the private instance attribute size."""
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the private instance attribute size with validation.

        Args:
            value (int): The new size of the square.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Calculates and returns the current square area.

        Returns:
            The area of the square (size squared).
        """
        return self.__size ** 2

    def my_print(self):
        """Prints the square with the # character to stdout.

        If size is 0, prints an empty line.
        """
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                print("#" * self.__size)
