# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        if (not p and q) or (not q and p):
            return False 
        stack1 = [p]
        stack2 = [q]
        while stack1 and stack2:
            nodep = stack1.pop()
            nodeq = stack2.pop()
            if nodep.val != nodeq.val:
                return False
            if nodep.left:
                stack1.append(nodep.left)
                if nodeq.left:
                    stack2.append(nodeq.left)
                else:
                    return False
            if nodep.right:
                stack1.append(nodep.right)
                if nodeq.right:
                    stack2.append(nodeq.right)
                else:
                    return False
            if nodeq.left:
                stack2.append(nodeq.left)
                if nodep.left:
                    stack1.append(nodep.left)
                else:
                    return False
            if nodeq.right:
                stack2.append(nodeq.right)
                if nodep.right:
                    stack1.append(nodep.right)
                else:
                    return False
            
            
        
        if stack1 or stack2:
            return False
        return True