#!/usr/bin/python3
'''a function that writes a string to a text file
(UTF8) and returns the number of characters written'''

def write_file(filename="", text=""):
    '''
    You must use the with statement
    You don’t need to manage file permission exceptions.
    Your function should create the file if doesn’t exist.
    '''
    with open(filename, "w",encoding="utf-8") as f:
        return f.write(text)
