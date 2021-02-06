class Node():

    def __init__(self, data):
        self.data = data
        self.next = None
    
class LinkedList():

    def __init__(self):
        self.head = None
        self.tail = None
  
    def append(self, data):
        new_node = Node(data)
        
        if self.head == None:
            self.head = new_node
            self.tail = self.head
            self.length = 1
        else:
            self.tail.next = new_node
            self.tail = new_node 
            self.length += 1
    
    def prepend(self, data):
        new_node = Node(data)

        if self.head == None:
            self.head = new_node
            self.tail = self.head
            self.length = 1
        else:
            new_node.next = self.head
            self.head = new_node
            self.length += 1
    
    def printList(self):
        linked_list = []
        currentNode = self.head

        while currentNode != None:
            linked_list.append(currentNode.data)
            currentNode = currentNode.next 
        
        print(linked_list)
        print(f"Length of linked list: {self.length}")
        return linked_list

    def insert(self, index, data):
        new_node = Node(data)

        if index >= self.length:
            return self.append(data)
        
        if index == 0:
            return self.prepend(data)
        
        temp_node = self.traverse_index(index-1)
        new_pointer = temp_node.next
        temp_node.next = new_node
        new_node.next = new_pointer
        self.length += 1
        
    def traverse_index(self, index):
        count = 0
        currentNode = self.head

        while count != index:
            currentNode = currentNode.next
            count += 1
        
        return currentNode
    
    def remove(self, index):
        if index >= self.length:
            print("Wrong index")
        
        if index == 0:
            self.head = self.head.next
            self.length -= 1
            return
        
        temp_node = self.traverse_index(index-1)
        deleted_node = temp_node.next
        temp_node.next = deleted_node.next
        self.length -= 1
    
    def reverse(self):
        if self.length == 1:
            return self.head
      
        first = self.head 
        self.tail = self.head 
        second = first.next

        while second != None:
            temp = second.next 
            second.next = first 
            first = second 
            second = temp 
        
        self.head.next = None
        self.head = first
    

# Testing
l = LinkedList()

print("Appending...")
l.append(10)
l.append(15)
l.append(20)
l.printList()
# print(l.head.data)
# print(l.tail.data)

print("Prepending...")
l.prepend(5)
l.prepend(1)
l.printList()
# print(l.head.data)
# print(l.tail.data)

print("Inserting...")
l.insert(10, 30)
l.insert(2, 8)
l.printList()

# print("Printing List...")
# l.printList()

print("Removing...")
l.remove(3)
l.printList()
l.remove(0)
l.printList()

print("Reversing...")
l.reverse()
l.printList()