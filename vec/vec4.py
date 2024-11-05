from math import *
from maths import *


class vec4:
    def __init__(self, x=0, y=0, z=0, w=0):
        self.x = x
        self.y = y
        self.z = z
        self.w = w

    def __str__(self):
        return f"({show_sqrt(self.x)}, {show_sqrt(self.y)}, {show_sqrt(self.z)}, {show_sqrt(self.w)})"

    def from_point(self, A, B):
        self.x = B.x-A.x
        self.y = B.y-A.y
        self.z = B.z-A.z
        self.w = B.w-A.w
    
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
