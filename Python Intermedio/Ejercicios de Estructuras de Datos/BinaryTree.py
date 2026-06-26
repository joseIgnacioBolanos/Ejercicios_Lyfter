class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self, root):
        self.root= root

    def print_structure(self):
        self.print_tree(self.root)


    def print_tree(self, current_node):
        if current_node is None:
            return

        print(current_node.data)

        self.print_tree(current_node.left)
        self.print_tree(current_node.right)

root = Node("A")

tree = BinaryTree(root)
root.left = Node("B")
root.right = Node("C")
root.left.left = Node("D")
root.left.right = Node("E")
root.left.left.left = Node("Z")


tree.print_structure()


        