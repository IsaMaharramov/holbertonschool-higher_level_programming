#!/usr/bin/python3
"""
This module defines a Square class.
It includes size and position validation, area calculation,
and custom printing capabilities.
"""


class Square:
    """
    Represents a square.

    Attributes:
        size (int): The length of a side of the square.
        position (tuple): The (x, y) coordinates for printing the square.
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes a new Square.

        Args:
            size (int): The size of the new square.
            position (tuple): The position of the new square.
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Retrieves the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the size of the square with validation."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Retrieves the position of the square."""
        return self.__size

    @position.setter
    def position(self, value):
        """Sets the position of the square with validation."""
        if (not isinstance(value, tuple) or len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Returns the current square area."""
        return self.__size ** 2

    def __str__(self):
        """Defines the printable representation of the Square instance."""
        if self.__size == 0:
            return ""

        res = []
        # Add the vertical offset (y-coordinate)
        for _ in range(self.__position[1]):
            res.append("")

        # Add the square rows with horizontal offset (x-coordinate)
        for _ in range(self.__size):
            res.append(" " * self.__position[0] + "#" * self.__size)

        return "\n".join(res)

    def my_print(self):
        """Prints the square with the # character to stdout."""
        print(self.__str__())
