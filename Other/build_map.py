from collections import deque, defaultdict

class Node():
    def __init__(self, val=0, left=None, right=None):
        self.val=val
        self.left=left
        self.right=right

root = Node(0, Node(1, Node(3, Node(7), Node(8)), Node(4, Node(9), Node(10))), Node(2, Node(5, Node(11), Node(12)), Node(6, Node(13), Node(14))))
root2 = Node(0, None, Node(1, None, Node(2, None, Node(3, None, Node(4, None, Node(5))))))

def build_map(root: Node):
    if not root:
        return {}
    
    res = defaultdict(lambda: [])

    q = deque([root])
    level = 0
    
    while q:
        curr = len(q)
        nodes = []

        for _ in range(curr):
            node = q.popleft()
            nodes.append(node)

            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        
        res[level] = nodes
        level += 1

    return res

def build_map_recur(root, level, N: dict):
    if not root:
        return

    if level not in N:
        N[level] = []
    
    N[level].append(root)  
    build_map_recur(root.left, level + 1, N)
    build_map_recur(root.right, level + 1, N)

res = {}
build_map_recur(root, 0, res)
for k in res:
    print(f"Level {k} nodes: {list(map(lambda x: x.val, res[k]))}")