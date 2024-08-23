# 111

from utils import TreeNode
from typing import Optional

def minDepth(root: Optional[TreeNode]) -> int:
    """
    Time complexity: O(n)
    Space complexity: O(n)
    """
    # simple case - if the root is null we return 0
    if not root:
        return 0
    
    # traverse down to the left and right subtrees respectively to calculate depth
    left = minDepth(root.left)
    right = minDepth(root.right)
    
    # case 1: for a given node, there is some depth on the left side and some depth on the right side and we want the minimum depth including the root node which is why we take the minimum of the two depths and add a 1
    if left and right:
        return min(left, right) + 1

    # it may also be possible that the depth on the left subtree or right subtree may be 0 entirely so in that case we want to account for that non-zero depth and the root node since taking the minimum again would just give a depth of 1: min(0, non-zero) + 1 === 1 
    return left + 1 if left else right + 1

root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
root2 = TreeNode(2, None, TreeNode(3, None, TreeNode(4, None, TreeNode(5, None, TreeNode(6)))))

print(minDepth(root))
print(minDepth(root2))