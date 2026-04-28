# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = [root]
        visited = set()
        t = 1
        while stack:
            if root.left and root.left not in visited:
                stack.append(root.left)
                root = root.left
            elif not root.left or root.left in visited:
                stack.pop()
                if t == k:
                    return root.val
                t += 1
                visited.add(root)

                if root.right and root.right not in visited:
                    stack.append(root.right)
                    root = root.right
                else:
                    root = stack[-1]

                

            