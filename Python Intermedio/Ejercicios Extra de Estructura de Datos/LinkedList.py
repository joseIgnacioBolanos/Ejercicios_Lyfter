class Node:
    def __init__(self, data, next = None, prev = None):
        self.data = data
        self.next = next
        self.prev = prev

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def insert_front(self, data):
        new_node= Node(data)
        if self.head is None:
            self.head = self.tail = new_node
            return

        new_node.next  =  self.head
        self.head.prev = new_node
        self.head = new_node

    def insert_back(self, data):
        new_node = Node(data)
        if self.tail is None:
            self.tail = self.head = new_node
            return
        
        self.tail.next = new_node
        new_node.prev = self.tail
        self.tail  = new_node

    def delete(self, data):
       current_node = self.head


       while current_node is not None:
           if current_node.data == data:
               if self.head == self.tail:
                   self.head = self.tail = None
                   break
               if self.head.data == data:
                   self.head=self.head.next
                   self.head.prev = None
                   break
               if self.tail.data == data:
                   self.tail = self.tail.prev
                   self.tail.next =None
                   break
               else:
                   current_node.prev.next = current_node.next
                   current_node.next.prev = current_node.prev
                   break
           current_node = current_node.next
           if current_node is None:
               return

    

    def print_all(self):
        current_node = self.head
        while current_node is not None:
            print(current_node.data)
            current_node = current_node.next



ll = LinkedList()

ll.insert_front(10)
ll.insert_front(20)
ll.insert_back(30)
ll.print_all()

ll.delete(30)
ll.print_all()