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
