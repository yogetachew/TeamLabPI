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
    This method below Loads all the events we need from the json file and then adds it tot he queue, 

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
            

    def runSimulation(self):
    
        while not self.eventQueue.isEmpty():
            event = self.eventQueue.dequeue()
            self.processEvent(event)
        print(f"Final Roster: {self.roster}")

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

