# 707

from utils import *

class Node:
    """
    Used to represent a node in a singly linked list
    """
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class MyLinkedList:
    """
    Class that represents a singly linked list
    """
    def __init__(self):
        """
        Initialize an empty linked list
        """
        self.head = None
        self.num_nodes = 0

    def get(self, index: int) -> int:
        """
        Gets the value of the `index` th node in the linked list. Returns -1 if the index is invalid
        """
        # if the list is empty or index is invalid
        if not self.head or not 0 <= index <= self.num_nodes - 1:
            return -1
        
        curr_idx = 0
        temp = self.head
        while temp:
            if curr_idx == index:
                return temp.val
            curr_idx += 1
            temp = temp.next
            
    def addAtHead(self, val: int) -> None:
        """
        Adds a node of value `val` before the first element of the linked list
        """
        new = Node(val)
        if not self.head:
            self.head = new
        else:
            new.next = self.head
            self.head = new
        self.num_nodes += 1
    
    def addAtTail(self, val: int) -> None:
        """
        Appends a node of value `val` as the last element of the linked list
        """
        new = Node(val)
        if not self.head:
            self.head = new
        else:
            curr = self.head
            while curr:
                if not curr.next:
                    curr.next = new
                    break
                curr = curr.next
        self.num_nodes += 1

    def addAtIndex(self, index: int, val: int) -> None:
        """
        Adds a node of value `val` before the `index` th node in the linked list. If `index` equals the length of the linked list, the node will be appended to the end of the linked list. If `index` is greater than the length, the node will not be inserted
        """
        new = Node(val)
        
        if not self.head:
            if index == 0:
                self.head = new
                self.num_nodes += 1
        else:
            if 0 <= index <= self.num_nodes:
                temp, curr_idx = self.head, 0
                if index == self.num_nodes:
                    while temp:
                        if not temp.next:
                            temp.next = new
                            break
                        temp = temp.next
                else:
                    prev = None
                    while temp:
                        if curr_idx == index:
                            new.next = temp
                            if not prev:
                                self.head = new
                            else:
                                prev.next = new
                            break
                        curr_idx += 1
                        prev = temp
                        temp = temp.next

                self.num_nodes += 1
    
    def deleteAtIndex(self, index: int) -> None:
        """
        Deletes the `index` th node in the linked list, if the index is valid
        """
        if self.head:
            if 0 <= index <= self.num_nodes - 1:
                temp, prev = self.head, None
                curr_idx = 0
                while temp:
                    if curr_idx == index:
                        if not prev:
                            self.head = temp.next
                        else:
                            prev.next = temp.next
                    curr_idx += 1
                    prev = temp
                    temp = temp.next

                self.num_nodes -= 1

obj = MyLinkedList()

obj.addAtHead(1)
print(f"Number of nodes: {obj.num_nodes}")
traverse(obj.head)

obj.addAtTail(3)
print(f"Number of nodes: {obj.num_nodes}")
traverse(obj.head)

obj.addAtIndex(1, 2)
print(f"Number of nodes: {obj.num_nodes}")
traverse(obj.head)

print(obj.get(1))

obj.deleteAtIndex(1)
print(f"Number of nodes: {obj.num_nodes}")
traverse(obj.head)

print(obj.get(1))
print(obj.get(3))

obj.deleteAtIndex(3)
print(f"Number of nodes: {obj.num_nodes}")
traverse(obj.head)

obj.deleteAtIndex(0)
print(f"Number of nodes: {obj.num_nodes}")
traverse(obj.head)

print(obj.get(0))

obj.deleteAtIndex(0)
print(f"Number of nodes: {obj.num_nodes}")
traverse(obj.head)

print(obj.get(0))