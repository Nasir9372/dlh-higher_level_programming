#!/usr/bin/python3
import hidden_4
if __name__ == "__main__":
    # get names from hidden and use dir() to return names in string form
    names = dir(hidden_4)
    # loop over sorted names
    for name in sorted(names):
        if not name.startswith("__"):
            print(name)
