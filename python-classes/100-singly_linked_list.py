class Node:
    """Represents a node in a singly linked list."""

    def __init__(self, data, next_node=None):
        """Initializes the node with validation."""
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Getter for the private __data attribute."""
        return self.__data

    @data.setter
    def data(self, value):
        """Setter for __data with type validation."""
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Getter for the private __next_node attribute."""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """Setter for __next_node with type and None validation."""
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """Represents a singly linked list structure."""

    def __init__(self):
        """Initializes an empty linked list."""
        self.__head = None

    def __str__(self):
        """Returns the list data formatted with one value per line."""
        output = []
        temp = self.__head
        while temp is not None:
            output.append(str(temp.data))
            temp = temp.next_node
        return "\n".join(output)

    def sorted_insert(self, value):
        """Inserts a new Node into the list in increasing sorted order."""
        new_node = Node(value)

        # Case 1: List is empty or new value is smaller than the head
        if self.__head is None or self.__head.data >= value:
            new_node.next_node = self.__head
            self.__head = new_node
        else:
            # Case 2: Traverse to find the correct insertion point
            current = self.__head
            while (current.next_node is not None and 
                   current.next_node.data < value):
                current = current.next_node
            
            new_node.next_node = current.next_node
            current.next_node = new_node
