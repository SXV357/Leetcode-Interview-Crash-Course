# 19

from typing import Optional
from utils import *

def removeNthFromEnd(head: Optional[ListNode], n: int) -> Optional[ListNode]:
        """
        Time complexity: O(n) because if n == 1 meaning the last element needs to be deleted we end up iterating through all elements in the list
        Space complexity: O(1) because the only variable we're storing are pointers which aren't dependent on input size
        """
        # start both pointers at the head
        slow = fast = head

        # this problem is similar to the return kth node from the end of the list and the idea behind that is to move both the pointers thru the list separated by a distance of k but it's n here

        # the fast pointer is the one that will originally be positioned at a distance n from the slow pointer and we will then move both pointers thru the list one node at a time
        for _ in range(n):
            fast = fast.next
        
        # we maintain this pointer because we are dealing with deletion and to do so we need to update the next pointer of the target node's previous node to delete the current element
        prev = None
        
        # we only need to check the validity of the fast pointer because by the time fast becomes NULL slow will be at a distance of n from fast and we will have the node that we want to delete

        while fast:
            prev = slow # along each step of the iteration we update the prev pointer so by the time the loop exits and slow hits the desired node we have the prev pointer of the target node
            # both the pointers are moved thru the list one node at a time
            slow = slow.next
            fast = fast.next
        
        # after we break out we have two cases

        # the previous pointer is not NULL and in that case we can update its next to point to the next of slow since slow will hold a reference to the nth node
        if prev:
            prev.next = slow.next
        # this happens when n = length of the list so after initially moving fast fast will be NULL and the while loop never executes so in that case we are essentially deleting the head so we update head to now point to its next node
        else:
            head = head.next

        return head 