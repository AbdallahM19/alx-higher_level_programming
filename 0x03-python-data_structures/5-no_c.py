#!/usr/bin/python3
def no_c(my_string):
    return_str = ""
    for i in range(len(my_string)):
        if (my_string[i] != 'C' and my_string[i] != 'c') :
            return_str += my_string[i]
    return return_str
