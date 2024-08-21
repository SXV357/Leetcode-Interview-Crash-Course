# 236

from utils import TreeNode

def lowestCommonAncestor(root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
    """
    Time complexity: O(n) because we're visiting every single node in the tree
    Space complexity: O(n) because of space taken up by the recursive call stack
    """
    # straightforward base case where the current node is NULL and there can be no LCA's with such a node
    if not root:
        return None
    
    # one key thing to realize is that if we ever reach a node that either equals p or q, then we can simply return that node because there's no point in continuing to search below that(we want the lowest common ancestor that has p and q as its descendants)
        # another thing to think about is that if both p and q are in the same subtree and we find p first then returning p is all that's needed because we anyways won't find q in the other subtree meaning that q would've been some descendant of p itself
    if root == p or root == q:
        return root
    
    # if the current node isn't p or q, we traverse down the left and right subtrees to check if we can find either of those nodes somewhere down the line
    left = lowestCommonAncestor(root.left, p, q)
    right = lowestCommonAncestor(root.right, p, q)

    # this is another case where at a given parent node, we have returned two non-null nodes for the left and right nodes respectively. this basically means that this node is the lowest common ancestor for p and q
        # case 1: p is in the left subtree and q is in the right subtree so the root is the only node that can be the LCA(in this case we'd be returning p to the left node of the root and q to the right node of the root)
        # case 2: p and q are in the same subtree but one isn't a child of the other and they both have an LCA within that subtree below the root
    if left and right:
        return root
    
    # we could also have cases where we return a non-null node and a null node but we don't care about the null node because the node returned is the one we're interested in(it is either the actual LCA or it is either p or q)
    return left if left else right

p, q = TreeNode(5), TreeNode(1)

p.left = TreeNode(6)
p.right = TreeNode(2, TreeNode(7), TreeNode(4))

q.left = TreeNode(0)
q.right = TreeNode(8)

root = TreeNode(3, p, q)

print(lowestCommonAncestor(root, p, q).val)