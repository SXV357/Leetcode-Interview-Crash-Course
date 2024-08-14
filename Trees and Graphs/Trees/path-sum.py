# 112

from utils import TreeNode
from typing import Optional

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

print(hasPathSum(root1, 22))
print(hasPathSum(root2, 5))
print(hasPathSum(None, 0))