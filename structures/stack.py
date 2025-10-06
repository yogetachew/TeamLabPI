class Node:
    def __init__(self, data):
        self.head = data 
        self.next = None

class UndoStack:
    def __init__(self):
        self.stack = []

    def push(self, cmd):
        # Add item to top of stack
        self.stack.append(cmd)
        
    def pop(self):
        # Remove and return top item
        if not self.is_empty():
            return self.stack.pop()
        else:
            return " Nothing were found"

    def peek(self):
        # Return top item without removing it
        if not self.is_empty():
            return self.stack[-1]
        else:
            return " Nothing were found "

    def is_empty(self):
        return len(self.stack) == 0