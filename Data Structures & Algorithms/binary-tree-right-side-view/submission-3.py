# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        
        def dfs(root, h):
            if not root:
                return None
            if h == len(res):
                res.append([])
            res[h] = root.val
            dfs(root.left, h + 1)
            dfs(root.right, h + 1)
        dfs(root, 0)
        return res