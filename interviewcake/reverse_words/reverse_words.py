#!/usr/bin/env python3

def reverse_words(words):
    output = ''
    splitted = words.split(' ')
    while splitted :
        output += splitted.pop() + ' '
    return(output.rstrip())

