"""
Here we do import all the datastructures class from the structures folder
"""
from structures.queue import EventQueue
from structures.stack import UndoStack
from structures.linkedlist import Linkedlist

"""
This is the function to tests the queue it prints the testing message and then initializes the queue class and then checks if every of the methods works fine using the assert keyword.
The assert key word wouldn't return or do anything if the result was true but if the result was false it returns an Assertion Error and it fails the test 
"""
def testingQueue():
    print("Testing The Queue")
    q = EventQueue() # initializes the queue class and starts with an empty queue
    assert q.isEmpty() == True # checks if the queue is empty using the assert key word to see if the test passes or not (It is supposed to be empty)

    q.enqueue("Event A") # add Event A to the queue 
    assert q.isEmpty() == False # checks if the queue is empty using the assert key word to see if the test passes or not (It is not supposed to be empty)
    assert q.peek() == "Event A" #checks if the first value is Event A
    assert q.getLength() == 1 #checks if length of the queue is 1

    q.enqueue("Event B")# add Event B to the queue
    assert q.peek() == "Event A" #checks if the first value is still Event A which it still should be

    item = q.dequeue() #we now remove the first element
    assert item == "Event A" #we check if what we removed was Event A
    assert q.peek() == "Event B" # we now check if the new event at the top is Event B
    assert q.getLength() == 1 # we now check if the length of the queue now is 1

"""
This is the function to tests the queue it prints the testing message and then initializes the stack class and then checks if every of the methods works fine using the assert keyword.
The assert key word wouldn't return or do anything if the result was true but if the result was false it returns an Assertion Error and it fails the test 
"""
def testingStack():
    print("Testing The Stack")
    s = UndoStack()# initializes the stack class and starts with an empty stack
    assert s.is_empty() == True # checks if the stack is empty using the assert key word to see if the test passes or not (It is supposed to be empty)

    s.push("Undo Action A") # add Undo Action A to the stack
    assert s.is_empty() == False  # checks if the stack is empty using the assert key word to see if the test passes or not (It is not supposed to be empty)
    assert s.peek() == "Undo Action A" #checks if the first value is Undo Action A

    s.push("Undo Action B")# add Undo Action B to the queue
    assert s.peek() == "Undo Action B" #checks if the first value is Undo Action B which it still should be

    item = s.pop() #we now remove elements from the back
    assert item == "Undo Action B" #checks if the item removed was Undo Action B
    assert s.peek() == "Undo Action A"# checks if the value at the top of the stack is Undo Action A

"""
This is the function to tests the queue it prints the testing message and then initializes the LinkedList class and then checks if every of the methods works fine using the assert keyword.
The assert key word wouldn't return or do anything if the result was true but if the result was false it returns an Assertion Error and it fails the test 
"""
def testingLinkedList():
    print("Testing The Linked List")
    roster = Linkedlist() # initializes the Linkedlist class and starts with an empty linkedlist
    assert roster.len == 0# checks if the linkedlist is empty using the assert key word to see if the test passes or not (It is supposed to be empty)

    roster.append("Ana") #adding Ana to the back of the LinkedList
    assert roster.head.data == "Ana" # checks if the head points to Ana
    assert roster.tail.data == "Ana" #checks if the tail points to Ana
    assert roster.len == 1 #checks if the length of the Linkedlist is 1

    roster.append("Ben") #adding Ber to the back of the LinkedList and making it the tail
    assert roster.head.data == "Ana" # checks if the head points to Ana
    assert roster.tail.data == "Ben"#checks if the tail points to Ben
    assert roster.len == 2 #checks if the length of the Linkedlist is 2
    assert str(roster) == "Ana -> Ben" #printing and cheking if the roster prints this was

"""
We run all the test here and see if they passed if the Last print statements run
"""
def run_tests():
    print("Running tests for the data structures")
    testingQueue()
    testingStack()
    testingLinkedList()
    print("All tests passed!")

if __name__ == '__main__':
    run_tests()