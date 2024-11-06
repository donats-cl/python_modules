import math as mt

class Tree:
    def __init__(self, key, value=[], left=None, right=None):
        self.key = key
        self.left = left
        self.right = right
        self.value = value
        self.height = 0
    
    def __str__(self):
        return f"{self.value} ({self.key})"

def min(node):
    if node == None: return None
    if node.left == None: return node
    return min(node.left)

def max(node):
    if node == None: return None
    if node.right == None: return node
    return max(node.right)

def find(node, key):
    if node == None: return None
    if node.key == key: return node
    return find(node.left, key) if key < node.key else find(node.right, key)

def add(node, key, value):
    if key < node.key:
        if node.left is None:
            node.left = Tree(key, value)
        else:
            add(node.left, key, value)
    elif key > node.key:
        if node.right is None:
            node.right = Tree(key, value)
        else:
            add(node.right, key, value)

def delete(node, key):
    if node == None: return None
    if key < node.key:
        node.left = delete(node.left, key)
    elif key > node.key:
        node.right = delete(node.right, key)
    else:
        if node.left is None:
            return node.right
        elif node.right is None:
            return node.left
        temp = min(node.right)
        node.key = temp.key
        node.value = temp.value
        node.right = delete(node.right, temp.key)
    return node

def update_height(node, key):
    left_h = node.left.height if not node.left == None else -1
    right_h = node.right.height if not node.right == None else -1
    node.height = 1 + mt.max(left_h, right_h)

def sort():
    pass


if __name__ == '__main__':
    tree = Tree(5, [''])

    add(tree, 3, ['left'])
    add(tree, 7, ['right'])
    add(tree, 2, ['left-left'])
    add(tree, 6, ['left-right'])

    print(min(tree))

    # print(f"{tree.value} have a child left {tree.child_left.value} and a child right {tree.child_right.value}")
    