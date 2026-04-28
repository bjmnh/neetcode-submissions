# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        stack = [root]
        current = root
        seen = set()
        descendants = {}
        
        while stack:
            if current.left and current.left not in seen:
                stack.append(current.left)
                current = current.left

            elif current.right and current.right not in seen:
                stack.append(current.right)
                current = current.right

            else:
                stack.pop()
                seen.add(current)
                descendants[current] = descendants.get(current.left, set()) | descendants.get(current.right, set()) | {current.val}
                if p.val in descendants[current] and q.val in descendants[current]:
                    return current
                current = stack[-1] if stack else None



