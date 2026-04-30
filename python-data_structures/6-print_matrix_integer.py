#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for integer in range(len(row)):
            if integer != len(row) - 1:
                print("{:d}".format(row[integer]), end="")
            else:
                print("{:d}".format(row[integer]), end=" ")
        print()
