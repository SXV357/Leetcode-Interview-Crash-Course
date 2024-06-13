class ListNode():
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# FAST AND SLOW POINTER TECHNIQUE
    # THE FAST POINTER MOVES 2 NODES AT A TIME AND THE SLOW POINTER MOVES ONLY ONE NODE AT A TIME
    # WE NEED TO CHECK FOR THE VALIDITY OF FAST.NEXT BECAUSE IF FAST IS THE TAIL NODE OF THE LIST(IT IS THE ONLY ONE THEN FAST.NEXT IS NULL AND ACCESSING NULL.NEXT WOULD RESULT IN A NULL-POINTER EXCEPTION)

# head is the head node of a linked list

# function fn(head):
#     slow = head
#     fast = head

#     while fast and fast.next:
#         Do something here
#         slow = slow.next
#         fast = fast.next.next

def return_middle(head: ListNode) -> int:
    """
    Given the head of a linked list with an odd number of nodes head, return the value of the node in the middle.
    Time complexity: O(n) for `n` nodes in the linked list because in the worst case we end up traversing thru every single node before we return the middle one
    Space complexity: O(1) because the pointers aren't dependent on list size and take up constant space
    """
    
    def non_optimal(head: ListNode):
        # without using the fast-slow pointer approach
            # traverse list once counting number of nodes
            # traverse again maintaining counter of how many nodes visited and return the appropriate middle node
        num_nodes = 0
        temp = head
        while temp:
            num_nodes += 1
            temp = temp.next
        
        mid, curr, idx = num_nodes // 2, head, 0

        while curr:
            if idx == mid:
                return curr.val
            idx += 1
            curr = curr.next
    
    # optimal solution that uses the fast-slow pointer approach

    # key here is to realize that if we have an odd number of nodes then at the time of the while loop termination the slow pointer will have the value of the middle node
        # let's say the list is 1 -> 2 -> 3 -> 4 -> 5
        # both fast and slow start at the head
        # on the first iteration fast advances to 3 and slow advances to 2
        # on the second iteration slow advances to 3 and fast advances to 5
        # on the third iteration fast.next is NULL so we break out and return slow.val
        # at this point slow points to 3 which is precisely the middle node 
    
    slow = fast = head # both pointers initially start at the head but will move at different paces thru the list
    # the current fast pointer needs to be valid since we're accessing fast.next and fast.next needs to be valid since we're accessing fast.next.next
    while fast and fast.next:
        slow = slow.next # just moves thru the list one node at a time
        fast = fast.next.next # moves thru the list 2 nodes at a time because fast.next is the first node skipped and it then moves onto the next of the next one

    return slow.val # since slow moves 1/2 as fast as the quick pointer it would be at the middle of the list by the time fast reaches the end