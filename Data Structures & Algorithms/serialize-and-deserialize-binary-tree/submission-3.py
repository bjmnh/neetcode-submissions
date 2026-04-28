# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        
        serialize = []

        def dfs(root):
            if root:
                serialize.append(str(root.val))
                dfs(root.left)
                dfs(root.right)
            else:
                serialize.append("N")
            
        dfs(root)
        return ",".join(serialize)


        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        if not data:
            return None
        treelist = data.split(",")
        treeidx = 0
        def dfs():
            nonlocal treeidx
            if treelist[treeidx] == "N":
                treeidx += 1
                return None

            node = TreeNode(treelist[treeidx])
            treeidx += 1
            node.left = dfs()
            node.right = dfs()
            return node
      
        return dfs()
