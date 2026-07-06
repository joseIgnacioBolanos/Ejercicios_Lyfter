class Node:
    def __init__(self, data, next = None):
        self.data = data
        self.next = next



class Queue():
    def __init__(self, head):
        self.head=  head
   
    def enqueue(self, new_node):

        current_node = self.head

        while current_node.next is not None:
            current_node= current_node.next

        current_node.next = new_node

    def dequeue(self):
        if self.head:
            self.head= self.head.next

    def print_structure(self):

        current_node = self.head
        while current_node is not None:
            print(current_node.data)
            current_node = current_node.next
            
node1= Node('A')
q = Queue(node1)

node2 = Node('B')
q.enqueue(node2)

node3 = Node('C')
q.enqueue(node3)

q.print_structure()
