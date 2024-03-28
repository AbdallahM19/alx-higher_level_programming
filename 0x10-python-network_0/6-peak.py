#!/usr/bin/python3
"""
Write a function that finds a peak in a list of unsorted integers.
"""


def find_peak(list_of_integers):
    """
    Your algorithm must have the lowest complexity
    (hint: you don’t need to go through
    all numbers to find a peak)
    """
    if not list_of_integers:
        return None

    low = 0
    high = len(list_of_integers) - 1
    while low < high:
        mid = (low + high) // 2
        if list_of_integers[mid] >= list_of_integers[mid + 1]:
            high = mid
        else:
            low = mid + 1
    return list_of_integers[low]
