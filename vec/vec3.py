from math import sqrt
from maths import show_sqrt
from .vec2 import *

from functools import singledispatchmethod


class vec3:
    @singledispatchmethod
    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z
    
    @__init__.register
    def _(self, v: vec2, z):
        self.x = v.x
        self.y = v.y
        self.z = z

    def __str__(self):
        return f"({show_sqrt(self.x)}, {show_sqrt(self.y)}, {show_sqrt(self.z)}"

    def from_point(self, A, B):
        self.x = B.x-A.x
        self.y = B.y-A.y
        self.z = B.z-A.z

    def norm(self):
        return vec3(self.x/self.len, self.y/self.len, self.z/self.len)
    
    # def __getattr__(self, name):
    #     v = [i for i in name]
    #     if len(v) == 2:
    #         return vec2(getattr(self, v[0]), getattr(self, v[1]))
    #     elif len(v) == 3:
    #         return vec3(getattr(self, v[0]), getattr(self, v[1]), getattr(self, v[2]))
    #     else:
    #         return vec4(getattr(self, v[0]), getattr(self, v[1]), getattr(self, v[2]), getattr(self, v[3]))
    
    @property
    def len(self):
        return sqrt(pow(self.x,2)+pow(self.y,2)+pow(self.z,2))
    
    def __add__(self, b):
        return vec3(self.x+b.x, self.y+b.y, self.z+b.z)
    
    def __sub__(self, b):
        return vec3(self.x-b.x, self.y-b.y, self.z-b.z)
    
    def __mul__(self, v):
        return vec3(self.x*v, self.y*v, self.z*v)
    
    def __truediv__(self, v):
        return vec3(self.x/v, self.y/v, self.z/v)
    
    