# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q = deque()
        q.append([root,0])
        res = {}
        while q:
            root, h = q.popleft()
            if root:
                q.append([root.left, h + 1])
                q.append([root.right, h + 1])
                if h not in res:
                    res[h] = []
                res[h].append(root.val)
        return list(res.values())