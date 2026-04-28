class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash1 = {}
        for v, num in enumerate(nums):
            if num in hash1:
                return [hash1[num], v]
            hash1[target - num] = v
        