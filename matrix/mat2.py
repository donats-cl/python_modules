from vec import *

class mat2:
    @singledispatchmethod
    def __init__(self, v):
        self.mat = vec2(vec2(v[0][0], v[0][1]),
                        vec2(v[1][0], v[1][1]))
    
    @__init__.register
    def _(self, x: vec2, y: vec2):
        self.mat = vec2(x, y)
    
    def __str__(self):
        return f"[{self.mat.x}\n{self.mat.y}]"
    
    def raw(self):
        return f"[{self.mat.x.raw()}\n{self.mat.y.raw()}]"

    def extend(self, v):
        self.x = v.x
        self.y = v.y

        self.mat = vec2(
            vec3(self.mat.x, self.x),
            vec3(self.mat.y, self.y)
        )

    @property
    def x(self):
        return self.mat.x
    
    @property
    def y(self):
        return self.mat.y

    # determinant
    @property
    def len(self):
        x = self.mat.x
        y = self.mat.y
        return x.x*y.y - (x.y*y.x)
