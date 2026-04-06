#!/usr/bin/python3
import sys


def safe_print_integer_err(value):

    try:
        print("{:d}".format(int(value)))
        return True
    except ValueError:
        sys.stderr.write("Exception: Cannot print as integer\n")
        return False
