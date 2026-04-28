# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        interval = 1
        while interval < len(lists):
            for x in range(0,len(lists), interval*2):
                lists[x] = self.merge2(lists[x], lists[x+interval] if x + interval < len(lists) else None)
            interval *= 2
        return lists[0]

    def merge2(self, list1, list2) -> ListNode:
        res = dummy = ListNode()
        while list1 and list2:
            if list1.val > list2.val:
                dummy.next = list2
                list2 = list2.next
            else:
                dummy.next = list1
                list1 = list1.next
            dummy = dummy.next
        
        dummy.next = list1 or list2
        return res.next