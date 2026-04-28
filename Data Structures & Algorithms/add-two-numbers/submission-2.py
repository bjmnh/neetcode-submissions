# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy1, dummy2 = l1, l2
        carry = 0
        while l1 and l2:
            value = l1.val + l2.val + carry
            carry = value//10
            l1.val = value%10
            l2.val = value%10
            t1, t2 = l1, l2
            l1 = l1.next
            l2 = l2.next
        if l1:
            if carry:
                while l1.next and l1.val == 9:
                    l1.val = 0
                    l1 = l1.next
                if l1.val == 9:
                    l1.val = 0
                    l1.next = ListNode(carry)
                else:
                    l1.val += carry
            return dummy1
        elif l2:
            if carry:
                while l2.next and l2.val == 9:
                    l2.val = 0
                    l2 = l2.next
                if l2.val == 9:
                    l2.val = 0
                    l2.next = ListNode(carry)
                else:
                    l2.val += carry
            return dummy2
        else:
            if carry:
                t1.next = ListNode(carry)
            return dummy1