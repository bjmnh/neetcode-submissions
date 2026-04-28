class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        self.nums = nums
        self.target = target
        result = set()
        rr = []
            
        def dfs(numarr):
            if sum(numarr) == self.target:
                result.add(tuple(sorted(numarr)))
            elif sum(numarr) >= self.target:
                return None
            
            for num in self.nums:
                dfs(numarr + [num])


        for num in nums:
            dfs([num])
        for item in result:
            rr.append(list(item))

        return rr