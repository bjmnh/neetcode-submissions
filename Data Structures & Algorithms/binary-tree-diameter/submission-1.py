# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.gmax = 0
        self.dfs(root)
        return self.gmax

    def dfs(self, root) -> int:
        if not root:
            return 0
        left = self.dfs(root.left)
        right = self.dfs(root.right)
        self.gmax = max(self.gmax, left + right)
        return 1 + max(left, right)
        