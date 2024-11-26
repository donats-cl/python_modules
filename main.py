from complex import Complex
from vec import vec2, vec3, vec4
from matrix import mat3
from maths import rtd
from math import pi

e = Complex(1, rtd(2*pi/3), trig=True)
o = Complex(0)
a = Complex(1)

mat = mat3([
    [o,o,e.pow()],
    [a,o,e.pow()],
    [e.pow(), e, a]])

print(mat.raw(), mat.len)

# a = vec3(1,0,0)
# m = mat3(a.xyy, a.yxy, a.yyx)

# print(m.x.x)

# v = (Complex(1,2).pow()-Complex(2,-1).pow(3))/(Complex(1,-1).pow(3)+Complex(2,1).pow())

# print(v)

# a = Complex(1, 1)
# b = a.vec()
# print(b)

# a = Complex(2, 2)
# b=a.pow()
# print(b)
# c=b.sqrt()

# for i in c:
#     print(i)

# b = a.pow(2)

# print(b.x, b.y)

# print(~a)

# v = vec2(1, 1)

# print(v.norm())

# a = Complex(2*cos(dtr(105)), 2*sin(dtr(105)))
# b = Complex(cos(dtr(150)), sin(dtr(150)))

# print(f"Res: {a},\nRaw: {a.raw()}\n")
# print(f"Res: {b},\nRaw: {b.raw()}\n")
# c = a/b
# print(f"Res: {c},\nRaw: {c.raw()}\n")
