#!/usr/bin/python3
for c in range(97, 123):
    if chr(c) == 'q' or chr(c) == 'e':
        continue
    else:
        print("{}".format(chr(c)), end="")
