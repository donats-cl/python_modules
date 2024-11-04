from vec import *


class mat2:
    def __init__(self, v):
        self.mat = vec2(vec2(v[0][0], v[0][1]),
                        vec2(v[1][0], v[1][1]))
    
    def __str__(self):
        return f"[{self.mat.x}\n{self.mat.y}]"

    def extend(self, v):
        self.x = v.x
        self.y = v.y

        self.mat = vec2(
            vec3(self.mat.x, self.x),
            vec3(self.mat.y, self.y)
        )

    # determinant
    def len(self):
        x = self.mat.x
        y = self.mat.y
        return x.x*y.y - (x.y*y.x)
