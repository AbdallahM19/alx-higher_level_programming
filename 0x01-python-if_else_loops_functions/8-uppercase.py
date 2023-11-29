#!/usr/bin/python3
def uppercase(s):
    for c in s:
        if ord('a') <= ord(c) <= ord('z'):
            char = chr(ord(c) - 32)
        else:
            char = c
        print("{:s}".format(char), end="")
    print('')
