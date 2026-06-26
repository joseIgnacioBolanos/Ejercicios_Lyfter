class Node:
    def __init__(self, data, next=None):
        self.data = data
        self. next = None


class Stack():
    def __init__(self):
        self.head = None

    def push(self, new_node):
        new_node.next = self.head
        self.head = new_node

    def pop(self):
        removed = self.head
        self.head = self.head.next
        return removed
    
    def print_stack(self):
        current = self.head

        while current is not None:
            print(current.data)
            current =  current.next


stack = Stack()
stack.push(Node('A'))
stack.push(Node('B'))
stack.push(Node('C'))
stack.push(Node('D'))

#stack.pop()

stack.print_stack()

