# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        placeholder = 1
        num1 = num2 = 0
        while l1:
            num1 += l1.val * placeholder
            placeholder*=10
            l1 = l1.next
        placeholder = 1
        while l2:
            num2 += l2.val * placeholder
            placeholder*=10
            l2 = l2.next
        res = num1 + num2
        if res == 0:
            return ListNode(0)
        dummy = ret = ListNode()
        while res > 0:
            ret.next = ListNode(res%10)
            ret = ret.next
            res = res//10
        return dummy.next
