# 2130

# from typing import Optional
# from collections import defaultdict
import unittest
from utils import *

class Solution:
    def pairSum(self, head: ListNode) -> int:
        """
        Time complexity: O(n) because all the individual operations run in linear time
        Space complexity: O(1) for just pointers and the result variable
        """
        # trivial hashmap solution(can technically be solved with an array as well but not ideal)
            # the since we determine pairs based on indices and all indices are guaranteed to be unique, we can create a dictionary where we map each value's index to itself
            # now since all values in the first half of the list are twins of one's in the second half we can simply iterate over the first half of the list, index into the dictionary to obtain the values and then update the maximum pair sum

        # mappings = defaultdict(int)
        # temp, idx = head, 0
        # while temp:
        #     mappings[idx] = temp.val
        #     idx += 1
        #     temp = temp.next
        
        # indices = list(mappings.keys())
        # n, res = len(indices), 0
        # for i in range(n // 2):
        #     res = max(res, mappings[indices[i]] + mappings[indices[n - 1 - i]])
        
        # return res

        # Key thing to note:
            # let's take the list 1->2->3->4->5->6
            # the pairs are (1, 6); (2, 5); (3, 4)
            # we're not working with a doubly linked list so we don't have flexibility but something to note is that we can use 2 pointers to achieve this(not directly though because we need to modify the list a bit before we can use it)
            # notice that if we reverse the second half of the list which starts from 4, we get the list 1->2->3->6->5->4 and now we can use fast and slow pointer positioned at a distance of n / 2 from each other, iterate over the list and update the maximum pair sum
            # we use a fast and slow pointer to first locate the list's middle node
            # we then reverse the second half and then use two pointers again to find the max pair sum 

        # use a fast and slow pointer to get reference to head of the second half of the list
        fast = slow = head
        prev = None # we need to maintain a reference to this because once we reverse the second half of the list we need to connect the first half and second half together and this pointer serves as that bridge
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next

        # at this point prev will hold reference to the node just before the middle node and it's the middle node from where we need to reverse the list until the very end
        curr = slow
        dummy_prev = None # this dummy_prev variable at the very end will point to the tail of the list and this will essentially be the new fast pointer that we can use in addition to another one from the start to find the max pair sum

        # standard reversal routine
        while curr:
            next_node = curr.next
            curr.next = dummy_prev
            dummy_prev = curr
            curr = next_node
        
        # the two halves of the list are disconnected so we now connect them

        # take the example from above
            # after the reversal we have 1->2->3 6->5->4
            # the below line makes the list this: 1->2->3->6->5->4
        prev.next = dummy_prev

        # dummy_prev is at the correct offset from the head so all we need is to initialize a slow pointer starting from the beginning and move them both thru the list one node at a time until dummy_prev becomes invalid
        # at that point we have calculated the twin pair sum of all possible pairs in the list and have also updated max
        new_slow = head
        
        res = 0
        while dummy_prev:
            res = max(res, new_slow.val + dummy_prev.val)
            new_slow = new_slow.next
            dummy_prev = dummy_prev.next
        
        return res

class TestPairSum(unittest.TestCase):
    sol = Solution()
    
    def test_one(self):
        five = ListNode(5)
        four = ListNode(4)
        two = ListNode(2)
        one = ListNode(1)

        five.next = four
        four.next = two
        two.next = one
        head = five

        self.assertEqual(self.sol.pairSum(head), 6)

    def test_two(self):
        four = ListNode(4)
        two_one = ListNode(2)
        two_two = ListNode(2)
        three = ListNode(3)

        four.next = two_one
        two_one.next = two_two
        two_two.next = three
        head = four

        self.assertEqual(self.sol.pairSum(head), 7)

    def test_three(self):
        one = ListNode(1)
        thousand = ListNode(100000)

        one.next = thousand
        head = one

        self.assertEqual(self.sol.pairSum(head), 100001)

if __name__ == "__main__":
    unittest.main()