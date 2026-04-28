class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        for num in nums:
            tempres = []
            for p in res:
                for i in range(len(p) + 1):
                    pcopy = p.copy()
                    pcopy.insert(i, num)
                    tempres.append(pcopy)
            res = tempres.copy()
        return res