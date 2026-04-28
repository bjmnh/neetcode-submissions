class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        nums.sort()
        def dfs(i, array, sum):
            if sum == target:
                res.append(array)
            if sum >= target or i == len(nums):
                return None


            dfs(i, array + [nums[i]], sum + nums[i])
            dfs(i + 1, array, sum)
        dfs(0, [], 0)
        return res
        
