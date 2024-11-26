from math import *
from vec import *
from maths import *
from functools import *


@total_ordering
class Complex:
    def __init__(self, real=0, imag=0, trig=False):
        if not trig:
            self.real = real
            self.imag = imag
        else:
            self.real = real*cos(dtr(imag))
            self.imag = real*sin(dtr(imag))
    
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
    
    def pow(self, v=2):
        vec = self.vec()
        r = vec.x**v
        return Complex(r*cos(v*dtr(vec.y)), r*sin(v*dtr(vec.y)))
    
    def sqrt(self, v=2):
        vec=self.vec()
        r=vec.x**(1/v)
        complexes=[]

        for i in range(0,v):
            phi=(vec.y+2*pi*i)/v
            complexes.append(Complex(r*cos(dtr(phi)), r*sin(dtr(phi))))

        return complexes

    def __invert__(self):
        return Complex(self.real, -self.imag)
    
    def vec(self):
        len = sqrt(self.real**2 + self.imag**2)
        ang = rtd(atan(self.imag/self.real))

        return vec2(len, ang) # if ang > -1 else 180+ang
    
    def raw(self):
        return self.real, self.imag
