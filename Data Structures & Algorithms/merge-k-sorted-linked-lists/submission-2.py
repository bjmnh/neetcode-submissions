# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq
class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        minpq = []
        dummy = cur = ListNode()

        for idx, root in enumerate(lists):
            heapq.heappush(minpq, (root.val, idx, root))
        while minpq:
            val, idx, root = heapq.heappop(minpq)
            cur.next = root
            cur = cur.next

            if root.next:
                lists[idx] = lists[idx].next
                heapq.heappush(minpq, (lists[idx].val, idx, lists[idx]))
        return dummy.next

