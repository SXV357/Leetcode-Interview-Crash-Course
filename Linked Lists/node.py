# creating a class that represents a SinglyNode in a linked list
class SinglyNode():
    def __init__(self, val):
        self.val = val # this is the value associated with the SinglyNode
        self.next = None # this is a pointer that points to the next SinglyNode in the list

one = SinglyNode(1)
two = SinglyNode(2)
three = SinglyNode(3)

# establishing the linked list
one.next = two
two.next = three
head = one

# Traversal
def traverse(head: SinglyNode) -> None:
    # for a singly linked list like we have created the only way to access any element down the line or basically perform any operation is to iterate from the head in the forward direction
    temp = head # save it into a temporary variable because we don't want to modify the original one

    # as long as the current SinglyNode is not null we keep iterating and printing its value
    while temp:
        if temp.next is not None:
            print(f"{temp.val}->", end = "")
        else:
            print(temp.val)
        temp = temp.next

def insert(target: SinglyNode, to_insert: SinglyNode) -> None:
    """
    O(1) because we already have a reference to the pointer after which the SinglyNode needs to be inserted otherwise it will be O(n) since we would need to iterate from the head until we reach the desired SinglyNode
    """
    # insert a SinglyNode in a linked list such that it is inserted after the SinglyNode passed in as input

    # loop approach
        # start from the head and keep iterating until we encounter the SinglyNode passed in as a parameter and insert the new SinglyNode after that
        # for the tail insertion just one pointer needs to be updated
        # for the insertion in the middle two pointers need to be updated in order to maintain list integrity

    # temp = head
    # while temp:
    #     if temp == target:
    #         if temp.next is None:
    #             temp.next = to_insert
    #         else:
    #             to_insert.next = target.next
    #             target.next = to_insert
    #     temp = temp.next
    
    # standard approach without using a loop
    to_insert.next = target.next
    target.next = to_insert

def delete(prev: SinglyNode, to_delete: SinglyNode) -> None:
    # deleting element after prev
    prev.next = to_delete.next

class DoublyNode():
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None

double_one = DoublyNode(1)
double_two = DoublyNode(2)
double_three = DoublyNode(3)
double_four = DoublyNode(4)

# establishing the doubly linked list
double_one.next = double_two

double_two.prev = double_one
double_two.next = double_three

double_three.prev = double_two
double_three.next = double_four

double_four.prev = double_three
doubly_head = double_one

def add_node(node: DoublyNode, node_to_add: DoublyNode) -> None:
    # add node_to_add after node
    node_to_add.next = node.next
    if node.next is not None:
        node.next.prev = node_to_add
    node_to_add.prev = node
    node.next = node_to_add

def traverse_doubly(head: DoublyNode):
    current = head
    while current:
        print(f"[{current.val}]", end=" <-> " if current.next else "")
        current = current.next

new = DoublyNode(1.5)

def insert_routine():
    print(f"List before adding 1.5")
    traverse_doubly(doubly_head)

    add_node(doubly_head, new)

    print(f"List after adding 1.5")
    traverse_doubly(doubly_head)

def delete_node(node: DoublyNode) -> None:
    node.prev.next = node.next
    node.next.prev = node.prev

def delete_routine():
    delete_node(new)

    print(f"List after deleting 1.5")
    traverse_doubly(doubly_head)

traverse_doubly(doubly_head)
print("\n")

add_head, add_tail = DoublyNode(0.5), DoublyNode(4.5)

def prepend(head: DoublyNode, node_to_add: DoublyNode) -> DoublyNode:
    # node to be added becomes the new head
    if not head:
        head = node_to_add
    
    node_to_add.next = head
    head.prev = node_to_add
    head = node_to_add

    return head

doubly_head = prepend(doubly_head, add_head)
traverse_doubly(doubly_head)
print("\n")

def append(tail: DoublyNode, node_to_add: DoublyNode):
    # node to be added becomes the new tail
    if not tail:
        tail = node_to_add
    
    tail.next = node_to_add
    node_to_add.prev = tail
    tail = node_to_add

append(double_four, add_tail)
traverse_doubly(doubly_head)
print("\n")

def remove_from_start(head: DoublyNode):
    if not head:
        return
    
    next_node = head.next
    if not next_node:
        head = None
    else:
        next_node.prev = head.prev
        head.next = None
        head = next_node
    
    return head

doubly_head = remove_from_start(add_head)
traverse_doubly(doubly_head)
print("\n")

def remove_from_end(tail: DoublyNode):
    if not tail:
        return
    
    prev_node = tail.prev
    if not prev_node:
        tail = None
    else:
        prev_node.next = tail.next
        tail.prev = None
        tail = prev_node

remove_from_end(add_tail)
traverse_doubly(doubly_head)
print("\n")