# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head: return
        
        self.left = head
        self.is_done = False
        
        def helper(right):
            if not right:
                return
            
            # 1. Recurse to the very end
            helper(right.next)
            
            # 2. On the way back up, check if we're done
            if self.is_done:
                return
            
            # 3. Stop if the pointers meet or cross
            if self.left == right or self.left.next == right:
                right.next = None
                self.is_done = True
                return
            
            # 4. Interleave: Left -> Right -> Left.next
            next_left = self.left.next
            self.left.next = right
            right.next = next_left
            
            # 5. Move Left forward for the next return call
            self.left = next_left
            
        helper(head)