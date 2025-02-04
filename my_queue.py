# A Queue works on the principle of “First-in, first-out”. A queue has two simple operations:
# enqueue - It adds an element to the end of the queue.
# dequeue - It removes the element from the beginning of the queue.


# class MyQueue(object):
#     def __init__(self, size):
#         """
#         Initializes the queue with a fixed size.

#         Parameters:
#         size (int): Maximum size of the queue.
#         """
#         self.__maxSize = size           # Size of the circular array
#         self.__que = [None] * size      # Queue stored as a list
#         self.__rear = -1                # Index of the last element
#         self.__front = 0                # Index of the first element
#         self.__nItems = 0               # Current number of items in the queue

#     def getQueue(self):
#         """
#      Returns the current state of the queue as a list.
#         """
#      return self.__que

#     def enqueue(self, item):
#         """
#         Adds an element to the rear of the queue.

#         Parameters:
#         item: The element to add.

#      Returns:
#         int: Index of the rear element or -1 if the queue is full.
#         """
#         if self.__nItems < self.__maxSize:  # Check if queue is not full
#             ## ADD YOUR CODE HERE
#      return -1  # Queue is full

    
#     def dequeue(self):
#         """
#         Removes an element from the front of the queue.

#       Returns:
#         The removed element or -1 if the queue is empty.
#         """
#         if self.__nItems > 0:  # Check if queue is not empty
#             ## ADD YOUR CODE HERE
#       return -1  # Queue is empty

class MyQueue(object):
    def __init__(self, size):
        self.__maxSize = size
        self.__que = [None] * size
        self.__rear = -1
        self.__front = 0
        self.__nItems = 0

    def getQueue(self):
        return self.__que

    def enqueue(self, item):
        if self.__nItems < self.__maxSize:
            self.__rear = (self.__rear + 1) % self.__maxSize
            self.__que[self.__rear] = item
            self.__nItems += 1
            return self.__rear
        return -1  # Queue is full

    def dequeue(self):
        if self.__nItems > 0:
            item = self.__que[self.__front]
            self.__que[self.__front] = None  # Optional: Clear the slot
            self.__front = (self.__front + 1) % self.__maxSize
            self.__nItems -= 1
            return item
        return -1  # Queue is empty
