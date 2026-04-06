#!/usr/bin/python3
import sys

def safe_function(fct, *args):
    try:
        return fct(*args)
    except Exception as e:
        # Use print with file=sys.stderr to ensure correct stream handling
        print("Exception: {}".format(e), file=sys.stderr)
        return None
