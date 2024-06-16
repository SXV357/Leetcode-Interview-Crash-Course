from typing import Optional
import unittest
from utils import *
from collections import defaultdict

def deleteDuplicatesNonOptimal(head: Optional[ListNode]) -> Optional[ListNode]:
    # Non optimal solution for the problem that leverages a hashmap to detect if an element appears more than once

    # Algorithm:
        # store the node's values along with their frequencies in a dictionary
        # iterate through the linked list
        # for each value whose frequency when looked up in the dictionary exceeds 1, delete it
    
    # extra computational complexity since we need to traverse thru the entire list once to get frequencies and then traverse again for deletion

    if not head or not head.next:
        return head

    freq, dummy = defaultdict(int), head
    while dummy:
        freq[dummy.val] += 1
        dummy = dummy.next
                
    curr, prev = head, None
    while curr:
        if freq[curr.val] > 1: # we delete this element
            next_node = curr.next
            if not prev:
                head = next_node
            else:
                prev.next = curr.next
            curr = next_node
        else:
            prev = curr
            curr = curr.next
        
    return head

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Time complexity: O(n) because in the worst case there are no duplicates and we traverse thru the whole list w/o deleting a single node
        Space complexity: O(1) because the only variables that take up memory are pointers
        """
        # if the list is empty or there's just one node there's nothing to delete so return the list as is
        if not head or not head.next:
            return head

        curr = head # this is the temporary variable used during the iteration process
        # prev is used so that when we have to delete a node that's not the head we can update its next pointer to point to the target element's next node
        # target here is the biggest modification from the first solution and will serve as the way to detect if a value appears more than once in the list
        prev = target = None

        while curr:
            # the key is that since the list is already sorted if an element appears more than once then those same values will be positioned adjacent to each other in the linked list so we can simply compare adjacent nodes and store the duplicate value that exists in the target variable so that if there's multiple of the current node we can just compare future nodes' values with target and then delete
            # one thing to keep in mind is that target will only update with a new value once all nodes containing the current duplicate value have been deleted
            if curr.next and curr.next.val == curr.val:
                target = curr.val
            
            # in the future we just need to check if this node's value matches target because if it does we can just delete it
            if curr.val == target:
                next_node = curr.next # temporarily store this so that we can maintain list integrity and not lose track
                # if we're deleting the head node, just make the new head point to the next node
                if not prev:
                    head = next_node
                # if prev points to a valid node then we just update its next pointer to point to this next one
                else:
                    prev.next = next_node
                curr = next_node
            # if there's no match we can simply update prev and advance curr since we don't need to delete this node
            else:
                prev = curr
                curr = curr.next
                
        return head

class TestRemoveDuplicatesII(unittest.TestCase):
    sol = Solution()

    def test_one(self):
        head = array_to_ll([1,2,3,3,4,4,5])
        modified = self.sol.deleteDuplicates(head)
        self.assertEqual(ll_to_array(modified), [1,2,5])

    def test_two(self):
        head = array_to_ll([1,1,1,2,3])
        modified = self.sol.deleteDuplicates(head)
        self.assertEqual(ll_to_array(modified), [2,3])

if __name__ == "__main__":
    unittest.main()