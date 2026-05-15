#!/usr/bin/python3
import sys
if __name__ == "__main__":
    argument = sys.argv
    count = len(sys.argv) - 1
    if count == 0:
        print("0 arguments.")
    elif count == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(count))

if count >= 1:
    for i in range(1, len(sys.argv)):
        print("{}: {}".format(i, sys.argv[i]))
