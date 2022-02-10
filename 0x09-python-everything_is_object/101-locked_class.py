#!/usr/bin/python3
"""class LockedClass with no class or object attribute"""
class LockedClass:
    """
    You are not allowed to import any module
    """
    _slots_ = ["first_name"]
