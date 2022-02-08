#!/usr/bin/python3
'''
Write a class Square that defines a square by: (based on 0-square.py)
'''


class Square:
    '''
    Private instance attribute: size
    Instantiation with size (no type/value verification)
    You are not allowed to import any module
    '''

    def __init__(self, size):
        '''
        The size of a square is crucial for a square
        '''
        self.__size = size
