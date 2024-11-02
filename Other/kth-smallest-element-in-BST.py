class Node():
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right=right

def insert(root, val):
    res = Node(val)
    if not root:
        return res
    else:
        temp = root
        while temp:
            if val < temp.val:
                if not temp.left:
                    temp.left = res
                    break
                else:
                    temp = temp.left
            else:
                if not temp.right:
                    temp.right = res
                    break
                else:
                    temp = temp.right

        return root
    
def inorder(root):
    if not root:
        return
    
    inorder(root.left)
    print(root.val)
    inorder(root.right)

vals = [10, 5, 4, 7, 12, 11, 14]
root = None
for val in vals:
    root = insert(root, val)

def kth_smallest(root, k):
    count = 1

    def dfs(root):
        nonlocal count
        if not root:
            return
        
        left = dfs(root.left)
        if left:
            return left

        if count == k:
            return (root, root.val)
        count += 1

        return dfs(root.right)
    
    return dfs(root)

target = kth_smallest(root, 3)
print(f"1st smallest element: {target}")