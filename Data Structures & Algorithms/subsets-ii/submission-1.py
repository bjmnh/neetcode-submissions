class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = [[]]
        def backtrack(cur, i):
            print(cur, i, res)
            if i >= len(nums):
                return None

            cur.append(nums[i])
            res.append(cur.copy())
            backtrack(cur, i+1)
            cur.pop()
            add = 1
            while i + add < len(nums) and nums[i] == nums[i+add]:
                add += 1

            backtrack(cur, i+add)

        backtrack([],0)
        return res
        