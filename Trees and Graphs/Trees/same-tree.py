#100

from utils import TreeNode
from typing import Optional

def isSameTree(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
    # if the nodes are both NULL then they're equal so we can return True
    if not p and not q:
        return True
    
    # here both the nodes aren't NULL but either
        # 1. one of them is and the other isn't - automatically return false because there's no way the trees can be the same
        # 2. both are valid but the values aren't the same(the values need to match consistently so we return false)
    if not p or not q or p.val != q.val:
        return False

    # we call the function recursively on both the left and right subtrees to determine whether the structures and node values are the same for all subsequent nodes and then we "and" the two values because we want them both to be true in order for the trees to be the same
    left = isSameTree(p.left, q.left)
    right = isSameTree(p.right, q.right)
    return left and right

p = TreeNode(1, TreeNode(2), TreeNode(1))
q = TreeNode(1, TreeNode(1), TreeNode(2))

print(isSameTree(p, q))