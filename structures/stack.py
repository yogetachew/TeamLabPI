class Node:
    def __init__(self, data):
        self.head = data 
        self.next = None
# store commands that can be undone later.
# Last In First Out rule, last action done will be the first one to be undone.
class UndoStack:
    # initiate and create empty list that will hold the commands
    def __init__(self):
        self.stack = []
    # to add new command to the top of the stack.
    def push(self, cmd):
        self.stack.append(cmd)
        
    def pop(self):
        # Before removing, it checks that the stack is not empty and remove
        # undo the last action done in the system
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