from math import *
from maths import *
from .vec2 import *

from functools import *


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
    
    @property
    def yzx(self):
        return vec3(self.y, self.z, self.x)
    
    @property
    def zxy(self):
        return vec3(self.z, self.x, self.y)
    
    @property
    def xzy(self):
        return vec3(self.x, self.z, self.y)
    
    @property
    def zyx(self):
        return vec3(self.z, self.y, self.x)
    
    @property
    def yxz(self):
        return vec3(self.y, self.x, self.z)
