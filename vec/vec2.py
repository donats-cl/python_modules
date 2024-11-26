from math import sqrt
from maths import show_sqrt

from functools import singledispatchmethod
from typing import Self

class vec2:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({show_sqrt(self.x)}, {show_sqrt(self.y)})"
    
    def __getattr__(self, name):
        v = [i for i in name]
        if len(v) == 2:
            return vec2(getattr(self, v[0]), getattr(self, v[1]))

    def from_point(self, A, B):
        self.x = B.x-A.x
        self.y = B.y-A.y

    def norm(self):
        return vec2(self.x/self.len, self.y/self.len)
    
    @property
    def len(self):
        return sqrt(pow(self.x,2)+pow(self.y,2))
    
    def __add__(self, b):
        return vec2(self.x+b.x, self.y+b.y)
    
    def __sub__(self, b):
        return vec2(self.x-b.x, self.y-b.y)
    
    def __mul__(self, v):
        return vec2(self.x*v, self.y*v)
    
    def __truediv__(self, v):
        return vec2(self.x/v, self.y/v)
