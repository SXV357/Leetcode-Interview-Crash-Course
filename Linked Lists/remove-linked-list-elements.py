# 203

from utils import *
from typing import Optional
import unittest

class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:  
        """
        Time complexity: O(n) because in the case where the list is not empty we iterate `n` times through it
        Space complexity: O(1) because the only variables we're using are pointers
        """
        # to delete all target elements which are not the head we need a reference to its prev pointer     
        prev, curr = None, head
        while curr:
            if curr.val == val:
                # if we find the element to delete but it's the head we simply update the head to point to its next element
                if not prev:
                    head = curr.next
                # in other cases when we change what the target element's prev node points to we delete the current element
                else:
                    prev.next = curr.next
            else:
                # we need to do this so by the time we find the correct node we have a reference to its previous node
                prev = curr
            curr = curr.next
        
        return head
    
class TestRemoveElements(unittest.TestCase):
    sol = Solution()

    def test_one(self):
        head = array_to_ll([1,2,6,3,4,5,6])
        modified = self.sol.removeElements(head, 6)
        self.assertEqual(ll_to_array(modified), [1,2,3,4,5])
    
    def test_two(self):
        head = array_to_ll([])
        modified = self.sol.removeElements(head, 1)
        self.assertEqual(ll_to_array(modified), [])
    
    def test_three(self):
        head = array_to_ll([7,7,7,7])
        modified = self.sol.removeElements(head, 7)
        self.assertEqual(ll_to_array(modified), [])
    
if __name__ == "__main__":
    unittest.main()