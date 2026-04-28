class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxheap = [-s for s in stones]
        heapq.heapify(maxheap)
        while len(maxheap) > 1:
            y =  - heapq.heappop(maxheap)
            x = - heapq.heappop(maxheap)
            if x < y:
                y = -(y-x)
                heapq.heappush(maxheap, y)
        if maxheap:
            return - heapq.heappop(maxheap)
        return 0