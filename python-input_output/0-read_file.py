#!/usr/bin/python3
'''function that reads a text file 
(UTF8) and prints it to stdout'''

def read_file(filename=""):
    '''
    using with statement
    i don't need to manage file permission
    im not allowed to import
    '''
    with open(filename, "r", encoding="utf-8") as f:
        print(f.read(), end="")
