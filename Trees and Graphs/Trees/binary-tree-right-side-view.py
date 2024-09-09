# 199

from utils import TreeNode
from typing import Optional, List
from collections import deque

def rightSideView(root: Optional[TreeNode]) -> List[int]:
    """
    Time complexity: O(n)
    Space complexity: O(n)
    """

    if not root:
        return []

    res = []
    res.append(root.val)

    # we begin BFS starting at the root
    q = deque([root])

    while q:
        # at this point, the queue will be holding all nodes of a specific level so by saving how many nodes there are we can then loop over only those many nodes and add their children to the queue
        num_nodes = len(q)

        # loop over all nodes in the current level
        for _ in range(num_nodes):
            # pop the node from the front of the queue and add its children to queue
            curr = q.popleft()

            if curr.left:
                q.append(curr.left)
            if curr.right:
                q.append(curr.right)
        
        # since we only want the nodes on the right side all we need to do is access the last element of the queue since for a given level the node in this position would be the rightmost node in the tree
        if q:
            res.append(q[-1].val)
    
    return res

# root = TreeNode(1, TreeNode(2, None, TreeNode(5)), TreeNode(3, None, TreeNode(4)))
root = None
print(rightSideView(root))