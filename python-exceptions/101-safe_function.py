#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        result = fct(*args)
        return result
    except Exception as error_execution:
        sys.stderr.write("Exception: {}\n".format(error_execution))
        return None
