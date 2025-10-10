#we are importing all the modules and files we need for this project
import json
from structures import queue
from structures import stack
from structures import linkedlist

class AirportSimulator:
    """
    In this contructor we initialize all the data structues from the files we need like the queue, the stack and the linkedlist
    """
    def __init__(self, eventsFilepath):
        self.eventQueue = queue.EventQueue()
        self.undoStack = stack.UndoStack()
        self.roster = linkedlist.Linkedlist()
        self.eventsFilepath = eventsFilepath
    """
    This method below Loads all the events we need from the json file and then adds it to the queue,
    It prints a successful message wit the length of the events been added to the queue.
    if the file was not found, it prints the error message saying the file was not found.
    if there was an error reading the json file but the json file was found it prints an error message for that. 

    """
    def loadEvents(self):
        try:
            with open(self.eventsFilepath, 'r') as f:
                events = json.load(f)
                for event in events:
                    self.eventQueue.enqueue(event)
            print(type(self.eventQueue))
            print(f"Successfully loaded {self.eventQueue.getLength()} events.")
        except FileNotFoundError:
            print(f"File name: {self.eventsFilepath} was not found.")
      
        except json.JSONDecodeError:
            print(f"There was an error reading the json file at {self.eventsFilepath}.")
            
    """
    This function runs the simulation, it checks if the queue is empty and if it's not empty it runs the processes in the next function and prints the roster everytime each processes run
    the processes ran depends on the type of process given to it in the json file and after that each event is been removed from the queue.
    """
    def runSimulation(self):
    
        while not self.eventQueue.isEmpty():
            event = self.eventQueue.dequeue()
            self.processEvent(event)
        print(f"Final Roster: {self.roster}")
    
    """
    This function is where the events is been processed based on the type been passed in each json entity.
    1. If the event type is 'arrive' it gets the persons name and then appends the name to the Linkedlist roster and also does the same to the stack in case of an undo
    2. If the event type is 'insert' it also gets the persons name and the index at which we would like to insert the the name at in the Linkedlist It also adds it to stack too and we also want to take into consideration any error adding the value to the specific index.
    3. If the event type is 'remove' it gets the index too and goes through the linkedlist finding the name at the index in the linkedlist and then removes the person from the 
    """
    def processEvent(self, event):
       
        event_type = event.get('type')
        print(f"Processing Event: {event}")

        if event_type == 'arrive':
            name = event.get('name')
            if name:
                self.roster.append(name)
                self.undoStack.push({'type': 'undo_arrive', 'name': name})
        
        elif event_type == 'insert':
            name = event.get('name')
            index = event.get('index')
            if name is not None and index is not None:
                try:
                    self.roster.insert(index, name)
                    self.undoStack.push({'type': 'undo_insert', 'index': index})
                except IndexError as e:
                    print(f"The error is {e}")

        elif event_type == 'remove':
            index = event.get('index')
            if index is not None:
                try:
                    removed_name = self.roster.remove(index)
                    self.undoStack.push({'type': 'undo_remove', 'name': removed_name, 'index': index})
                except IndexError as e:
                    print(f"The error is {e}")
        
        else:
            print(f"Unknown event type '{event_type}'")
        
        print(f"Current Roster: {self.roster}\n")


if __name__ == '__main__':
    events_file = 'sample_events.json'
    simulator = AirportSimulator(events_file)
    simulator.loadEvents()
    simulator.runSimulation()

