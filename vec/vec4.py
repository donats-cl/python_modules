from math import sqrt
from maths import show_sqrt
from .vec2 import *
from .vec3 import *

from functools import singledispatchmethod


class vec4:
    @singledispatchmethod
    def __init__(self, x=0, y=0, z=0, w=0):
        self.x = x
        self.y = y
        self.z = z
        self.w = w
        
    @__init__.register
    def _(self, v: vec3, w):
        self.x = v.x
        self.y = v.y
        self.z = v.z
        self.w = w
    
    @__init__.register
    def _(self, a: vec2, b: vec2):
        self.x = a.x
        self.y = a.y
        self.z = b.x
        self.w = b.y

    def __str__(self):
        return f"({show_sqrt(self.x)}, {show_sqrt(self.y)}, {show_sqrt(self.z)}, {show_sqrt(self.w)})"

    def from_point(self, A, B):
        self.x = B.x-A.x
        self.y = B.y-A.y
        self.z = B.z-A.z
        self.w = B.w-A.w
    
    def norm(self):
        return vec4(self.x/self.len, self.y/self.len, self.z/self.len, self.w/self.len)
    
    def __getattr__(self, name):
        v = [i for i in name]
        if len(v) == 2:
            return vec2(getattr(self, v[0]), getattr(self, v[1]))
        elif len(v) == 3:
            return vec3(getattr(self, v[0]), getattr(self, v[1]), getattr(self, v[2]))
        else:
            return vec4(getattr(self, v[0]), getattr(self, v[1]), getattr(self, v[2]), getattr(self, v[3]))
        
    @property
    def len(self):
        return sqrt(pow(self.x,2)+pow(self.y,2)+pow(self.z,2)+pow(self.w,2))
    
    def __add__(self, b):
        return vec4(self.x+b.x, self.y+b.y, self.z+b.z, self.w+b.w)
    
    def __sub__(self, b):
        return vec4(self.x-b.x, self.y-b.y, self.z-b.z, self.w-b.w)
    
    def __mul__(self, v):
        return vec4(self.x*v, self.y*v, self.z*v, self.w*v)
    
    def __matmul__(self, v):
        ... 
    
    def __truediv__(self, v):
        return vec4(self.x/v, self.y/v, self.z/v, self.w*v)
