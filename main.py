from complex import *
from maths import *

a = Complex(2*cos(dtr(105)), 2*sin(dtr(105)))
b = Complex(cos(dtr(150)), sin(dtr(150)))

print(f"Res: {a},\nRaw: {a.raw()}\n")
print(f"Res: {b},\nRaw: {b.raw()}\n")
c = a/b
print(f"Res: {c},\nRaw: {c.raw()}\n")
