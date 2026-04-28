# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        stack = [[root, 1]]
        maxd = 0
        while stack:
            node, d = stack.pop()
            if node:
                maxd = max(maxd, d)
                stack.append([node.left, d + 1])
                stack.append([node.right, d + 1])
        return maxd

