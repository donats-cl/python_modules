# Matrix
## mat2 and mat3

    mat = mat3([
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ])

    print(mat.len()) 
    # mat.len() it's determinant = 0

    mat.extend([1, 2, 3])

    print(mat)
    # [1, 2, 3, 1]
    # [4, 5, 6, 2]
    # [7, 8, 9, 3]

    print(mat.gauss())
    # [1, 2, 3, 1]
    # [0, 3, 6, 2]
    # [0, 0, 0, 0]
