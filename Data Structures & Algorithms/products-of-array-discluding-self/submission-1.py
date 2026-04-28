class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        sol = len(nums)*[1]
        n = len(sol)
        pref,suff = 1,1
        for x in range(0,n):
            sol[x] *= pref
            pref *= nums[x]
            sol[n- 1-x] *= suff
            suff *= nums[n-1-x]
        return sol        