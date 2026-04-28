class MedianFinder:

    def __init__(self):
        self.intlist = []

    def addNum(self, num: int) -> None:
        self.intlist.append(num)
        

    def findMedian(self) -> float:
        if len(self.intlist) == 1:
            return self.intlist[0]
        self.intlist.sort()
        if len(self.intlist) %2 == 0:
            median = (self.intlist[len(self.intlist)//2] + self.intlist[len(self.intlist)//2 - 1]) / 2
        else:
            median = self.intlist[len(self.intlist)//2]
        
        return median