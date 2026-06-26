class Node:
    def __init__(self, data, next = None, previous=None):
        self.data  = data
        self.next = None
        self.previous = None

class Dequeue:
    def __init__(self):
        self.head = None
        self.tail = None

    def push_left(self, new_node):
        if self.head is None:
            self.head = self.tail= new_node
            return
        
        new_node.next = self.head
        self.head = new_node
        self.previous= new_node
    def push_right(self, new_node):
        if self.tail is None:
            self.tail = self.head = new_node
            return
         
        self.tail.next = new_node
        new_node.previous = self.tail
        self.tail = new_node

    def pop_left(self):
        if self.head is None:
            return None
        
        removed = self.head
        self.head = self.head.next

        if self.head is not None:
            self.head.previous = None
        else:
            self.tail =None

        return removed
    
    def pop_right(self):
        if self.tail is None:
            return None
        
        removed = self.tail
        self.tail = self.tail.previous 

        if self.tail is not None:
            self.tail.next = None
        else:
            self.head = None

        return removed
    
    def print_deque(self):
        current = self.head

        while current is not None:
            print(current.data)
            current= current.next

            




dequeue = Dequeue()
dequeue.push_left(Node('A'))
dequeue.push_left(Node('V'))
dequeue.push_right(Node('Y'))
dequeue.push_left(Node('S'))
dequeue.pop_left()

dequeue.print_deque()