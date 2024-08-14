# 112

from utils import TreeNode
from typing import Optional

def pathSumRecur(root: Optional[TreeNode], targetSum: int) -> bool:
    """
    Pre-order recursive DFS traversal
    """
    def dfs(node, curr):
        # base case: if the root is null then no path sum can exist so we return false
        if not node:
            return False
        
        # we only care about whether the path sum equals the target sum at a leaf node so if the node is a leaf node check whether the sum of all the nodes prior to this node and this node's value equals the target value
        if not node.left and not node.right:
            return curr + node.val == targetSum
        
        # this is accumulating the value of the previous node before moving onto the left and right subtrees respectively
        curr += node.val

        # reason why we use "or" is because we want just one path in the overall tree starting at the root and ending at a leaf node with the target path sum and it doesn't matter whether it is in the left subtree or the right subtree because as long as it holds true in either one we return true
        return dfs(node.left, curr) or dfs(node.right, curr)
    
    # call the helper function starting at the root with an initial value of 0 since the sum of all nodes prior to the root is 0(it has no parents)
    return dfs(root, 0)

def hasPathSum(root: Optional[TreeNode], targetSum: int) -> bool:
    """
    Time complexity: O(n) because every node is visited
    Space complexity: O(n) because every single node 
    """
    # if the root is null then there's no path sum at all so return false
    if not root:
        return False
    
    # each element in the stack will consist of the node(object) and the path sum starting at the root and until this node
        # we start with the root because we are finding a path sum from the root till a leaf node
    stack = [(root, root.val)]

    # iterative preorder DFS approach using a stack (N -> L -> R)
    while stack:
        node, val = stack.pop()
        # as we're going down the tree, and based on the parent node popped, we add the parent node's value to this child's value as a way of incrementing the sum and do it for both the left and right child
        if node.left:
            stack.append((node.left, node.left.val + val))
        if node.right:
            stack.append((node.right, node.right.val + val))
        
        # we only care if we are at a leaf node and the sum as of considering this node equals targetSum
        if not node.left and not node.right and val == targetSum:
            return True
    
    return False

root1 = TreeNode(5, TreeNode(4, TreeNode(11, TreeNode(7), TreeNode(2)), None), TreeNode(8, TreeNode(13), TreeNode(4, None, TreeNode(1))))
root2 = TreeNode(1, TreeNode(2), TreeNode(3))

assert(hasPathSum(root1, 22) == pathSumRecur(root1, 22))
assert(hasPathSum(root2, 5) == pathSumRecur(root2, 5))
assert(hasPathSum(None, 0) == pathSumRecur(None, 0))
print("all assertions passed successfully")