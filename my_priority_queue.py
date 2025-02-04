# PRIORITY QUEUES
# Like an ordinary queue, a priority queue has a front and a rear, and items are removed from the front. 
# In a priority queue, however, each element has a priority value associated with it. 
# When you add an element to the queue, it is inserted in a position based on its priority value. Items are ordered by a priority value so that the item with the highest 
# priority (which in many implementations is the lowest value of a key) is always at the front. 
# When multiple items have the same priority, they follow the queue ordering, FIFO, so that the oldest inserted item comes first. 
# As with both stacks and queues, no access is provided to arbitrary items in the middle of a priority queue.

# class MyItem:
#     def __init__(self, priority, value):
#         """Initialize an item with a value and priority."""
#         self.value = value
#         self.priority = priority

#     def __str__(self):                  # String representation of the array
#         return "(" + str(self.value) + ", " + str(self.priority) + ")"

#     def getPriority(self):
#         """Return the item's priority."""
#         return self.priority

#     def getValue(self):
#         """Return the item's value."""
#         return self.value
    

# class MyPriorityQueue:
#     def __init__(self, size):
#         """Initialize a priority queue with a given size."""
#         self.__maxSize = size           # Maximum size of the queue
#         self.__que = [None] * size      # Internal list representing the queue
#         self.__nItems = 0              # Number of items in the queue (empty initially)

#     def __str__(self):                  # String representation of the array
#         return "[" + ", ".join(
#             str(self.__que[i]) for i in range(self.__nItems)
#         ) + "]"
   
#     def __len__(self):
#       return self.__nItems
    
#     def getQueue(self):
#         """Return the internal representation of the queue."""
#         return self.__que

#     def peek(self):                    # Return frontmost item
#       return None if self.isEmpty() else self.__que[self.__nItems-1]

#     def isEmpty(self):
#         return self.__nItems == 0

#     def isFull(self):
#         return self.__nItems == self.__maxSize

#     def enqueue(self, item):
#         """Insert an item into the queue based on its priority.
#         High priority == high value
#         Return -1 is queue is full, zero otherwise"""
#         ## ADD YOUR CODE HERE
#         return 0
                             

#     def dequeue(self):
#         """Remove and return the item at the front of the queue.
#         Return -1 if queue is empty, and the item otherwise"""
#         ## ADD YOUR CODE HERE
#         return -1
 
class MyItem:
    def __init__(self, priority, value):
        """Initialize an item with a value and priority."""
        self.value = value
        self.priority = priority

    def __str__(self):
        return "(" + str(self.value) + ", " + str(self.priority) + ")"

    def getPriority(self):
        return self.priority

    def getValue(self):
        return self.value


class MyPriorityQueue:
    def __init__(self, size):
        """Initialize a priority queue with a given size."""
        self.__maxSize = size
        self.__que = [None] * size
        self.__nItems = 0

    def __str__(self):
        return "[" + ", ".join(
            str(self.__que[i]) for i in range(self.__nItems)
        ) + "]"

    def __len__(self):
        return self.__nItems

    def getQueue(self):
        return self.__que

    def peek(self):
        return None if self.isEmpty() else self.__que[self.__nItems - 1]

    def isEmpty(self):
        return self.__nItems == 0

    def isFull(self):
        return self.__nItems == self.__maxSize

    def enqueue(self, item):
        """Insert an item into the queue based on its priority.
        High priority == low value (min priority queue).
        Returns -1 if queue is full, 0 otherwise."""
        if self.isFull():
            return -1  # Queue is full

        i = self.__nItems - 1
        while i >= 0 and self.__que[i].getPriority() > item.getPriority():
            self.__que[i + 1] = self.__que[i]  # Shift right
            i -= 1

        self.__que[i + 1] = item  # Insert item at correct position
        self.__nItems += 1
        return 0

    def dequeue(self):
        """Remove and return the item at the front of the queue.
        Returns -1 if the queue is empty."""
        if self.isEmpty():
            return -1

        self.__nItems -= 1
        return self.__que[self.__nItems]  # Return highest priority item