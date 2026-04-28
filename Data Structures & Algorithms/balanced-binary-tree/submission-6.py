# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        stack = [root]
        heights = {}
        while root and stack:
            
            if root.left and root.left not in heights:
                stack.append(root)
                root = root.left
            elif root.right and root.right not in heights:
                stack.append(root)
                root = root.right

            else:
                stack.pop()
                if abs(heights.get(root.right, 0) - heights.get(root.left, 0)) > 1:
                    return False
                heights[root] = max(heights.get(root.right,0), heights.get(root.left, 0)) + 1
                
                root = stack[-1] if stack else None
        return True

