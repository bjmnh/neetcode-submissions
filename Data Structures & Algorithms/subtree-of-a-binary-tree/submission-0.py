# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        def isequal(root1, root2):
            stack = [(root1,root2)]
            while stack:
                r1,r2 = stack.pop()
                if not r1 and not r2:
                    continue
                if not r1 or not r2 or r1.val != r2.val:
                    return False
                stack.append((r1.left,r2.left))
                stack.append((r1.right,r2.right))
            return True

        stack = [root]
        while stack:
            r1 = stack.pop()
            if isequal(r1, subRoot):
                return True
            if r1:
                stack.append(r1.left)
                stack.append(r1.right)
        return False



