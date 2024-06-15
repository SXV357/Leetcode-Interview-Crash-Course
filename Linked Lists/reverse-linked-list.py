# 206

from typing import Optional
from utils import *

# LINKED LIST REVERSAL

# let's say the list is 1->2->3->4->5 and we want to output 5->4->3->2->1
# the underlying idea behind a linked list reversal is that for whichever element we're currently on we need to update its next pointer to point to whatever its previous was
    # for example 1 is now the head but when we reverse it it becomes the new tail and we know that tail node's next pointers are null but we also know that head pointer previous is also None
    # this process will be repeated for all elements until we reach the end of the list

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Time complexity: O(n) because the reversal requires iterating through all nodes in the list
        Space complexity: O(1) because no variables being used that depend on the input size
        """
        # we maintain a prev pointer because on each iteration we will update the next pointer of the current one point to the prev node
        prev = None
        # this is simply which node we're currently on in the list
        curr = head
        while curr:
            # the reason we save the current node's next pointer is that since we're updating curr.next to prev we don't want to lose the next node since that's what we'll be moving on to in the list once we've updated it for the current one
            next_node = curr.next
            # take the current node and update its next pointer to point to the previous one so on the first iteration we do 1.next = None because in the resulting list that's the case
            curr.next = prev
            # we need to update the previous pointer because like the original example we need to modify the following pointers:
                # 1.next, 2.next, 3.next, 4.next, 5.next
                # for all the above we need a reference to the updated prev pointer else it won't work so once we've updated the current pointer we update prev as well to ensure its updated properly
            prev = curr
            # since we saved the next node we can just update curr to move onto that now and the process continues
            curr = next_node
        
        # the new head of the list once the loop completes is prev because prev will come to 5 and curr will go to NULL so when we're returning prev at the end we're basically returning the head

        return prev