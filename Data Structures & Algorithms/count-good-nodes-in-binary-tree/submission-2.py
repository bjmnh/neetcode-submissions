# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        q = deque()
        q.append([root, root.val])
        good = 0
        while q:
            node, l = q.popleft()
            if node:
                if l <= node.val:
                    good += 1
                l = max(l, node.val)
                q.append([node.left, l])
                q.append([node.right,l])
        return good