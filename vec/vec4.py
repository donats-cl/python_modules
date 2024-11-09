from math import *
from maths import *
from .vec2 import *
from .vec3 import *

from functools import *


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

    @property
    def xyzw(self):
        return vec4(self.x, self.y, self.z, self.w)

    @property
    def xzyw(self):
        return vec4(self.x, self.z, self.y, self.w)

    @property
    def xzwy(self):
        return vec4(self.x, self.z, self.w, self.y)

    @property
    def xwyz(self):
        return vec4(self.x, self.w, self.y, self.z)

    @property
    def xwzy(self):
        return vec4(self.x, self.w, self.z, self.y)

    @property
    def yxzw(self):
        return vec4(self.y, self.x, self.z, self.w)

    @property
    def yxwz(self):
        return vec4(self.y, self.x, self.w, self.z)

    @property
    def yzwx(self):
        return vec4(self.y, self.z, self.w, self.x)

    @property
    def ywzx(self):
        return vec4(self.y, self.w, self.z, self.x)

    @property
    def ywxz(self):
        return vec4(self.y, self.w, self.x, self.z)

    @property
    def zxyw(self):
        return vec4(self.z, self.x, self.y, self.w)

    @property
    def zxwy(self):
        return vec4(self.z, self.x, self.w, self.y)

    @property
    def zywx(self):
        return vec4(self.z, self.y, self.w, self.x)

    @property
    def zyxw(self):
        return vec4(self.z, self.y, self.x, self.w)

    @property
    def zwxy(self):
        return vec4(self.z, self.w, self.x, self.y)

    @property
    def zwyx(self):
        return vec4(self.z, self.w, self.y, self.x)

    @property
    def wxyz(self):
        return vec4(self.w, self.x, self.y, self.z)

    @property
    def wxzy(self):
        return vec4(self.w, self.x, self.z, self.y)

    @property
    def wyxz(self):
        return vec4(self.w, self.y, self.x, self.z)

    @property
    def wyzx(self):
        return vec4(self.w, self.y, self.z, self.x)

    @property
    def wzxy(self):
        return vec4(self.w, self.z, self.x, self.y)

    @property
    def wzyx(self):
        return vec4(self.w, self.z, self.y, self.x)
    
    @property
    def len(self):
        return sqrt(pow(self.x,2)+pow(self.y,2)+pow(self.z,2)+pow(self.w,2))
    
    def __add__(self, b):
        return vec4(self.x+b.x, self.y+b.y, self.z+b.z, self.w+b.w)
    
    def __sub__(self, b):
        return vec4(self.x-b.x, self.y-b.y, self.z-b.z, self.w-b.w)
    
    def __mul__(self, v):
        return vec4(self.x*v, self.y*v, self.z*v, self.w*v)
    
    def __truediv__(self, v):
        return vec4(self.x/v, self.y/v, self.z/v, self.w*v)
