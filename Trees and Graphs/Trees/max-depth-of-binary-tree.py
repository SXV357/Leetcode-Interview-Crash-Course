# 104

from utils import TreeNode
from typing import Optional

def maxDepth(root: Optional[TreeNode]) -> int:
    if not root:
        return 0
    
    if root and not root.left and not root.right:
        return 1
    
    return max(maxDepth(root.left), maxDepth(root.right)) + 1

tree = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
print(maxDepth(tree))