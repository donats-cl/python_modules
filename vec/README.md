# Vec module
## vec2 and vec3: 
    # Initialize vector a and b
    a = vec2(1, 2)
    b = vec2(2, 5)

    # sum 
    c = a + b
    # vector (1+2, 2+5) = vector (3, 7);
    # c = vec2(3, 6)

    # mul vector and number
    v = 10
    c = a * v
    # vector (1*10, 2*10) = vector (10, 20);
    # c = vec2(10, 20)
    
# Length vec2 and vec3
    # Initialize vector a and b
    a = vec2(1, 1)
    b = vec2(2, 3)

    # print lenght vector a and b
    print(a.len()) # sqrt(2)
    print(b.len()) # sqrt(13)

# Get Vector from points
    # Initialize points A and B like vec3
    A = vec3(2, 5, 3)
    B = vec3(0, 1, 8)

    # get vector from points A and B
    AB = vec3.from_point(A, B)
    # vector (-2, -4, 5)
