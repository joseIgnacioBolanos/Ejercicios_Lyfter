class Node:
    def __init__(self, data, next = None):
        self.data = data
        self.next = next



class Queue():
    def __init__(self):
        self.head=  None
   
    def enqueue(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node        
            return

        current_node = self.head

        while current_node.next is not None:
            current_node= current_node.next

        current_node.next = new_node

    def dequeue(self):
        if self.head is None:
            return None

      
        removed = self.head
        self.head= self.head.next
        
        return removed.data
        


    def print_all(self):

        current_node = self.head
        while current_node:
            if  current_node.next is  None:
                print(current_node.data)
            else:
                print(current_node.data, end= " - > ")
            current_node = current_node.next
            
q = Queue()

q.enqueue('A')
q.enqueue('B')

q.enqueue('C')

q.print_all()

print(q.dequeue())

q.print_all()
