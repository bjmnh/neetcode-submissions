# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def dfs(root):
            if not root:
                return 0
            a = dfs(root.right)
            b = dfs(root.left)
            if a == -1 or b == -1 or abs(a - b) > 1:
                return -1
            return max(a, b) + 1

        if root and dfs(root) == -1:
            return False
        return True

        