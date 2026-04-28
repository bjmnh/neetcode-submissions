class Solution:
    def trap(self, height: List[int]) -> int:
        largestttl = []
        largestttr = []
        leftmax = 0
        rightmax = 0
        total = 0
        for num in height:
            leftmax = max(leftmax, num)
            largestttl.append(leftmax)
        for num in height[::-1]:
            rightmax = max(rightmax, num)
            largestttr.append(rightmax)
        largestttr = largestttr[::-1]
        
        for v, num in enumerate(height):
            if num < min(largestttl[v], largestttr[v]):
                total += min(largestttl[v], largestttr[v]) - num
        return total

