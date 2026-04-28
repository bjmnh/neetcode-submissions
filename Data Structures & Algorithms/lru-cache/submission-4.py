class ListNode:
    def __init__(self, val=0, key=None, next=None, prev=None):
        self.val = val
        self.key = key
        self.next = next
        self.prev = prev

class LRUCache:

    def __init__(self, capacity: int):
        self.hm = {}
        self.cap = capacity
        self.head = ListNode()
        self.tail = ListNode()
        self.head.next = self.tail
        self.tail.prev = self.head

    def add(self, key: int):
        self.hm[key].next = self.head.next
        self.head.next.prev = self.hm[key]
        self.hm[key].prev = self.head
        self.head.next = self.hm[key]


    def remove(self, key: int):
        self.hm[key].prev.next = self.hm[key].next
        self.hm[key].next.prev = self.hm[key].prev

        

    def get(self, key: int) -> int:
        if key in self.hm:
            if key != self.head.next.key:
                self.remove(key)
                self.add(key)
            return self.hm[key].val
        return -1
        

    def put(self, key: int, value: int) -> None:
        if key not in self.hm:
            self.hm[key] = ListNode(value, key)
            self.add(key)
        else:
            self.hm[key].val = value
            self.remove(key)
            self.add(key)

        if len(self.hm) > self.cap:
            t = self.tail.prev.key
            self.remove(t)
            self.hm.pop(t)






        
