# Create the node class to get the data /name for the linkedlist
class Node:
    def __init__(self, data):
        self.data = data 
        self.next = None

# Linkedlist class for the storage of the data in the list. 
# The first function is going to initialize both the head and tail boxes as well as the length variable for the list.
# The append function is to get each name assign to a box in the list,
# if the head of the list is empty, then the new data is given to both the head and the tail.
# else the the data is assign to the end of the list.
# the insert function, put the name with a index proper to it. In that case the index must not be nnegative or have a value greater than the length of our list
# If it does there is a error test for it
# then if the index is 0, that means it is our first data in the list, so the head get that value, if the length of the list is 0, then the list must carry both head and tail with same data
# if the index is anything else than 0 or the invalid ones, then the value is attribute to the box that follow the one with the index - 1, again if the tail has nothing in it, we gave it a new value
# The next function will be the remove function, it has an error control to verify if the index is incorrectly enter, or if the size of the list is 0, which means there is no data in the list,
# if the index is correct and the list is not empty, then the value that correspond to the index is removed while the data in the next boxes are pushed toward the head
# The find function browse the list looking for the name inserted, if find, it return the index
class Linkedlist:
    def __init__(self):

        self.head = None
        self.tail = None
        self.len = 0

    def append(self, name):
    
        new_node = Node(name)
        if not self.head:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

        self.len += 1

    def insert(self, index, name):
        if index < 0 or index > self.len:
            raise IndexError("Bounds' index is out of box")
        
        new_node = Node(name)
        if index == 0:
            self.head = new_node
            if self.len == 0:
                self.tail = new_node
        
        else:
            prev = self._get_node(index-1)
            new_node.next = prev.next 
            prev.next = new_node

            if new_node.next is None:
                self.tail = new_node
    
    def remove(self, index):
        if self.len == 0:
            raise IndexError("This list is empty, no need to remove anything.")
        if index < 0 or index >= self.len:
            raise IndexError("Bounds' index is out of box")

        if index == 0:
            removed = self.head
            self.head = self.head.next
            if self.len == 1:
                self.tail = None
        else:
            prev = self._get_node(index - 1)
            removed = prev.next
            prev.next = removed.next
            if removed == self.tail:
                self.tail = prev

        self.len -= 1
        return removed.data

    def find(self, name):
        current = self.head
        index = 0
        while current:
            if current.data == name:
                return index
            current = current.next
            index += 1
        return -1

    def _get_node(self, index):
        current = self.head
        for _ in range(index):
            current = current.next
        return current

    def __iter__(self):
        current = self.head
        while current:
            yield current.data
            current = current.next

    def __str__(self):
        return " -> ".join(str(name) for name in self)
