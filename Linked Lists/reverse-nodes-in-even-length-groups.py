# 2074

from utils import *
from typing import Optional
import unittest

class Solution:
    def reverseEvenLengthGroups(self, head: Optional[ListNode]) -> Optional[ListNode]:        
        # edge cases for last group in the list:
            # odd group but even number of nodes - need to be reversed
            # even group but odd number of nodes - leave it the way it is

        # potential algorithm:
            # in an infinite loop
                # set a prev pointer to begin at head
                # set a fast and slow pointer to begin at head.next
                # including where fast is currently iterate current group number of times to find number of nodes and move fast to the appropriate location
                # if the number of nodes is not positive, break
                # otherwise, reverse the group from slow to fast.prev
                # update the original prev to point to the reversed sections new head and the tail to point to fast then update slow to point to fast and prev to point to slow
                # repeat
        
        prev = fast_prev = head # once we have reversed the list prev will need to be connected to the new head to maintain the list
        slow = fast = head.next # we will use these to check for valid node count and also for the reversal
        curr_group = 2 # start at group 2 because we have already dealt with the single and 2 node cases
        while True:
            num_nodes = 1
            flag = False

            # after this loop fast points to the head of the new list where slow and fast will again be repositioned
            for i in range(curr_group):
                if not fast:
                    flag = True
                    break
                if fast.next and i != curr_group - 1:
                    num_nodes += 1
                fast_prev = fast
                fast = fast.next
            
            if flag and num_nodes % 2 != 0:
                break

            # print(f"original address of slow: {hex(id(slow))} and its val: {slow.val}")

            if num_nodes % 2 == 0: # do the reversal
                modified_prev = fast
                curr = slow
                while curr is not fast:
                    next_node = curr.next
                    curr.next = modified_prev
                    modified_prev = curr
                    curr = next_node
                
                prev.next = modified_prev
                # print(f"new address of slow: {hex(id(slow))} and its val: {slow.val}")
                prev = slow
                slow = fast
                curr_group += 1
            else:
                prev = fast_prev
                slow = fast
                curr_group += 1
        
        return head 

class TestReverseInEven(unittest.TestCase):
    sol = Solution()

    def test_one(self):
        head = array_to_ll([1])
        modified = self.sol.reverseEvenLengthGroups(head)
        self.assertEqual(ll_to_array(modified), [1])

    def test_two(self):
        head = array_to_ll([3, 7])
        modified = self.sol.reverseEvenLengthGroups(head)
        self.assertEqual(ll_to_array(modified), [3, 7])

    def test_three(self):
        head = array_to_ll([5,2,6,3,9,1,7,3,8,4])
        modified = self.sol.reverseEvenLengthGroups(head)
        self.assertEqual(ll_to_array(modified), [5,6,2,3,9,1,4,8,3,7])

    def test_four(self):
        head = array_to_ll([1,1,0,6])
        modified = self.sol.reverseEvenLengthGroups(head)
        self.assertEqual(ll_to_array(modified), [1,0,1,6])

    def test_five(self):
        head = array_to_ll([1,1,0,6,5])
        modified = self.sol.reverseEvenLengthGroups(head)
        self.assertEqual(ll_to_array(modified), [1,0,1,5,6])

if __name__ == "__main__":
    unittest.main()