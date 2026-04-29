"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
            
        # Map the original node to its clone immediately
        hm = {node: Node(node.val)}
        stack = [node]
        
        while stack:
            cnode = stack.pop()
            
            for n in cnode.neighbors:
                # If the neighbor hasn't been cloned yet
                if n not in hm:
                    hm[n] = Node(n.val)
                    stack.append(n) # Add to stack to process its neighbors later
                
                # Link the clone of cnode to the clone of n
                hm[cnode].neighbors.append(hm[n])
                
        return hm[node]