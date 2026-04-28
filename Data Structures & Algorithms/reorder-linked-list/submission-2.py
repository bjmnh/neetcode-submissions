# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        slow = fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        temp = None

        while slow:
            next = slow.next
            slow.next = temp
            temp = slow
            slow = next
        slow = temp
        while head and slow:
            temp1 = head.next
            temp2 = slow.next
            head.next = slow
            slow.next = temp1
            slow = temp2
            head = temp1
        
