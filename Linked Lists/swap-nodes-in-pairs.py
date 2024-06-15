# 24

from typing import Optional
from utils import *

class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Time complexity: O(n) but technically O(n // 2) since we traverse the list those many times at worst and also swap pairs those many number of times but ignoring constants the algorithm runs in linear time
        Space complexity: O(1) because we're only storing pointers
        """
        # if the list is empty to begin with we have nothing to swap so we return null right away
        if not head:
            return None
        
        # again if there's only one node in the list then there's no adjacent node to swap it with so we just return the list as is
        if head.next is None:
            return head
        
        # curr will keep track of the current node that we need to swap with its adjacent node
        # prev is used because as we're swapping nodes except for the first pair we need to update this extra pointer as well
        curr, prev = head, None
        while curr:
            # this first condition is to deal with lists that are off an odd length
                # a max of only n // 2 pair swaps will happen and then we will end up at a lone node after which there's no more pairs to swap
                # since we are keeping track of the current node's next node and its next node once we reach the lone node, its next is NULL and accessing its next's next will lead to a null pointer exception so we break out right away because we don't need to swap this and can keep it as is
            if not curr.next:
                break
            # next_pair is the next node that we will be moving on to once we swap the current pair because we swap the current node and its adjacent one and then move on to the adjacent node's next node to continue the swapping
            # we also store next_node for swapping purposes because we need to update its next pointer to point to the node prior to it
            next_pair = curr.next.next
            next_node = curr.next
            # as of this point we know there are atleast 2 nodes in the list and this is the first time when we're swapping pairs so the previous node will be NULL. we need to check for this condition because the head of the list will change

            # ex list: 1->2->3->4

            if not prev:
                # curr = 1, curr.next = 2, curr.next.next = 3, prev = NULL
                # we need to make 1 point to curr.next.next, 2 point to curr and head point to curr.next including prev to point to 1 because when we swap 3 with 4 we need to update what 1 also points to
                curr.next = next_pair # 1.next = 3
                next_node.next = curr # 2.next = 1
                head = next_node # head = 2
                prev = curr # prev = 1
            
            # at this point we have a reference to the current node's previous node so we need to handle this case as well
            else:
                # curr = 3, curr.next = 4, curr.next.next = NULL, prev = 1
                # we need to make 1 point to 4, 4 point to 3 and 3 point to NULL
                prev.next = next_node # 1.next = 4
                next_node.next = curr # 4.next = 3
                curr.next = next_pair # 3.next = NULL
                prev = curr # prev = 3

            curr = next_pair # we move on to the next pair to be swapped
        
        return head
        
one = ListNode(1)
two = ListNode(2)
three = ListNode(3)
four = ListNode(4)
five = ListNode(5)

one.next = two
two.next = three
three.next = four
four.next = five
head = one

print(f"Before swapping:")
traverse(head)

print(f"After swapping:")
sol = Solution()
modified = sol.swapPairs(head)
traverse(modified)