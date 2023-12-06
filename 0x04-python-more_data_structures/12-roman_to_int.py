#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or roman_string is None:
        return 0
    value = 0
    current_value = 0
    roman = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    for i in reversed(roman_string):
        current_value = roman[i]
        value += current_value if value < 5 * current_value else -current_value
    return value
