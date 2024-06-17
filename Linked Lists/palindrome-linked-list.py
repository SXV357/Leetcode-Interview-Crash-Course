# 234

from typing import Optional
from utils import *
import copy

def array_solution(head: Optional[ListNode]) -> bool:
    # Adds all values in the linked list to an array then uses a standard 2-pointer approach to check if the list is a palindrome or not
    res = []

    while head:
        res.append(head.val)
        head = head.next
    
    l, r = 0, len(res) - 1
    while l < r:
        if res[l] != res[r]:
            return False
        l += 1
        r -= 1
    
    return True

def copy_solution(head: Optional[ListNode]) -> bool:
    # Original solution
        # reverses the list and compares the reversed list with the original one to check for similarity
        # since reversal changes the original head we create a deep copy of the list and store it beforehand so that once we're done with the reversal there's no problem in checking the contents of both the lists
        # inefficient since we're making a copy of the entire list where every single object within the list needs to be inserted into the new one in a recursive manner
    orig = copy.deepcopy(head)

    curr, prev = head, None
    while curr:
        next_node = curr.next
        curr.next = prev
        prev = curr
        curr = next_node
        
    temp = prev
    while temp:
        if temp.val != orig.val:
            return False
        temp = temp.next
        orig = orig.next
        
    return True

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        """
        COME BACK TO THIS TO RE-ATTEMPT
        Time complexity: O(n + n/2 + n/2) -> O(2n) -> O(n)
        - Finding middle node in the worst case takes O(n) time
        - Reversal is only for second half so O(n/2) time
        - Once again palindrome checking is happening against validity of reversed list so O(n/2) time
        Space complexity: O(1) because the only variables we're using are pointers which take up constant space
        """
        # if there's just node in the list it is already a palindrome so return true
        if not head.next:
            return True
        
        # Main idea:
            # if we reverse the second half of the list and compare it with the first half we can determine if the list as a whole is a palindrome or not
            # ex: 1->2->3->3->2->1
            # if we reverse the second half we get 1->2->3 and both halves are now the same so we can say its a palindrome
        
        # Algorithm
            # Find the middle node since this is the head of the second half of the linked list
            # Reverse the list starting from the middle node
            # Compare both the halves of the list

        # use fast and slow pointer to find the middle node
        slow = fast = head
        prev = None # this represents the node just before the middle node and we use it to connect both halves of the list once the reversal has taken place
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next

        # slow now points to the middle node in the list and we can now reverse the list with this node as the head as normal     
        curr, modified_prev = slow, None
        while curr:
            next_node = curr.next
            curr.next = modified_prev
            modified_prev = curr
            curr = next_node
        
        # the list has been reversed and we now connect the first and second halves together using this statement
        # THIS IS NECESSARY BECAUSE WE NEED IT FOR CASES WHEN WE'RE DEALING WITH AN ODD-LENGTH PALINDROME LINKED LIST
        prev.next = modified_prev

        # compare corresponding nodes in both halves of the list to determine if the list is a palindrome or not
        # initialize two pointers to start at the head of both halves of the list
        head_temp, prev_temp = head, modified_prev
        # we only loop as long as the head of the second half is valid because we only want to compare corresponding nodes starting with this one
        while prev_temp:
            # this condition is needed to handle odd-length palindrome linked lists
            # take a situation where the list is 1->0->1
            # when we reverse the second half the list becomes 1->1->0
            # when we loop the first time 1 == 1 so update the pointers to be 1 and 0 but 1 and 0 aren't equal so with the original approach we would've returned false but the thing is that the current node in the first list half is at the head of the reversed list meaning it must be a palindrome so the moment we detect that we break out and return true
            if head_temp == modified_prev:
                break
            # standard palindrome checking logic where if the values don't align we return false
            if head_temp.val != prev_temp.val:
                return False
            head_temp = head_temp.next
            prev_temp = prev_temp.next
        
        return True

sol = Solution()
head = array_to_ll([1,0,1])
print(sol.isPalindrome(head))