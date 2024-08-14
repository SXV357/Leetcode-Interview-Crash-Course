# 1448  

from utils import TreeNode

def goodNodes(root: TreeNode) -> int:
    res = 0 # keep track of the number of good nodes
    def dfs(node: TreeNode, prev_max: int) -> None:
        nonlocal res # res isn't local to this function so we need to specify this keyword to make it work

        # we are simply accumulating the number of good nodes in this function and not returning anything but a base case is needed once we hit null nodes at the bottom of the tree so we simply return 
        if not node:
            return
        
        # the idea is that this current node's value needs to be the greatest of all the previous node's values so if that is true we can update the value of prev_max which stores the previous maximum value and we can update the count since this node would constitute as a good node
        if node.val >= prev_max:
            prev_max = max(prev_max, node.val)
            res += 1
        
        # once we've updated the answer, we call dfs on both the left and right child with the current max passed in. the key is that we want to always maintain the current maximum along with each node
        dfs(node.left, prev_max)
        dfs(node.right, prev_max)

    # call the helper function starting at the root and the starting maximum being the root's value and then return the answer since that was updated inside the helper function
    dfs(root, root.val)
    return res

root1 = TreeNode(3, TreeNode(1, TreeNode(3)), TreeNode(4, TreeNode(1), TreeNode(5)))
root2 = TreeNode(3, TreeNode(3, TreeNode(4), TreeNode(2)))
root3 = TreeNode(1)

print(goodNodes(root1))
print(goodNodes(root2))
print(goodNodes(root3))