# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        preidx =0
        inidx =0

        def build(limit):
            nonlocal preidx, inidx
            if preidx >= len(preorder):
                return None

            if inorder[inidx] == limit:
                inidx += 1
                return None

            node = TreeNode(preorder[preidx])
            preidx += 1
            node.left = build(node.val)
            node.right = build(limit)
            return node

        return build(float('inf'))