from utils import TreeNode

def construct() -> TreeNode:
    root = TreeNode(1)
    root.left = TreeNode(2, TreeNode(4), TreeNode(5))
    root.right = TreeNode(3, TreeNode(6), TreeNode(7))
    return root

# 3 types of DFS down below: pre-order, in-order, post-order
    # the base case is so that if we recurse to a null node, we stop exploring that one given side, backtrack to the root node and then explore the other side

def preorder(root: TreeNode) -> None:
    # pre-order traversal: NLR
        # standard traversal where the current node is explored first followed by its left subtree and its right subtree
        # starts at the top and works it way down to the bottom
        # LOGIC DONE BEFORE EXPLORING CHILDREN
    if not root:
        return

    print(root.val)
    preorder(root.left)
    preorder(root.right)

def inorder(root: TreeNode) -> None:
    # in-order traversal: LNR
        # explore left subtree completely, then the root node and then the right subtree
        # starts at the bottom of the left subtree and works it way back up then to the bottom of the right subtree then all the way back up before returning
        # LOGIC DONE BETWEEN EXPLORING CHILDREN
    if not root:
        return
    
    inorder(root.left)
    print(root.val)
    inorder(root.right)

def postorder(root: TreeNode) -> None:
    # post-order traversal: LRN
        # explore the left subtree and the right subtree then the root node at the very end
        # LOGIC DONE AFTER EXPLORING CHILDREN
    if not root:
        return
    
    postorder(root.left)
    postorder(root.right)
    print(root.val)