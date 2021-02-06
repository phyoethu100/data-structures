class Node():
    def __init__(self, data):
        self.data = data
        self.next = None 

class Stack():
    def __init__(self):
        self.top = None
        self.bottom = None
        self.length = 0
    
    def peek(self):
        if self.top is None:
            return None
        return self.top.data
    
    def push(self, data):
        new_node = Node(data)

        if self.top == None:
            self.top = new_node
            self.bottom = new_node
        else:
            temp_pointer = self.top
            self.top = new_node 
            self.top.next = temp_pointer

        self.length += 1
    
    def pop(self):
        if self.top == None:
            return None
        else:
            temp_pointer = self.top
            self.top = self.top.next
            self.length -= 1
            if (self.top == self.bottom) or (self.length == 0):
                return None
        

# Testing
s = Stack()
s.push(3)
s.push(5)
s.push(7)
print("After pushing...")
print(s.peek())
s.pop()
s.pop()
print("After popping...")
print(s.peek())
