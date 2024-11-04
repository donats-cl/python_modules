from math import *


class vec3:
    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z

    def from_point(self, A, B):
        self.x = B.x-A.x
        self.y = B.y-A.y
        self.z = B.z-A.z
    
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


class vec2:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def from_point(self, A, B):
        self.x = B.x-A.x
        self.y = B.y-A.y
    
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
