#!/usr/bin/python3
"""
Prints a text with 2 new lines after each
of these characters: ., ? and :
"""


def text_indentation(text):
    """
    Prints a text with 2 new lines after each of
    these characters: ., ? and :

    Args:
        text (str): The input text.

    Raises:
        TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    for i in [".", "?", ":"]:
        text_parts = [line.strip() for line in text.split(i)]
        text = (i + "\n\n").join(text_parts)
    print(text, end="")
