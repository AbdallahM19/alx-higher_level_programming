#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for n in matrix:
        for i, j in enumerate(n):
            if i == len(n) - 1:
                print("{:d}".format(j), end="")
            else:
                print("{:d}".format(j), end=" ")
        print()
