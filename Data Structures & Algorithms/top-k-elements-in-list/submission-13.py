class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freqb = [[] for i in range(len(nums) + 1)]
        for num in nums:
            if num in count:
                count[num] += 1
            else:
                count[num] = 1
        for key, val in count.items():
            freqb[val].append(key)
        res = []
        for i in range(len(freqb) - 1,0,-1):
            for num in freqb[i]:
                res.append(num)
                if len(res) == k:
                    return res