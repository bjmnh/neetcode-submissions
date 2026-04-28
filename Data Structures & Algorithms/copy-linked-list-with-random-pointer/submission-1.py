"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        dummy1 = head
        res = dummy2 = Node(head.val)
        lookupt = {dummy1:dummy2}

        while dummy1.next:
            dummy1 = dummy1.next
            dummy2.next = Node(dummy1.val)
            dummy2 = dummy2.next
            lookupt[dummy1] = dummy2
        
        dummy1 = head
        dummy2 = res
        while dummy2:
            if dummy1.random:
                dummy2.random = lookupt[dummy1.random]
            else:
                dummy2.random = None
            dummy2 = dummy2.next
            dummy1 = dummy1.next


        return res
