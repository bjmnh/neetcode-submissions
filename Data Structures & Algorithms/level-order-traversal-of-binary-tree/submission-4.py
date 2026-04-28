# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q = deque()
        q.append(root)
        res = []
        while q:
            l = len(q)
            level = []
            for i in range(l):
                root = q.popleft()
                if root:
                    q.append(root.left)
                    q.append(root.right)
                    level.append(root.val)
            if level:
                res.append(level[:])
        return res
