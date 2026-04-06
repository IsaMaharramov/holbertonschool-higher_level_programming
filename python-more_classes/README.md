# Python - More Classes and Objects

## Tutorial
[Object Oriented Programming](https://python.swaroopch.com/oop.html)

[Object Oriented Programming](https://python-course.eu/oop/object-oriented-programming.php)

[Class vs. Instance Attributes](https://python-course.eu/oop/class-instance-attributes.php)

[Python OOP Tutorial 3: classmethods and staticmethods](https://youtu.be/rq8cL2XMM5M?si=9ciDQqHnqolKjk80)

[Properties vs. Getters and Setters](https://python-course.eu/oop/properties-vs-getters-and-setters.php)

[Python's str() vs. repr()](https://shipit.dev/posts/python-str-vs-repr.html)

## Project Overview
This project is a deep dive into **Object-Oriented Programming (OOP)** in Python. The goal is to build a robust `Rectangle` class from the ground up, incrementally adding features like data validation, property decorators, magic methods, class attributes, and factory methods.

## Learning Objectives
* **Encapsulation:** Protecting attributes using private variables (`__width`, `__height`).
* **Data Validation:** Using `@property` and `@setter` to enforce type and value constraints.
* **Magic Methods:** Implementing `__str__` for user-friendly printing, `__repr__` for object recreation, and `__del__` for lifecycle management.
* **Class vs Instance Attributes:** Managing shared state with `number_of_instances` and `print_symbol`.
* **Static & Class Methods:** Using `@staticmethod` for logic comparison and `@classmethod` for factory instantiation (e.g., creating a square).

---

## File Directory & Evolution

| File | Task | Key Features Added |
| :--- | :--- | :--- |
| `0-rectangle.py` | Simple rectangle | Basic empty class definition. |
| `1-rectangle.py` | Real definition | Private attributes with type/value validation. |
| `2-rectangle.py` | Area and Perimeter | Public instance methods for geometric calculations. |
| `3-rectangle.py` | String representation | `str()` and `print()` support using the `#` character. |
| `4-rectangle.py` | Eval-ready | `repr()` support to recreate instances via `eval()`. |
| `5-rectangle.py` | Detect deletion | Destructor (`__del__`) with a "Bye rectangle..." message. |
| `6-rectangle.py` | Instance Tracking | Class attribute to track the number of active objects. |
| `7-rectangle.py` | Change symbol | Customizable `print_symbol` for string representation. |
| `8-rectangle.py` | Compare rectangles | Static method to find the larger rectangle by area. |
| `9-rectangle.py` | Square factory | Class method to create a Square (Rectangle with equal sides). |

---

## Requirements
- **Language:** Python 3.8.x
- **Style Guide:** [Pycodestyle](https://pypi.org/project/pycodestyle/) (formerly PEP 8)
- **Environment:** Ubuntu 20.04 LTS (or similar)
- **Constraints:** No external modules imported.

## Usage
To test the functionality of the final class (Task 9):

```bash
# Ensure the file is executable
chmod +x 9-main.py 9-rectangle.py

# Run the test script
./9-main.py
```

## Example Code
```Python
Rectangle = __import__('9-rectangle').Rectangle

# Create a square using the class method factory
my_square = Rectangle.square(5)

print(f"Area: {my_square.area()} - Perimeter: {my_square.perimeter()}")
print(my_square)

# Change the symbol for this instance
my_square.print_symbol = "&"
print(my_square)
```