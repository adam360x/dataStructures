class RedBlackTree:
    class Node:
        def __init__(self, val, arg2):
            self.val = val
            self.left = None
            self.right = None
            self.col = 'R'
            self.parent = None
            self.arg2 = arg2
    
    def __init__(self):
        self.root = None

    def leftRotate(self, node):
        y = node.right
        node.right = y.left

        if y.left is not None:
            y.left.parent = node

        y.parent = node.parent

        if node.parent is None:
            self.root = y
        elif node == node.parent.left:
            node.parent.left = y
        else:
            node.parent.right = y

        y.left = node
        node.parent = y

    def rightRotate(self, node):
        y = node.left
        node.left = y.right

        if y.right is not None:
            y.right.parent = node

        y.parent = node.parent

        if node.parent is None:
            self.root = y
        elif node == node.parent.right:
            node.parent.right = y
        else:
            node.parent.left = y

        y.right = node
        node.parent = y

    def fix(self, node):

        while node != self.root and node.parent is not None and node.parent.col == 'R':

            if node.parent.parent is None:
                break

            if node.parent == node.parent.parent.left:
                y = node.parent.parent.right
                if y is not None and y.col == 'R':
                    node.parent.col == 'B'
                    y.color = 'B'
                    node.parent.parent.col == 'R'
                    node = node.parent.parent
                else:
                    if node == node.parent.right:
                        node = node.parent
                        self.leftRotate(node)
                    node.parent.color = 'B'
                    node.parent.parent.col = 'R'
                    self.rightRotate(node.parent.parent)
            else:
                y = node.parent.parent.left
                if y is not None and y.col == 'R':
                    node.parent.col = 'B'
                    y.color = 'B'
                    node.parent.parent.col = 'R'
                    node = node.parent.parent
                else:
                    if node == node.parent.left:
                        node = node.parent
                        self.rightRotate(node)
                    node.parent.color = 'B'
                    node.parent.parent.col = 'R'
                    self.leftRotate(node.parent.parent)
            if node == self.root:
                break
        self.root.col = 'B'


    # Additional arg2 for flexibility
    def insert(self, val, arg2 = None):

        z = self.Node(val, arg2)
        y = None
        x = self.root
        while x != None:
            y = x
            if val < x.val:
                x = x.left
            else:
                x = x.right
        
        z.parent = y

        if y == None:
            self.root = z
        elif z.val < y.val:
            y.left = z
        else:
            y.right = z

        if z.parent is not None:
            self.fix(z)
