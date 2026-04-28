class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lp, rp = 0, len(nums) - 1
        while lp <= rp:
            mid = int((lp +rp)//2)
            if nums[mid] == target:
                return mid
            if nums[mid] < target:
                lp = mid + 1
            else:
                rp = mid - 1
        return -1