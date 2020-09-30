#!/usr/bin/python3
def magic_string(n=[0]):
    n[0] += 1
    return ('Holberton, ' * (n[0] - 1)) + 'Holberton'
