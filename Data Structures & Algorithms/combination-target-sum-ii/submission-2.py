class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        def combin(start, clist, csum):
            if csum == target:
                res.append(clist.copy())

            
            
            for x in range(start, len(candidates)):
                if x > start and candidates[x] == candidates[x-1]:
                    continue
                if csum + candidates[x] > target:
                    break
                clist.append(candidates[x])
                combin(x + 1, clist, csum + candidates[x])
                clist.pop()
        combin(0, [], 0)
        return res
