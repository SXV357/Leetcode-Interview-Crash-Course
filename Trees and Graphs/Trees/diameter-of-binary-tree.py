# 543

from typing import Optional
from utils import TreeNode

def diameterOfBinaryTree(root: Optional[TreeNode]) -> int:
    """
    Time complexity: O(n)
    Space complexity: O(n) - recursion stack
    """
    diam = 0

    def dfs(root):
        # the idea behind this function is that we will be using the return values from both subtrees to calculate the diamater of the current node
            # these return values will be the height of the left and right subtrees respectively

        nonlocal diam
        # base case: if the current node is NULL, it doesnt have a height so return 0
        if not root:
            return 0
        
        # recursive calls to both the left and right subtrees respectively to get their height
        left = dfs(root.left)
        right = dfs(root.right)

        # we will be using this global variable which is what actually stores the largest diameter which is basically the sum of the heights of both subtrees
        diam = max(diam, left + right)

        # usual logic for calculating height(+ 1 because we need to account for the current node as well)
        return max(left, right) + 1

    dfs(root)
    return diam

root = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3))
print(diameterOfBinaryTree(root))