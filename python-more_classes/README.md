# Python - More Classes and Objects

## Tutorial
[Object Oriented Programming](https://python.swaroopch.com/oop.html)

[Object Oriented Programming](https://python-course.eu/oop/object-oriented-programming.php)

[Class vs. Instance Attributes](https://python-course.eu/oop/class-instance-attributes.php)

[Python OOP Tutorial 3: classmethods and staticmethods](https://youtu.be/rq8cL2XMM5M?si=9ciDQqHnqolKjk80)

[Properties vs. Getters and Setters](https://python-course.eu/oop/properties-vs-getters-and-setters.php)

[Python's str() vs. repr()](https://shipit.dev/posts/python-str-vs-repr.html)

## Project Overview
This repository focuses on **Object-Oriented Programming (OOP)** and **Algorithmic Problem Solving** in Python. It documents the evolution of a `Rectangle` class—from a simple empty definition to a complex object with data validation and factory methods—and concludes with a backtracking solution for the classic **N Queens puzzle**.

## Learning Objectives
* **Encapsulation:** Protecting attributes using private variables (`__width`, `__height`).
* **Data Validation:** Using `@property` and `@setter` to enforce type and value constraints.
* **Magic Methods:** Implementing `__str__`, `__repr__`, and `__del__` for object lifecycle and representation.
* **Class vs Instance Attributes:** Managing shared state (e.g., `number_of_instances`).
* **Static & Class Methods:** Using `@staticmethod` for logic and `@classmethod` for factories.
* **Backtracking Algorithms:** Implementing a recursive solution to solve the N Queens non-attacking placement challenge.

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
| `101-nqueens.py` | N Queens | Backtracking program to solve the N queens puzzle. |

---

## Requirements
* **Interpreter:** Python 3.8.x
* **Style Guide:** `pycodestyle` (version 2.8.*)
* **Environment:** Ubuntu 20.04 LTS
* **Constraints:** No external modules imported (except `sys` for Task 101).

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