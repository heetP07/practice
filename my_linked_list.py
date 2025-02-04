# A SIMPLE LINKED LIST
# A linked list is a data structure where each element (node) is linked to the next.
# Each node contains data and a reference (pointer) to the next node.

# class MyListNode:
#     def __init__(self, data, next=None):
#         """
#         Constructor to initialize a node.
#         :param data: Data to be stored in the node.
#         :param next: Reference to the next node (default is None).
#         """
#         self.__data = data  # The data for this node.
#         self.__next = next  # Reference to the next node.

#     def getData(self):
#         """Return the data stored in this node."""
#         return self.__data

#     def setData(self, data):
#         """Set the data for this node."""
#         self.__data = data

#     def getNext(self):
#         """Return the reference to the next node."""
#         return self.__next

#     def setNext(self, link):
#         """
#         Set the reference to the next node.
#         :param link: The next node (must be of type MyListNode or None).
#         """
#         if link is None or isinstance(link, MyListNode):
#             self.__next = link
#         else:
#             raise Exception("Next link must be MyListNode or None")

#     def isLast(self):
#         """Check if this node is the last in the list."""
#         return self.getNext() is None


# class MyLinkedList:
#     def __init__(self):
#         """Constructor to initialize an empty linked list."""
#         self.__head = None  # Head of the linked list.

#     def getHead(self):
#         """Return the head node of the linked list."""
#         return self.__head

#     def setHead(self, node):
#         """
#         Set the head node of the linked list.
#         :param node: The new head node (must be of type MyListNode or None).
#         """
#         if node is None or isinstance(node, MyListNode):
#             self.__head = node
#         else:
#             raise Exception("Head node must be MyListNode or None")

#     def isEmpty(self):
#         """Check if the linked list is empty."""
#         return self.__head is None

#     def insert(self, data):
#         """Insert a new node at the head of the linked list."""
#         ## ADD YOUR CODE HERE

#     def remove(self):
#         """
#         Remove the head node of the linked list.
#         :return: The data of the removed node, or -1 if the list is empty.
#         """
#         ## ADD YOUR CODE HERE
#         return -1

#     def find(self, item):
#         """
#         Search for a node with the specified data.
#         :param item: The data to search for.
#         :return: The node containing the data, or None if not found.
#         """
#         current = self.getHead()
#         while current:
#             if current.getData() == item:
#                 return current
#             current = current.getNext()
#         return None

#     def getCount(self):
#         """Return the number of nodes in the linked list."""
#         count = 0
#         node = self.getHead()
#         while node:
#             count += 1
#             node = node.getNext()
#         return count

#     def insertAt(self, goal, data):
#         """
#         Insert a new node with the specified data after a node with the specified goal data.
#         :param goal: The data of the node after which the new node should be inserted.
#         :param data: The data for the new node.
#         :return: True if the insertion was successful, False otherwise.
#         """
#         ## ADD YOUR CODE HERE
#         return False

#     def removeItem(self, item):
#         """
#         Remove the first node with the specified data.
#         :param item: The data of the node to remove.
#         :return: True if the node was removed, False otherwise.
#         """
#         ## ADD YOUR CODE HERE
#         return False

class MyListNode:
    def __init__(self, data, next=None):
        self.__data = data
        self.__next = next

    def getData(self):
        return self.__data

    def setData(self, data):
        self.__data = data

    def getNext(self):
        return self.__next

    def setNext(self, link):
        if link is None or isinstance(link, MyListNode):
            self.__next = link
        else:
            raise Exception("Next link must be MyListNode or None")

    def isLast(self):
        return self.getNext() is None


class MyLinkedList:
    def __init__(self):
        self.__head = None

    def getHead(self):
        return self.__head

    def setHead(self, node):
        if node is None or isinstance(node, MyListNode):
            self.__head = node
        else:
            raise Exception("Head node must be MyListNode or None")

    def isEmpty(self):
        return self.__head is None

    def insert(self, data):
        """Insert a new node at the head of the linked list."""
        new_node = MyListNode(data)
        new_node.setNext(self.__head)
        self.__head = new_node

    def remove(self):
        """Remove the head node and return its data."""
        if self.isEmpty():
            return -1
        removed_data = self.__head.getData()
        self.__head = self.__head.getNext()
        return removed_data

    def find(self, item):
        """Search for a node with the specified data."""
        current = self.getHead()
        while current:
            if current.getData() == item:
                return current
            current = current.getNext()
        return None

    def getCount(self):
        """Return the number of nodes in the linked list."""
        count = 0
        node = self.getHead()
        while node:
            count += 1
            node = node.getNext()
        return count

    def insertAt(self, goal, data):
        """Insert a new node after the node with the specified goal data."""
        current = self.__head
        while current:
            if current.getData() == goal:
                new_node = MyListNode(data, current.getNext())
                current.setNext(new_node)
                return True
            current = current.getNext()
        return False

    def removeItem(self, item):
        """Remove the first node with the specified data."""
        if self.isEmpty():
            return False

        if self.__head.getData() == item:
            self.__head = self.__head.getNext()
            return True

        prev = None
        current = self.__head
        while current and current.getData() != item:
            prev = current
            current = current.getNext()

        if current:
            prev.setNext(current.getNext())
            return True

        return False
    