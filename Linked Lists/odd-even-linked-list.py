# 328

from utils import *
from typing import Optional

class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Time complexity: O(n) because we're iterating through the list only once while performing all the pointer updates
        Space complexity: O(1) because we're only using pointers for variables
        """
        # if the list is empty or there's just one node or there's just 2 nodes there's nothing to group so we just return the list as is
        if (not head) or (not head.next) or (not head.next.next):
            return head
        
        # the idea is that we group all the odd indices and group all the even indices then connect the tail of the odd indices list to the head of the even indices list

        # we initialize the following pointers
            # odd_head = starts at the original head of the list because this is the first node to have an odd_index
            # odd_prev = the pointer that is used to form the list of all nodes with odd indices and used to connect both the lists together at the end
            # even_head = starts at one node after the head because the second node of the list has an even index
            # even_prev = used to form the list of all nodes with even indices and used to terminate the modified list since all even index nodes come at the end
        odd_head = odd_prev = head
        even_head = even_prev = head.next
        # the connection will be done in an alternate manner where we connect two odd index nodes then two even index nodes and so on and this variable will be used to determine that
        idx = 1

        # fast will serve as the node to which the current node that either connects to odd_prev or even_prev
        fast = even_head.next
        while fast:
            # first pair of nodes to be connected which are the odd index nodes
            if idx % 2 != 0:
                # odd_prev points to the current odd index node and fast points to the node that odd_prev connects to
                odd_prev.next = fast
                # once we've connected the two update odd_prev to point to fast so that we can connect the next set of odd nodes
                odd_prev = fast
            else:
                # same logic as above where we need to update the next pointer of even_prev to point to fast and then update even_prev itself
                even_prev.next = fast
                even_prev = fast
            # alternate pointer updates using this variable
            idx += 1
            fast = fast.next
        
        # at the end once all odd nodes have been connected and all even nodes have been connected we need to link them together

        # even_prev will now point to the last even_node in the list and its next should be set to null since it comes at the end of the list
        even_prev.next = None
        # now connect tail of odd node list to the head of the even node list
        odd_prev.next = even_head

        return odd_head


sol = Solution()
head = array_to_ll([1,2,3,4,5])
traverse(sol.oddEvenList(head))