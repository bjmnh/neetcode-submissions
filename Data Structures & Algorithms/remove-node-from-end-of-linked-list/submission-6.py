# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        runner = dummy = head
        dummy
        x = leng = 0
        while runner:
            leng+=1
            runner= runner.next
        delete = leng - n - 1
        if leng == 1:
            return None
        if leng == 2:
            if n == 1:
                head.next = None
                return head
            else:
                return head.next
        if delete < 0:
            return head.next
        while x < delete:
            x += 1
            dummy = dummy.next
        dummy.next = dummy.next.next or None
        return head
        
            


            