#!/usr/bin/python3
"""
This module defines a Node class and a SinglyLinkedList class.
The SinglyLinkedList allows for sorted insertion of integer data.
"""


class Node:
    """
    Defines a node of a singly linked list.

    Attributes:
        data (int): The integer value stored in the node.
        next_node (Node): The next node in the list.
    """

    def __init__(self, data, next_node=None):
        """
        Initializes a new Node.

        Args:
            data (int): The data for the node.
            next_node (Node): The next node in the list.
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Retrieves the data of the node."""
        return self.__data

    @data.setter
    def data(self, value):
        """Sets the data of the node with type validation."""
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Retrieves the next_node of the node."""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """Sets the next_node with type validation."""
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """
    Defines a singly linked list.

    Attributes:
        head: The first node of the list.
    """

    def __init__(self):
        """Initializes an empty SinglyLinkedList."""
        self.__head = None

    def __str__(self):
        """
        Returns a string representation of the list.
        Each node's data is printed on a new line.
        """
        values = []
        current = self.__head
        while current is not None:
            values.append(str(current.data))
            current = current.next_node
        return "\n".join(values)

    def sorted_insert(self, value):
        """
        Inserts a new Node into the correct sorted position (increasing order).

        Args:
            value (int): The value to insert into the list.
        """
        new_node = Node(value)

        # Handle empty list or insertion at the head
        if self.__head is None or self.__head.data >= value:
            new_node.next_node = self.__head
            self.__head = new_node
        else:
            # Locate the node before the point of insertion
            current = self.__head
            while (current.next_node is not None and
                   current.next_node.data < value):
                current = current.next_node

            new_node.next_node = current.next_node
            current.next_node = new_node
