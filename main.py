from complex import Complex
from vec import vec2

# a = Complex(1, 1)
# b = a.vec()
# print(b)

a = Complex(2, 2)
b=a.pow()
print(b)
c=b.sqrt()

for i in c:
    print(i)

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
