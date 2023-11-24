#!/usr/bin/python3
'''class Square that defines a square by: (based on 2-square.py)'''


class Square:
    '''
    You are not allowed to import any module
    '''
    def __init__(self, size=0):
         '''
         Private instance attribute
         nstantiation with optional
         '''
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
             '''
             that returns the current square area
             '''
        return self.__size * self.__size
