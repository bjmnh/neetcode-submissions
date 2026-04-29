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
        seen = set()
        hm = {}
        stack = [node]
        while stack:
            cnode = stack.pop()
            if cnode not in hm:        
                hm[cnode] = Node(cnode.val)
            seen.add(cnode)
            if cnode.neighbors:
                for n in cnode.neighbors:
                    if n not in hm:
                        hm[n] = Node(n.val)
                    if n not in seen:
                        stack.append(n)
                        seen.add(n)
                    hm[cnode].neighbors.append(hm[n])
        return hm[node]
            
            

        