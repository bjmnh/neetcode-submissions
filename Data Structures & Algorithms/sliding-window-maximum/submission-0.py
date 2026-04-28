class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        result = []
        i = 0
        while i + k <= len(nums):
            result.append(max(nums[i:i+k]))
            i += 1
        return result
        