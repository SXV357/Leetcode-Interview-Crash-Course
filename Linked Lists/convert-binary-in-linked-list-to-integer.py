# 1290

from utils import *
import unittest

class Solution:
    def naive_solution(self, head: ListNode) -> int:
        """
        Time complexity: O(n) because `n` iterations to add all values in the list to the array, `n` iterations to convert all values into a string, `n` iterations to cocatenate the values into a string and presumably `n` iterations to convert the string to an integer but overhead because of string concatenation
        Space complexity: O(n) because as the list grows in size the array also grows in size
        """
        # 46ms (Beats 7.29%)

        # Algorithm
            # add all values in the list to an array
            # convert every digit to a string in the array
            # join everything back together into a string and use the built-in int() function to do the conversion

        elems = []
        curr = head

        while curr:
            elems.append(curr.val)
            curr = curr.next
        
        elems = list(map(lambda elem: str(elem), elems))
        return int("".join(elems), 2)

    def stack_solution(self, head: ListNode) -> int:
        """
        Time complexity: O(n) because `n` iterations to update array with all values and `n` iterations to calculate decimal
        Space complexity: O(n) because as the list size grows larger the stack also grows larger
        """
        # 31ms (Beats 81.82%)

        # Algorithm
            # add all values from the list to an array
            # since we start from the lowest power of 2 and multiply each digit of the number with this starting with the rightmost digit, iterate while the stack is not empty, pop the last value, multiply it with the appropriate power of 2 and update the power to move on 

        stack = []
        tmp = head
        while tmp:
            stack.append(tmp.val)
            tmp = tmp.next
        
        curr = res = 0
        while stack:
            res += stack.pop() * pow(2, curr)
            curr += 1
        
        return res
    
    def reversal_solution(self, head: ListNode) -> int:
        """
        Time complexity: O(n) because we iterate over the list `n` times to reverse it and another `n` times to calculate the decimal value
        Space complexity: O(1) because we're not using any other variables apart from pointers
        """
        # 29ms (Beats 90.56%)

        # Algorithm:
            # reverse the list
            # iterate from the new head of the list and calculate the base 2 equivalent of the binary number using powers of 2 going up in number until the end of the list is reached

        curr, prev = head, None
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        
        start = res = 0
        while prev:
            res += (prev.val * pow(2, start))
            prev = prev.next
            start += 1
        
        return res

    def getDecimalValue(self, head: ListNode) -> int:
        """
        Time complexity: O(n) because `n` iterations to count number of nodes and `n` iterations to calculate the decimal value
        Space complexity: O(1) because in addition to variables that just store integers the only other ones being used are pointers
        """
        # 34ms (Beats 66.48%)

        # Algorithm:
            # count the number of nodes in the list
            # traverse the list once again starting from the head and calculate the base 2 equivalent of the binary number using powers of two starting from one less than the total number of nodes

        num_nodes = 0
        temp = head

        while temp:
            num_nodes += 1
            temp = temp.next
        
        max_deg = num_nodes - 1
        curr, res = head, 0

        while curr:
            res += (curr.val * pow(2, max_deg))
            curr = curr.next
            max_deg -= 1
        
        return res

class TestBinaryConversion(unittest.TestCase):
    sol = Solution()

    def test_one(self):
        head = array_to_ll([1,0,1])
        traverse(head)
        naive, stack, reverse, orig = self.sol.naive_solution(head), self.sol.stack_solution(head), self.sol.reversal_solution(head), self.sol.getDecimalValue(head)
        self.assertListEqual([naive, stack, reverse, orig], [5, 5, 5, 5])

    def test_two(self):
        head = array_to_ll([0])
        naive, stack, reverse, orig = self.sol.naive_solution(head), self.sol.stack_solution(head), self.sol.reversal_solution(head), self.sol.getDecimalValue(head)
        self.assertListEqual([naive, stack, reverse, orig], [0, 0, 0, 0])

if __name__ == "__main__":
    unittest.main()