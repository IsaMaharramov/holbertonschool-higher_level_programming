#!/usr/bin/python3
import sys

def safe_print_integer_err(value):

    try:
        # Pass value directly to the formatter
        print("{:d}".format(value))
        return True
    except Exception as e:
        # Capture the actual exception object 'e' and print it to stderr
        sys.stderr.write("Exception: {}\n".format(e))
        return False
