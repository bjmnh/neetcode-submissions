class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = [1] * len(nums)
        for n in range(len(nums)):
            x = n + 1
            y = n - 1
            while x < len(nums):
                ans[n] *= nums[x]
                x += 1
            while y >= 0:
                ans[n] *= nums[y]
                y -= 1
        return ans