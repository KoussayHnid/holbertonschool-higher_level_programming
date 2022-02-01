#!/usr/bin/python3
''' function that appends a string at the end of 
a text file (UTF8) and returns the number of characters added'''
def append_write(filename="", text=""):
    '''
    If the file doesn’t exist, it should be created
    You must use the with statement
    You don’t need to manage file permission
    '''
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
