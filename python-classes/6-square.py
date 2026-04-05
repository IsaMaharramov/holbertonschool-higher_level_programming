#!/usr/bin/python3
"""Module that defines a Square class with position and printing logic."""


class Square:
    """Class that defines a square by size and position."""

    def __init__(self, size=0, position=(0, 0)):
        """Initializes a new Square.

        Args:
            size (int): The length of a side of the square.
            position (tuple): The (x, y) coordinates of the square.
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Retrieves the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the size with validation."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Retrieves the position of the square."""
        return self.__size_position

    @position.setter
    def position(self, value):
        """Sets the position with validation for a tuple of 2 positive ints."""
        if (not isinstance(value, tuple) or len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__size_position = value

    def area(self):
        """Returns the current square area."""
        return self.__size * self.__size

    def my_print(self):
        """Prints the square with # and spaces for position."""
        if self.__size == 0:
            print("")
            return

        # Print vertical offset (y-coordinate)
        if self.__size_position[1] > 0:
            for i in range(self.__size_position[1]):
                print("")

        # Print square with horizontal offset (x-coordinate)
        for i in range(self.__size):
            print(" " * self.__size_position[0] + "#" * self.__size)
