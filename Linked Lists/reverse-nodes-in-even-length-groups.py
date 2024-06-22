# 2074

from utils import *
from typing import Optional
import unittest

class Solution:
    def reverseEvenLengthGroups(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Time complexity: First loop to count number of nodes runs in O(curr_group) time and while loop to do reversal also runs in O(curr_group) time since we only need to iterate over `curr_group` nodes in order to do the reversal. outer while loop at the worst runs for the number of times which is equal to when the sum of the first `k` natural numbers equals `n` where `n` is the size of the list
        Space complexity: O(1) because we're just storing integers and pointers in memory and they aren't dependent on list size
        """
        
        # prev is used because once we reverse a valid section we connect prev to the head of the new list
        # fast_prev is used in cases when we're dealing with a group of an odd number of nodes. even though no reversal happens we still need a reference to the prev pointer of the next group so that if it's valid we're set 
        prev = fast_prev = head
        # both the pointers are used for the reversal process where the reversal starts at the slow node and ends at the node right before fast. start at head.next because the head never needs to be modified
        slow = fast = head.next
        # in every single test case, we never delete the head node which belongs to group 1 so we begin at group 2 and start checking from there. this is used to count number of nodes in a given group since it is possible that we encounter the edge cases as described above
        curr_group = 2
        # we don't know how many reversals will happen so we loop infinitely
        while True:
            # the counting begins from the current node where slow and fast are correctly positioned and we include the current node when we begin
            num_nodes = 1
            # this is to detect when we reach the end of the list so that we don't keep looping for the desired count of nodes and encounter null pointer exceptions
            flag = False

            # since the group number dictates how many nodes it "usually" contains we loop those many times so that we have a start and end bound for the group which needs to be reversed
            for i in range(curr_group):
                # if it reaches the end of list and even if we haven't looped over the actual group number count we still break out to avoid any errors. all we care is that we're working with an even number of nodes
                if not fast:
                    flag = True
                    break
                # if we're in the middle of the list and don't encounter the first condition, when the loop ends fast is positioned at a node that is not part of the group to be reversed so we have the following conditions below to check and then update the count of nodes appropriately
                if fast.next and i != curr_group - 1:
                    num_nodes += 1
                fast_prev = fast
                fast = fast.next
            
            # if we reached the end of the list and don't have an even number of nodes just stop and return the head otherwise the reversal goes on as normal
            if flag and num_nodes % 2 != 0:
                break
            
            # the reversal can only be done when the current group has an even number of nodes
            if num_nodes % 2 == 0:
                # once the group is reversed the original head's next pointer will point to fast
                modified_prev = fast
                curr = slow
                # we only want to reverse the group starting at slow going until one node before fast
                while curr is not fast:
                    next_node = curr.next
                    curr.next = modified_prev
                    modified_prev = curr
                    curr = next_node
                
                # the original node before fast becomes the new head so connect prev to that
                prev.next = modified_prev
                # now that we have done the reversal we need to move on to the next group and do all the same checks as above so now prev is modified to slow(the original slow now becomes the tail of the list or essentially fast's prev pointer)
                prev = slow
                # position slow and fast once again at the same node to carry forward the process
                slow = fast
                # increment the group count because for each group we still need the checks for valid number of nodes
                curr_group += 1
            else:
                # if this group has an odd number of nodes then no reversal happens but we have a reference to the prev pointer of the next group so we update that
                prev = fast_prev
                # once again align fast and slow and increment group count
                slow = fast
                curr_group += 1
        
        return head 

class TestReverseInEven(unittest.TestCase):#
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