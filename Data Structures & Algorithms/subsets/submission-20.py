class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        for num in nums:
            temp = []
            for s in res:
                temp.append(s + [num])
            res = res + temp
        return res