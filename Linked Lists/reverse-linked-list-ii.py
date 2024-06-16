# 92

from typing import Optional
from utils import *

class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        """
        Time complexity: O(left - 1) + (2 * O(right - left)) but in the worst case O(n) because if left = 1 and right = `n` then we reverse the whole list
        Space complexity: O(1) because the only variables we're storing are pointers
        """
        # handle the case where the list is empty or when there's only one node in the list
        if not head or not head.next:
            return head
        
        # based on the range given we want to position two pointers at those respective nodes so that we can do the reversal accordingly so we initialize two of them to start at the head
        start = end = head
        # in cases where the reversal is not done from the head we need to ensure the list remains connected and this serves as the link for that
        start_prev = None

        # left represent's the nth node in the list from the head and since we can treat the list as 0-indexed we need to iterate left - 1 times so that we can position start at the correct node
        # start's previous pointer is updated along the way because we need to it connect the list after it's reversed
        # we also update the pointer that should point to the end node so that next time when it needs to be updated we don't have to start from the beginning
        for _ in range(left - 1):
            start_prev = start
            start = start.next
            end = end.next
        
        # the distance to move in order to position end at the right node is right - left so we iterate those many times to position the pointer in the appropriate spot
        for _ in range(right - left):
            end = end.next
        
        # save this beforehand because we need to connect the beginning node to this node and also because it's used as the stopping condition for the loop where the reversal takes place
        end_next = end.next
    
        curr = start # the reversal begins from here so initialize a pointer to start from this place
        prev = end.next # in a normal list reversal where the whole list is reversed prev is initialized to None but it starts here because to begin with we need to make the beginning node point to this node and then move thru the remaining nodes

        # the end condition is this because we need to update all pointers from start to end and once we reach end's next we can terminate because we don't need it for the reversal
        # standard reversal process below where we always save the next node, update curr's next pointer to point to the previous node and update curr to point to what was originally at prev
        while curr is not end_next:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node

        # if start's prev pointer is none it means the list's head will change so we simply update the head to point to the end node because in the reversal the end node becomes the start node
        if not start_prev:
            head = end
        # in other cases we simply link start's prev to the end node to link the list back together
        else:
            start_prev.next = end
        
        return head

one = ListNode(1)
two = ListNode(2)
three = ListNode(3)
four = ListNode(4)
five = ListNode(5)

one.next = two
two.next = three
three.next = four
four.next = five
head = one

# sol = Solution()
# modified = sol.reverseBetween(head, 1, 3)
# traverse(modified)