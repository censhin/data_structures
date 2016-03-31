class Node():

    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

class BST():

    def __init__(self, root=None):
        self.root = root
        self.count = 0

    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
            self.count += 1
            return
        else:
            current = self.root
            while True:
                parent = current
                if value == current.value:
                    return
                elif value < current.value:
                    current = current.left
                    if current is None:
                        parent.left = Node(value)
                        self.count += 1
                        return
                elif value > current.value:
                    current = current.right
                    if current is None:
                        parent.right = Node(value)
                        self.count += 1
                        return

    def pre_order_traverse(self, current):
        if current:
            print current.value
            self.pre_order_traverse(current.left)
            self.pre_order_traverse(current.right)

    def in_order_traverse(self, current):
        if current:
            self.pre_order_traverse(current.left)
            print current.value
            self.pre_order_traverse(current.right)

    def post_order_traverse(self, current):
        if current:
            self.pre_order_traverse(current.left)
            self.pre_order_traverse(current.right)
            print current.value

if __name__ == '__main__':
    bst = BST()
    bst.insert(10)
    bst.insert(12)
    bst.insert(2)
    print "count {}".format(bst.count)
    print "value {}".format(bst.root.value)
    print "right {}".format(bst.root.right)
    print "left {}".format(bst.root.left)
    bst.insert(32)
    print "count {}".format(bst.count)
    print "Traversing Pre Order..."
    bst.pre_order_traverse(bst.root)
    print "Traversing In Order..."
    bst.in_order_traverse(bst.root)
    print "Traversing Post Order..."
    bst.post_order_traverse(bst.root)
