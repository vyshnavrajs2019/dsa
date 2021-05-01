"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        
        visited = {}
        
        def helper(node):
            nonlocal visited
            
            if not node:
                return None
            
            if node.val in visited:
                return visited[node.val]
            
            # create a copy of the node
            cloned_node = Node(node.val)
            
            # store in cache
            visited[node.val] = cloned_node
            
            # clone neighbors
            for neighbor in node.neighbors:
                cloned_node.neighbors.append(helper(neighbor))
            
            return cloned_node
        
        return helper(node)
