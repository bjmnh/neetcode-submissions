class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        hm = set()
        for num in nums:
            if num in hm:
                return num
            hm.add(num)