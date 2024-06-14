from typing import Optional
class ListNode():
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# FAST AND SLOW POINTER TECHNIQUE
    # THE FAST POINTER MOVES 2 NODES AT A TIME AND THE SLOW POINTER MOVES ONLY ONE NODE AT A TIME
    # WE NEED TO CHECK FOR THE VALIDITY OF FAST.NEXT BECAUSE IF FAST IS THE TAIL NODE OF THE LIST(IT IS THE ONLY ONE THEN FAST.NEXT IS NULL AND ACCESSING NULL.NEXT WOULD RESULT IN A NULL-POINTER EXCEPTION)

# head is the head node of a linked list

# function fn(head):
#     slow = head
#     fast = head

#     while fast and fast.next:
#         Do something here
#         slow = slow.next
#         fast = fast.next.next

def return_middle(head: ListNode) -> int:
    """
    Given the head of a linked list with an odd number of nodes head, return the value of the node in the middle.
    Time complexity: O(n) for `n` nodes in the linked list because in the worst case we end up traversing thru every single node before we return the middle one
    Space complexity: O(1) because the pointers aren't dependent on list size and take up constant space
    """
    
    def non_optimal(head: ListNode):
        # without using the fast-slow pointer approach
            # traverse list once counting number of nodes
            # traverse again maintaining counter of how many nodes visited and return the appropriate middle node
        num_nodes = 0
        temp = head
        while temp:
            num_nodes += 1
            temp = temp.next
        
        mid, curr, idx = num_nodes // 2, head, 0

        while curr:
            if idx == mid:
                return curr.val
            idx += 1
            curr = curr.next
    
    # optimal solution that uses the fast-slow pointer approach

    # key here is to realize that if we have an odd number of nodes then at the time of the while loop termination the slow pointer will have the value of the middle node
        # let's say the list is 1 -> 2 -> 3 -> 4 -> 5
        # both fast and slow start at the head
        # on the first iteration fast advances to 3 and slow advances to 2
        # on the second iteration slow advances to 3 and fast advances to 5
        # on the third iteration fast.next is NULL so we break out and return slow.val
        # at this point slow points to 3 which is precisely the middle node 
    
    slow = fast = head # both pointers initially start at the head but will move at different paces thru the list
    # the current fast pointer needs to be valid since we're accessing fast.next and fast.next needs to be valid since we're accessing fast.next.next
    while fast and fast.next:
        slow = slow.next # just moves thru the list one node at a time
        fast = fast.next.next # moves thru the list 2 nodes at a time because fast.next is the first node skipped and it then moves onto the next of the next one

    return slow.val # since slow moves 1/2 as fast as the quick pointer it would be at the middle of the list by the time fast reaches the end

def hasCycle(head: Optional[ListNode]) -> bool:
    """
    Come back to this again to re-attempt
    """
    # O(1) space and O(n) solution using fast and slow pointers - Optimal in terms of runtime and space

    # Main idea:
        # if there's no cycle, tail.next is NULL and the loop terminates with tail not looping back to an already existing node meaning we can return false right away
        # if there is a cycle then there is some node that tail connects to which we have already visited and there's a neat trick to detect this
            # MAIN THING TO NOTE IS THAT WE CANNOT DO THE CHECK OF THE TWO POINTERS EQUALLING ONE ANOTHER AT THE START BECAUSE BOTH START AT THE HEAD AND IT WILL ALWAYS RETURN TRUE IRRESPECTIVE OF WHETHER THERE'S A CYCLE OR NOT SO WE NEED TO MOVE BOTH THE POINTERS FORWARD AND ONLY THEN DO THE COMPARISON
            # the slow pointer is always moving half as fast as the fast pointer so after the fast pointer loops around once there are 2 possible scenarios: it is one position behind the slow pointer or it is two positions behind the slow pointer
            # if the fast pointer is one position behind the slow pointer then on the next iteration both pointers will meet at the same address and if the fast pointer is two positions behind it is one position behind on the next iteration and the next time they meet again
            # we return true if they meet at the same location because this is happening some time after one traversal of the list is complete after both pointers start at the head

    slow = fast = head
    # if we reach the tail and fast.next is null we break out and return false because the list has a termination point and there is no cycle at all
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        # since the list can have duplicates we compare the references for purposes of accuracy otherwise we may get false positives
        if slow == fast:
            return True
    
    return False

    # O(n) space and O(n) solution using a set - Optimal but not in terms of space
        # if there is a cycle then after looping back from the tail we encounter a node that we have already visited before so we use a set to keep a track of that
        # one thing to keep in mind is that instead of storing the node's value we store its address because several nodes could store the same value but they all have unique addresses which is how we know whether or not a cycle exists in the list
        # downside is that it is not space-efficient because in the worst case all n nodes are added to it and the list terminates and we return false

    # seen = set()
    # temp = head
    # while temp:
    #     if temp in seen:
    #         return True
    #     seen.add(temp)
    #     temp = temp.next
    
    # return False

def kth_node(head: ListNode, k: int) -> ListNode:
    """
    COME BACK TO THIS AGAIN TO RE-ATTEMPT
    Given the head of a linked list and an integer k, return the k^th node from the end
    Time complexity: O(n) because if k = 1 then we iterate through every single node in the list before we return
    Space complexity: O(1) because the only variables we're dealing with are the pointers which don't depend on input size
    """

    # Count number of nodes in the list then move forward the list again and return the appropriate node

    # num_nodes = 0
    # temp = head
    # while temp:
    #     num_nodes += 1
    #     temp = temp.next
    
    # curr = head
    # for _ in range(num_nodes - k):
    #     curr = curr.next
    
    # return curr

    # fast and slow pointer solution

    # main idea:
        # what we can do is to separate the pointers at a distance of k to begin with and move them thru the list one node at a time, specifically the fast pointer
        # by the time the fast pointer which is always a distance of k away from the slow pointer reaches the end of the list and goes past, the slow pointer will point to the correct node since it was always at the same distance away from the fast pointer which is now at the end of the list
        # ex: 1 -> 2 -> 3 -> 4 -> 5 with k = 3
        # slow starts at 1 and fast starts at 4
        # move slow to 2 and fast to 5
        # now move slow to 3 and fast is NULL and now slow is at a distance of 3 away from the end of the list so we return it

    slow = fast = head

    # moving fast so that it starts at a distance of k from slow
    for _ in range(k):
        fast = fast.next
    
    # moving both pointers one step at a time thru the list until fast reaches the end because as of this point slow will be at a distance of k from where fast currently is
    while slow and fast:
        slow = slow.next
        fast = fast.next
    
    return slow