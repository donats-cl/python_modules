
class Tree:
    def __init__(self, key, value=[], child_left=None, child_right=None):
        self.key = key
        self.child_left = child_left
        self.child_right = child_right
        self.value = value

    def insert(self, key, value):
        if key < self.key:
            if self.child_left is None:
                self.child_left = Tree(key, value)
            else:
                self.child_left.insert(key, value)
        elif key > self.key:
            if self.child_right is None:
                self.child_right = Tree(key, value)
            else:
                self.child_right.insert(key, value)
    
    def sort():
        pass


if __name__ == '__main__':
    tree = Tree(5, [''])

    tree.insert(3, ['left'])
    tree.insert(7, ['right'])

    print(f"{tree.value} have a child left {tree.child_left.value} and a child right {tree.child_right.value}")
    