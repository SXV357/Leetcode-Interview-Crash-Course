# 1721

from utils import *
from typing import Optional

class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        """
        Time complexity: O(2k - 1 + n)
        - O(k - 1) to position first node in the right spot
        - O(k) to position the fast pointer in lieu of obtaining the kth node from the end
        - O(n) in the worst case to position the second node in the right spot
        - Remaining operations involve pointer manipulation so all are O(1)
        Space complexity: O(1) because we're only dealing with pointers which take up constant space
        """
        # we have nothing to swap if there's just one node in the list so we return the list as is
        if not head.next:
            return head
        
        # to store the previous nodes of both the nodes respectively
        first_prev = second_prev = None
        first = head

        # gets the first node to be swapped
            # positions first at the first node that needs to be swapped
            # updates first_prev to point to the first node's previous node
        for _ in range(k - 1):
            first_prev = first
            first = first.next
        
        # gets the second node to be swapped
            # very similar to the find nth node in the list problem where we use 2-pointers(fast and slow)
            # separate fast by a distance of k from slow and move them thru the list one node at a time until fast becomes invalid because at this point slow will point to the nth node from the tail which is what we want
        second = fast = head
        for _ in range(k):
            fast = fast.next
        
        while fast:
            second_prev = second
            second = second.next
            fast = fast.next
        
        # stores the next nodes of both the nodes respectively
        first_next, second_next = first.next, second.next

        # Edge case: first node is positioned to the right of the second node
        
        # Case 1: The first node is at the tail and the second node is at the head
        if not first_next and not second_prev:
            first.next = second_next if second_next is not first else second
            second.next = first_next
            if first_prev is not second:
                first_prev.next = second
            head = first
            return head
        # Case 2: The two nodes are somewhere in the middle of the list but both are right next to each other
        elif second_next == first and first_prev == second:
            second_prev.next = first
            first.next = second
            second.next = first_next
            return head
        # Case 3 but no test cases generated for it: The two nodes are somewhere in the middle of the list but both are not right next to each other
        
        # *********************************************************************
        
        # Normal case: second node is positioned to the right of the first node
        
        # Case 1: swap head and tail
        if not first_prev and not second_next:
            # Sub-case 1: the nodes are right next to each other
            if first_next == second and second_prev == first:
                second.next = first
                first.next = second_next
                head = second
            # Sub-case 2: the nodes are separated by atleast 1 node
            else:
                second.next = first_next
                head = second
                second_prev.next = first
                first.next = second_next
        # Case 2: swap two middle nodes
        else:
            # Sub-case 3: the nodes are right next to each other
            if first_next == second and second_prev == first:
                first_prev.next = second
                second.next = first
                first.next = second_next
            # Sub-case 4: the nodes are spaced apart by atleast one node
            else:
                first_prev.next = second
                second.next = first_next
                second_prev.next = first
                first.next = second_next
        
        return head

head = array_to_ll([55,60,78,53,93,37,31,4,61,11,13,51,34,83,24,96,5,77,1,67])
sol = Solution()
modified = sol.swapNodes(head, 11)
traverse(modified)