# STACKS
# A stack data structure allows access to only one data item in the collection: the last item inserted.
# A Stack is a data structure that follows the LIFO(Last In First Out) principle. 

# A stack has two simple operations:
# push - It adds an element to the top (i.e., end) of the stack.
# pop - It removes an element from the top (i.e., end) of the stack.

# class MyStack(object):
#     def __init__(self, max):           # Constructor
#         """Initialize the stack with a fixed size."""
#         self.__stackList = [None] * max  # The stack stored as a list
#         self.__top = -1                  # No items initially
#         self.__maxSize = max             # Max size of the stack   

#     def getStack(self):
#         """Retrieve the current state of the stack."""
#         return self.__stackList
    
#     def push(self, item): 
#         """
#         Insert an item at the top of the stack.
#         Returns the index of the item if successful, or -1 if the stack is full.
#         """
#         #ADD YOUR CODE HERE
        
#     def pop(self):    
#         """
#         Remove the top item from the stack.
#         Returns the item if successful, or -1 if the stack is empty.
#         """
#         ## ADD YOUR CODE HERE
    
class MyStack(object):
    def __init__(self, max):           # Constructor
        """Initialize the stack with a fixed size."""
        self.__stackList = [None] * max  # The stack stored as a list
        self.__top = -1                  # No items initially
        self.__maxSize = max             # Max size of the stack   

    def getStack(self):
        """Retrieve the current state of the stack."""
        return self.__stackList
    
    def push(self, item): 
        """
        Insert an item at the top of the stack.
        Returns the index of the item if successful, or -1 if the stack is full.
        """
        if self.__top < self.__maxSize - 1:
            self.__top += 1
            self.__stackList[self.__top] = item
            return self.__top
        else:
            return -1  # Stack is full
        
    def pop(self):    
        """
        Remove the top item from the stack.
        Returns the item if successful, or -1 if the stack is empty.
        """
        if self.__top >= 0:
            item = self.__stackList[self.__top]
            self.__stackList[self.__top] = None  # Clear the reference
            self.__top -= 1
            return item
        else:
            return -1  # Stack is empty