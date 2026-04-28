# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        q = deque()
        res = {}
        q.append([root, 0])

        while q:
            node, h = q.popleft()
            if node:
                q.append([node.left, h + 1])
                q.append([node.right, h + 1])
                res[h] = node.val
        return list(res.values()) 