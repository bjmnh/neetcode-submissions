class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        closest = []
        lookup = {}
        for point in points:
            x = point[0]
            y = point[1]
            dist = x**2 + y**2
            heapq.heappush(closest, dist)
            if dist in lookup:
                lookup[dist].append(point)
            else:
                lookup[dist] = [point]
        res = []
        for i in range(k):
            dist = heapq.heappop(closest)
            res.append(lookup[dist][-1])
            lookup[dist].pop()
        return res
            
