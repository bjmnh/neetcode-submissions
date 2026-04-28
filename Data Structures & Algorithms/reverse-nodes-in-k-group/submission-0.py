# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        dummy = runner = head
        linker = ret = None

        while runner:
            x = 0
            while x < k:
                if runner:
                    runner = runner.next
                    x +=1
                else:
                    return ret or dummy.next
            temp1 = runner
            t = head
            while head != runner:
                temp = head.next
                head.next = temp1
                temp1 = head
                head = temp

            if linker:
                linker.next = temp1
            else:
                ret = temp1
            linker = t
            


        return ret

            