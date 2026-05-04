#!/usr/bin/python3
for i in range(10):
    for j in range(1, 10):
        if i == j:
            continue
        elif i < j and i != 8:
            print("{}".format(i) + "{}".format(j) + ", ", end="")
        elif i < j and i == 8:
            print("{}".format(i) + "{}".format(j))
