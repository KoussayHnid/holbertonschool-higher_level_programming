#!/usr/bin/python3
'''class Square that defines a square by: (based on 1-square.py)'''


class Square:
    '''
    You are not allowed to import any module
    '''

    def __init__(self, size=0):
        '''
        size must be an integer, otherwise raise a
        TypeError exception with the message size must be an integer
        '''
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
