# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def serialize(root):
            if not root:
                return "#$"
            return "#" + str(root.val) + serialize(root.left) + serialize(root.right)
            
        if serialize(subRoot) in serialize(root):
            return True
        return False