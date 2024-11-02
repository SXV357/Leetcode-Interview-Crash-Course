from collections import defaultdict
import copy

G = {0: [2, 3], 1: [0], 2: [1], 3: [4], 4: [0]}
t = defaultdict(lambda: [])

def transpose(G, transpose):
    """
    O(V + E) - Cannot do it more efficiently than this
    """
    for node, edges in G.items(): # O(V)
        for edge in edges: # O(E)
            transpose[edge].append(node) # O(1)

def square(G: dict):
    """
    Overall time complexity
        O((2V + E) + O(V * len(graph[edgeNode]) * len(remaining)))
    """
    final = copy.deepcopy(G) # O(V + E)
    vertices = list(G.keys()) # O(V)
    
    for vertex in vertices: # O(V)
        edges = G[vertex] # O(1)
        remaining = (set(vertices) - set(edges)) - {vertex} # O(1) for set operations
        for edgeNode in edges: # O(len(graph[edgeNode]))
            for dest in remaining: # O(len(remaining))
                if dest in G[edgeNode]: # O(1)
                    final[vertex].append(dest) # O(1)
    
    return final

def universal_sink(G: list[list[int]], v: int) -> bool:
    if not 1 <= v <= len(G):
        return False
    
    n = len(G)
    inDeg, outDeg = 0, False

    # check if out degree is 0
    if any (val == 1 for val in G[v - 1]):
        outDeg = False
    
    # check if in-degree is |V| - 1
    for i in range(1, n + 1):
        if G[i - 1][v - 1] == 1:
            inDeg += 1

    return ((inDeg == n - 1) and outDeg)

matrix = [[0, 1, 0, 0, 0, 0, 0], 
          [1, 0, 1, 1, 0, 0, 0], 
          [0, 1, 0, 0, 0, 0, 0], 
          [0, 1, 0, 0, 1, 1, 0], 
          [0, 0, 0, 1, 0, 0, 0], 
          [0, 0, 0, 1, 0, 0, 1], 
          [0, 0, 0, 0, 0, 1, 0]]

print(universal_sink(matrix, 1))