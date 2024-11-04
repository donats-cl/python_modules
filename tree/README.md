# Binary Tree

## Tree()

    tree = new Tree(5, "start")
    tree.insert(3, "LOW")
    tree.insert(7, "HIGH"")

    print(tree.child_left.value)
    # it's a child which key lower than root key // printed LOW

    print(tree.child_right.value)
    # it's a child which key lower than root key // printed HIGH

    tree.insert(8, "it's child right child's")
    # it's a child right child's, because tree have all children

### Tree have *left* and *right* children

    left = tree.child_left
    right = tree.child_right

    print(tree.value)
    # printed value root the tree // "start"

    print(left.value)
    # printed value left child the tree // "LOW"

    print(right.value)
    # printed value right child the tree // "HIGH"

    print(tree.child_right.child_right.value)
    print(right.child_right.value) 
    # IT'S SAME OPERATION. They printed "it's child right child's"
