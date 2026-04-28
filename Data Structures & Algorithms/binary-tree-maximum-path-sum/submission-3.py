# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        maxseen = float('-inf')
        def mps(root):
            nonlocal maxseen
            left = mps(root.left) if root.left else float('-inf')
            right = mps(root.right) if root.right else float('-inf')
            maxseen = max(maxseen, left + root.val, right + root.val, root.val, left + right + root.val)
            return max(max(left, right) + root.val, root.val)

        mps(root)
        return maxseen