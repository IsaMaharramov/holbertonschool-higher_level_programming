#!/usr/bin/python3
import sys

if __name__ == "__main__":
    arg_count = len(sys.argv) - 1
    if arg_count == 0:
        print("{:d} arguments.".format(arg_count))
    elif arg_count == 1:
        print("{:d} argument:".format(arg_count))
    else:
        print("{:d} arguments:".format(arg_count))
    for i in range(1, arg_count + 1):
        print("{:d}: {}".format(i, sys.argv[i]))
