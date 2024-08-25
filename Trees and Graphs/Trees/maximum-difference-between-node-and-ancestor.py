# 1026

from utils import TreeNode

def maxDiffRecursive(root: TreeNode) -> int:
    """
    Time complexity: O(n)
    Space complexity: O(n)
    """
    res = 0
    
    # the idea behind this problem is always keeping a track of the maximum and minimum value along the path from the root until the current node we're on
    def helper(root, curr_max, curr_min):
        nonlocal res

        if not root:
            return
        
        # at each node we're on, we have a record of the maximum node until this node and the minimum node until this one so we take the maximum of the previous value along with both of these since it could be possible that at some point, the 3rd value we're comparing may be larger than the other two
            # another thing to note is that curr_max and curr_min will always represent the ancestors of this current node because they're calculated prior to visiting this node
        res = max(res, abs(curr_max - root.val), abs(curr_min - root.val))

        # once we update the maximum difference, we update the current maximum and minimum with this node so that we have the updated values at the next node(s) we visit
        curr_max = max(curr_max, root.val)
        curr_min = min(curr_min, root.val)

        # traverse down the left and right subtrees respectively
        helper(root.left, curr_max, curr_min)
        helper(root.right, curr_max, curr_min)
    
    # the starting maximum and minimum is the root's value because it has no ancestors
    helper(root, root.val, root.val)
    return res

def maxAncestorDiff(root: TreeNode) -> int:
    """
    Time complexity: O(n^2)
    Space complexity: O(n)
    """
    # uses an iterative stack brute force approach to find the max difference
        # finds the ancestors for all nodes, stores them in an array and then loops over all ancestors and calculates the maximum of all differences between those ancestor(s) and the node which has those ancestors
    stack = [(root, [])]
    modified = []

    while stack:
        node, ancestors = stack.pop()

        new = ancestors.copy()
        new.append(node.val)

        if node.left:
            stack.append((node.left, new))
            modified.append((node.left, new))
        
        if node.right:
            stack.append((node.right, new))
            modified.append((node.right, new))
    
    res = 0
    for pair in modified:
        above = pair[1]
        for node in above:
            res = max(res, abs(node - pair[0].val))
    
    return res

root = TreeNode(8, TreeNode(3, TreeNode(1), TreeNode(6, TreeNode(4), TreeNode(7))), 
                   TreeNode(10, None, TreeNode(14, TreeNode(13))))

print(maxDiffRecursive(root))