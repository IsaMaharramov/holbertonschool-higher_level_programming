# Python - More Classes and Objects

## Tutorial
[Object Oriented Programming](https://python.swaroopch.com/oop.html)

[Object Oriented Programming](https://python-course.eu/oop/object-oriented-programming.php)

[Class vs. Instance Attributes](https://python-course.eu/oop/class-instance-attributes.php)

[Python OOP Tutorial 3: classmethods and staticmethods](https://youtu.be/rq8cL2XMM5M?si=9ciDQqHnqolKjk80)

[Properties vs. Getters and Setters](https://python-course.eu/oop/properties-vs-getters-and-setters.php)

[Python's str() vs. repr()](https://shipit.dev/posts/python-str-vs-repr.html)

## Project Overview
This repository contains a series of exercises focused on **Object-Oriented Programming (OOP)** in Python. The goal is to build a robust `Rectangle` class from scratch, incrementally adding advanced features like data validation, property decorators, magic methods, class attributes, and static/class methods.

## Learning Objectives
* **Encapsulation:** Protecting attributes using private variables (`__width`, `__height`).
* **Properties:** Using `@property` and `@width.setter` for data validation.
* **Magic Methods:** Implementing `__str__`, `__repr__`, and `__del__`.
* **Class vs Instance:** Managing state with class attributes (`number_of_instances`).
* **Method Types:** Using `@staticmethod` for utility and `@classmethod` for factories (e.g., `square`).

---

## File Directory & Evolution

| File | Task | Key Features Added |
| :--- | :--- | :--- |
| `0-rectangle.py` | Simple rectangle | Empty class definition. |
| `1-rectangle.py` | Real definition | Private attributes with type/value validation. |
| `2-rectangle.py` | Area and Perimeter | Public instance methods for calculations. |
| `3-rectangle.py` | String representation | `print()` support using `#`. |
| `4-rectangle.py` | Eval-ready | `repr()` support to recreate instances via `eval()`. |
| `5-rectangle.py` | Detect deletion | Destructor (`__del__`) with exit message. |
| `6-rectangle.py` | How many instances | Class attribute to track active objects. |
| `7-rectangle.py` | Change symbol | Customizable `print_symbol` for the string representation. |
| `8-rectangle.py` | Compare rectangles | Static method to find the larger rectangle by area. |
| `9-rectangle.py` | A square is a rectangle | Class method factory to create a square. |

---

## Requirements
- **Language:** Python 3.8.x
- **Style Guide:** [Pycodestyle](https://pypi.org/project/pycodestyle/) (formerly PEP 8)
- **Environment:** Ubuntu 20.04 LTS (or similar)
- **Constraints:** No external modules imported.

## Usage
To test any of the classes, use the provided main files:

```bash
# Example: Testing the final Rectangle class (Task 9)
python3 9-main.py
```

## Example Code
```Python
Rectangle = __import__('9-rectangle').Rectangle

# Create a square using the class method factory
my_square = Rectangle.square(5)

print(f"Area: {my_square.area()}")
print(my_square)
# Output:
# Area: 25
# #####
# #####
# #####
# #####
# #####
```

## Author
* [Isa Maharramov](https://github.com/IsaMaharramov)
