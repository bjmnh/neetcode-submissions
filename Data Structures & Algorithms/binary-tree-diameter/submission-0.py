# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        d, l = self.findLR(root)
        return max(d, l) - 1

    def findLR(self, root) -> List[int]:
        if not root:
            return [0,0]
        ll, lt = self.findLR(root.left)
        rl, rt = self.findLR(root.right)

        return [max(ll, rl) + 1, max(ll + rl + 1, lt, rt)]