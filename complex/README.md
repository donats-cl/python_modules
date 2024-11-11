# Complex number
## Complex()

    a = Complex(3, 2)
    # 3 + 2i

    a.real # 3
    a.imag # 2

    b = ~a
    # 3 - 2i

    a + b
    # 6

    a-b
    # 0 + 4i

## method *vec*

    a = Complex(2, 2)
    # 3 + 2i

    v = a.vec()
    # (2*sqrt(2), 45) (len, angle)

## method *raw*

    a = Complex(sqrt(2), sqrt(2))
    # sqrt(2) + sqrt(2)i it's what print show

    a.raw()
    # return (1.41.., 1.41..)
