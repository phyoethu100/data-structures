class Node():

    def __init__(self, data):
        self.data = data
        self.next = None


class Queue():

    def __init__(self):
        self.first = None
        self.last = None
        self.length = 0
    
    def peek(self):
        if self.first == None:
            return None
        return self.first.data

    def enqueue(self, data):
        new_node = Node(data)

        if self.length == 0:
            self.first = new_node
            self.last = new_node 
        else:
            self.last.next = new_node
            self.last = new_node

        self.length += 1

    def dequeue(self):
        if self.first == None:
            return None
        if self.first == self.last:
            self.last = None
        
        self.first = self.first.next
        self.length -= 1


# Testing
q = Queue() 
print("Enqueue...")
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
print(q.peek())
print("Dequeue...")
q.dequeue()
q.dequeue()
print(q.peek())