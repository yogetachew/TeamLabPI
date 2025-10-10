
# Import all the classes you need to test
from structures.queue import EventQueue
from structures.stack import UndoStack
from structures.linkedlist import Linkedlist

def run_tests():
    print("Running tests for the data structures")
    testingQueue()
    testingStack()
    testingLinkedList()
    print("All tests passed!")

def testingQueue():
    print("Testing Queue...")
    q = EventQueue()
    assert q.isEmpty() == True

    q.enqueue("Event A")
    assert q.isEmpty() == False
    assert q.peek() == "Event A"
    assert q.getLength() == 1 # This should be __len__ but matches your code

    q.enqueue("Event B")
    assert q.peek() == "Event A" # First item should still be A

    item = q.dequeue()
    assert item == "Event A"
    assert q.peek() == "Event B"
    assert q.getLength() == 1

# --- STACK TESTS ---
def testingStack():
    print("Testing Stack...")
    s = UndoStack()
    assert s.is_empty() == True

    s.push("Undo Action A")
    assert s.is_empty() == False
    assert s.peek() == "Undo Action A"

    s.push("Undo Action B")
    assert s.peek() == "Undo Action B" # Should now be B on top

    item = s.pop()
    assert item == "Undo Action B" # LIFO - B comes out first
    assert s.peek() == "Undo Action A"

# --- LINKED LIST TESTS ---
def testingLinkedList():
    print("Testing Linked List...")
    roster = Linkedlist()
    assert roster.len == 0

    roster.append("Ana") # Test append on empty list
    assert roster.head.head == "Ana" # Using .head because of your Node's naming
    assert roster.tail.head == "Ana"
    assert roster.len == 1

    roster.append("Ben") # Test append on non-empty list
    assert roster.head.head == "Ana"
    assert roster.tail.head == "Ben"
    assert roster.len == 2
    # This assertion would have caught your insert-at-head bug
    # It checks if the list links correctly
    assert str(roster) == "Ana -> Ben"

# To run the tests, add this to the bottom of the file
if __name__ == '__main__':
    run_tests()