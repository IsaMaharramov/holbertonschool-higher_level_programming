class Square:
    """Defines a square by size with area-based comparisons."""

    def __init__(self, size=0):
        """Initialize the square with a given size."""
        self.size = size

    @property
    def size(self):
        """Retrieve the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square with type and value validation."""
        if not isinstance(value, (int, float)):
            raise TypeError("size must be a number")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Calculate and return the current square area."""
        return self.__size ** 2

    # Rich Comparison Methods
    def __eq__(self, other):
        """Check if area is equal to another square's area."""
        return self.area() == other.area()

    def __ne__(self, other):
        """Check if area is not equal to another square's area."""
        return self.area() != other.area()

    def __lt__(self, other):
        """Check if area is less than another square's area."""
        return self.area() < other.area()

    def __le__(self, other):
        """Check if area is less than or equal to another square's area."""
        return self.area() <= other.area()

    def __gt__(self, other):
        """Check if area is greater than another square's area."""
        return self.area() > other.area()

    def __ge__(self, other):
        """Check if area is greater than or equal to another square's area."""
        return self.area() >= other.area()
