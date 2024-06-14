# 83

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def deleteDuplicates(head: Optional[ListNode]) -> Optional[ListNode]:
    """
    Time complexity: O(n) - the maximum number of iterations that can take place is `n` where `n` is the number of nodes in the list
    Space complexity: O(n) -if no duplicates at all then we add `n` values to the set
    """
    # since the list is already sorted we don't need to worry about that but what we can do to keep track of duplicates is to use a set since we can check if a value has already been seen before to determine if its duplicate

    seen = set() # this set will keep track of visited values
    temp = head # dummy pointer so we don't lose the original pointer to the head
    prev = None # previous pointer since when we're deleting some element we need to modify the next pointer of this element's previous element

    while temp:
        if temp.val in seen: # this is a duplicate value and needs to be deleted
            # modify the next pointer of the previous element to point to this element's next one
            # if li = 1 -> 2 -> 3 -> 4 and we're deleting 2, we need to modify the next pointer of 1 to point to 3 now instead of 2 where 1 is prev and 3 is curr.next
            prev.next = temp.next
        else:
            seen.add(temp.val) # this value hasn't been encountered previously so we add it to the set
            # the reason we only update prev in this case is because we don't want to have a deleted node as prev since that will lead to null pointer exceptions
            prev = temp
                
        temp = temp.next # to ensure continuous iteration update the current pointer
        
    return head # since head is never deleted but the internal nodes may or may not be modified we just return a reference to the head