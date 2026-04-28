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
            if not root:
                return 0
            nonlocal maxseen
            left = max(mps(root.left), 0)
            right = max(mps(root.right), 0) 
            maxseen = max(maxseen, left + right + root.val)
            return max(left, right) + root.val

        mps(root)
        return maxseen