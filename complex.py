#!/usr/bin/env python3


# ME499-S20 Python Lab 5
# Programmer: Jacob Gray
# Last Edit: 5/12/2020


from random import randint
from numbers import Number
import numpy as np


def compare_test(a, b):
    """
    Compares integers a and b and raises ValueError if they're not equal.
    :param a: Integer.
    :param b: Integer.
    :return: Raises ValueError if integers a and b are not equal, does nothing otherwise.
    """
    if a != b:
        raise ValueError


class Complex():

    def __init__(self, re=0, im=0):
        self.re = float(re)  # Real component
        self.im = float(im)  # Imaginary component

    def __str__(self):
        if self.im < 0:
            template = '({} - {}i)'
            return template.format(self.re, abs(self.im))

        else:
            template = '({} + {}i)'
            return template.format(self.re, self.im)

    def __repr__(self):
        self.__str__()

    def __add__(self, other):
        if isinstance(other, Complex):
            return Complex(self.re + other.re, self.im + other.im)
        elif isinstance(other, Number):
            return Complex(self.re + other, self.im)
        else:
            return TypeError(
                "Math hasn't figured out how to add a complex number to a {} yet".format(type(other).__name__))

    def __radd__(self, other):
        if isinstance(other, Complex):
            return Complex(self.re + other.re, self.im + other.im)
        elif isinstance(other, Number):
            return Complex(self.re + other, self.im)
        else:
            return TypeError(
                "Math hasn't figured out how to add a complex number to {} yet".format(type(other).__name__))

    def __mul__(self, other):
        if isinstance(other, Complex):
            return Complex((self.re * other.re) - (self.im * other.im),
                           (self.re * other.im) + (self.im * other.re))
        elif isinstance(other, Number):
            return Complex(self.re * other, self.im * other)
        else:
            return TypeError("Math hasn't figured out how to multiply a "
                             "complex number to a {} yet".format(type(other).__name__))

    def __rmul__(self, other):
        if isinstance(other, Complex):
            return Complex((self.re * other.re) - (self.im * other.im),
                           (self.re * other.im) + (self.im * other.re))
        elif isinstance(other, Number):
            return Complex(self.re * other, self.im * other)
        else:
            return TypeError("Math hasn't figured out how to multiply a "
                             "complex number to a {} yet".format(type(other).__name__))

    def __sub__(self, other):
        if isinstance(other, Complex):
            return Complex(self.re - other.re, self.im - other.im)
        elif isinstance(other, Number):
            return Complex(self.re - other, self.im)
        else:
            return TypeError("Math hasn't figured out how to subtract a {} from a "
                             "complex number yet".format(type(other).__name__))

    def __rsub__(self, other):
        if isinstance(other, Complex):
            return Complex(other.re - self.re, other.im - self.im)
        elif isinstance(other, Number):
            return Complex(other - self.re, self.im)
        else:
            return TypeError("Math hasn't figured out how to subtract a complex number from a "
                             "{} number yet".format(type(other).__name__))

    def __truediv__(self, other):
        if isinstance(other, Complex):
            return Complex((self.re * other.re + self.im * other.im) / (other.re ** 2 + other.im ** 2),
                           (self.im * other.re - self.re * other.im) / (other.re ** 2 + other.im ** 2))
        elif isinstance(other, Number):
            return Complex(self.re * (other ** -1), self.im * (other ** -1))
        else:
            return TypeError("Math hasn't figured out how to divide an "
                             "imaginary number by a {] yet".format(type(other).__name__))


if __name__ == '__main__':
    # Testing my complex numbers vs numpys
    for i in range(1000):
        a = randint(-500, 500)
        b = randint(-500, 500)
        c = randint(-500, 500)
        d = randint(-500, 500)
        my_complex1 = Complex(a, b)
        my_complex2 = Complex(c, d)
        np_complex1 = np.complex(a, b)
        np_complex2 = np.complex(c, d)
