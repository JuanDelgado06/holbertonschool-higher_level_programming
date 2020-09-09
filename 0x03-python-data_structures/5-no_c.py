#!/usr/bin/python3
def no_c(my_string):
    c_list = []
    for i in my_string:
        if i != 'c' and i != 'C':
            c_list.append(i)
    return ''.join(c_list)
