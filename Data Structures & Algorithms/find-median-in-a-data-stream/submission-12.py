class MedianFinder:

    def __init__(self):
        self.minheap = []
        #This will hold the largest side
        self.maxheap = []
        #This will hold the smallest side
        

    def addNum(self, num: int) -> None:
        if not self.maxheap or num < -self.maxheap[0]:
            heapq.heappush(self.maxheap, -num)
        else:
            heapq.heappush(self.minheap, num)
        
        if len(self.maxheap) > len(self.minheap) + 1:
            heapq.heappush(self.minheap, - heapq.heappop(self.maxheap))
        if len(self.maxheap) < len(self.minheap):
            heapq.heappush(self.maxheap, - heapq.heappop(self.minheap))

        

    def findMedian(self) -> float:
        if len(self.minheap) == 0:
            return -self.maxheap[0]
        if len(self.maxheap) > len(self.minheap):
            return -self.maxheap[0]
        else:
            res = (-self.maxheap[0] + self.minheap[0]) / 2
            return res
        
        