# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        stack = [(p,q)]
        while stack:
            p, q = stack.pop()

            if (p and not q) or (not p and q) or (p and q and p.val != q.val):
                return False
            if not p and not q:
                continue

            stack.append((p.left, q.left))
            stack.append((p.right,q.right))

        return True