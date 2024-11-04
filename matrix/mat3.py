from vec import *


class mat3:
    def __init__(self, v):
        self.mat = vec3(vec3(v[0][0], v[0][1], v[0][2]),
                        vec3(v[1][0], v[1][1], v[1][2]),
                        vec3(v[2][0], v[2][1], v[2][2]))
        
    def __str__(self):
        return f"[{self.mat.x}\n{self.mat.y}\n{self.mat.z}]"

    def extend(self, v):
        self.x = v[0]
        self.y = v[1]
        self.z = v[2]

        self.mat = vec3(
            vec4(self.mat.x.x, self.mat.x.y, self.mat.x.z, self.x),
            vec4(self.mat.y.x, self.mat.y.y, self.mat.y.z, self.y),
            vec4(self.mat.z.x, self.mat.z.y, self.mat.z.z, self.z)
        )
    
    def gauss(self):
        x = self.mat.x
        y = self.mat.y
        z = self.mat.z

        y = x*y.x - y*x.x
        z = x*z.x - z*x.x
        
        z = y*z.y - z*y.y

        res = mat3([
            [x.x, x.y, x.z],
            [y.x, y.y, y.z],
            [z.x, z.y, z.z]
            ])
        res.extend([x.w, y.w, z.w])

        return res

    # determinant
    def len(self):
        x = self.mat.x
        y = self.mat.y
        z = self.mat.z
        return (x.x*y.y*z.z) + (y.x*z.y*x.z) + (x.y*y.z*z.x) - (z.x*y.y*x.z) - (z.y*y.z*x.x) - (y.x*x.y*z.z)
