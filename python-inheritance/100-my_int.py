#!/usr/bin/python3
"""
This module defines the rebel class MyInt that inherits from int.
"""


class MyInt(int):
    """
    A class that inherits from int but has == and != operators inverted.
    """

    def __eq__(self, other):
        """
        Overrides the equality operator to return the opposite.

        Args:
            other: The value to compare against.

        Returns:
            True if the values are not equal, False otherwise.
        """
        return super().__ne__(other)

    def __ne__(self, other):
        """
        Overrides the inequality operator to return the opposite.

        Args:
            other: The value to compare against.

        Returns:
            True if the values are equal, False otherwise.
        """
        return super().__eq__(other)
