class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # 1. Base case: If we hit a null node or find one of our targets
        if not root or root.val == p.val or root.val == q.val:
            return root
        
        # 2. Look left and right
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        
        # 3. If both children returned something, this node is the LCA
        if left and right:
            return root
            
        # 4. If only one side found something, return that side. 
        # If neither found anything, this naturally returns None.
        return left if left else right