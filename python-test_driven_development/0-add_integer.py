#!/usr/bin/python3

"""This is afunction to add two integers."""


def add_integer(a, b=98):
    """Function adds two integers or floats"""
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
