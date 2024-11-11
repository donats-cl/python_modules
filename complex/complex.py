from math import *
from vec import *
from maths import *
from functools import *


@total_ordering
class Complex:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag
    
    def __add__(self, other):
        return Complex(self.real + other.real, self.imag + other.imag)
    
    def __sub__(self, other):
        return Complex(self.real - other.real, self.imag - other.imag)
    
    def __mul__(self, other):
        real_part = self.real * other.real - self.imag * other.imag
        imag_part = self.real * other.imag + self.imag * other.real
        return Complex(real_part, imag_part)
    
    def __truediv__(self, other):
        denominator = other.real**2 + other.imag**2
        real_part = (self.real * other.real + self.imag * other.imag) / denominator
        imag_part = (self.imag * other.real - self.real * other.imag) / denominator
        return Complex(real_part, imag_part)
    
    def __str__(self):
        return f"{show_sqrt(self.real)} - {show_sqrt(abs(self.imag))}i" if self.imag < 0 else f"{show_sqrt(self.real)} + {show_sqrt(self.imag)}i"
    
    def __eq__(self, other):
        return self.real == other.real and self.imag == other.imag
    
    def __gt__(self, other):
        return self.real > other.real and self.imag > other.imag
    
    def pow(self, v):
        res = self
        for _ in range(1, v):
            res = res * res
        return res

    def __invert__(self):
        return Complex(self.real, -self.imag)
    
    def vec(self):
        len = sqrt(self.real**2 + self.imag**2)
        ang = atan2(self.real, self.imag)*180/pi

        return vec2(len, ang if ang > 0 else 180+ang)
    
    def raw(self):
        return self.real, self.imag
