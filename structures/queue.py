class EventQueue:
    # store events in FIFO structure
    # we gonna initiate the queue and the enqueue function adds a new event at the end
    # to ensure that events are handled in the same order they arrive.
    def __init__(self):
        self.eventList = [] 
    def enqueue(self, event):
        try:
            self.eventList.append(event)
        except Exception as ex:
            print("Error while adding event:", ex)

    # dequeue function removes the first event from our list, this means the oldest event is removed first.
    def dequeue(self):
        try:
            if not self.isEmpty():
                return self.eventList.pop(0)
            else:
                print("Queue is empty, cannot remove any event.")
                return None
        except Exception as ex:
            print("Error while removing event:", ex)
            return None

    # we will use peek function to look at the first element without removing it.
    def peek(self):
        if not self.isEmpty():
            return self.eventList[0]
        else:
            return None
    # The isEmpty function simply returns True if our queue is empty to helps avoid popping or
    # peeking into an empty list, which can cause errors.
    def isEmpty(self):
        return len(self.eventList) == 0

    # The getLength function returns the number of events to help track how many operations are pending at the airport system.
    def getLength(self):
        return len(self.eventList)
