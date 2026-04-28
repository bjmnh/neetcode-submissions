class Solution:
    def findMin(self, nums: List[int]) -> int:
        lp = 0
        rp = len(nums) - 1
        while lp <= rp:
            mid = (lp + rp)//2
            if nums[mid] < nums[rp]:
                rp = mid
            else:
                lp = mid + 1
        return nums[rp]

        