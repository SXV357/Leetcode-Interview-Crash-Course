# 2095

from typing import Optional
from utils import *
import unittest

class Solution:
    def deleteMiddle(self, head: ListNode) -> ListNode:
        """
        Time complexity: O(n) because at the worst we will iterate through all `n` elements before we find the middle node
        Space complexity: O(1) because the only variables we're working with are pointers
        """
        # if the list is empty or there is just one node we just return an empty list because the middle node would end up being that one node
        if not head or not head.next:
            return None
        
        prev = None # the idea behind maintaining this is that to delete the middle node we need to update the next pointer of its previous node
        fast = slow = head # we will use a fast and slow pointer approach to reach the middle node

        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        
        prev.next = slow.next # after the loop ends slow points to the middle node and prev points to slow's previous so to delete slow we change what previous' next points to

        return head

class TestDeleteMiddle(unittest.TestCase):
    sol = Solution()

    def test_one(self):
        head = array_to_ll([1,3,4,7,1,2,6])
        modified = self.sol.deleteMiddle(head)
        self.assertEqual(ll_to_array(modified), [1,3,4,1,2,6])

    def test_two(self):
        head = array_to_ll([1,2,3,4])
        modified = self.sol.deleteMiddle(head)
        self.assertEqual(ll_to_array(modified), [1,2,4])

    def test_three(self):
        head = array_to_ll([2,1])
        modified = self.sol.deleteMiddle(head)
        self.assertEqual(ll_to_array(modified), [2])

if __name__ == "__main__":
    unittest.main()