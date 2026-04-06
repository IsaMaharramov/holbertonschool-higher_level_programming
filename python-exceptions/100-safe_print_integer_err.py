#!/usr/bin/python3
import sys


def safe_print_integer_err(value):

    try:
        # Try to convert the value to an integer and prints it
        print("{:d}".format(int(value)))
        # Returns True to indicate that the value was printed correctly
        return True
    except ValueError:
        # On error, print an error message to stderr
        print("Exception: Cannot print as integer", file=sys.stderr)
        # Return False to indicate that the value was not printed correctly
        return False