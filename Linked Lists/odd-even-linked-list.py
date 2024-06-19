# 328

from utils import *
from typing import Optional

class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # handling the cases for no nodes, 1 node, and 2 nodes
        if (not head) or (not head.next) or (not head.next.next):
            return head

        # O(n) time O(1) space approach
        
        odd_head = odd_prev = head
        even_head = even_prev = head.next
        idx = 1 # depending on this we will manipulate the appropriate pointers

        fast = even_head.next
        while fast:
            # fast_next = fast.next
            if idx % 2 != 0:
                odd_prev.next = fast
                odd_prev = fast
            else:
                even_prev.next = fast
                even_prev = fast
            idx += 1
            fast = fast.next
        
        even_prev.next = None
        odd_prev.next = even_head

        return odd_head


sol = Solution()
head = array_to_ll([1,2,3,4,5])
traverse(sol.oddEvenList(head))