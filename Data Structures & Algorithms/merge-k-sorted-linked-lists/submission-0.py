# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy = ListNode(float('inf'))
        res = dummy
        remainder = True
        while remainder:
            smallest = dummy
            cur = -1
            for idx, node in enumerate(lists):
                if node and node.val < smallest.val:
                    smallest = node
                    cur = idx
            if smallest == dummy:
                remainder = False
            else:
                res.next = smallest
                res = res.next
                lists[cur] = lists[cur].next
        return dummy.next