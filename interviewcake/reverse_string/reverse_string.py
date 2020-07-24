#!/usr/bin/env python3

def reverse_str(string):
    output = ""
    while string:
        output += string[-1]
        string = string[:-1]
    return (output)

