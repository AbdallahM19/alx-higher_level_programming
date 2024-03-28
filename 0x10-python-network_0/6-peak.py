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
    list_of_integers.sort(reverse=True)
    return list_of_integers[0]
