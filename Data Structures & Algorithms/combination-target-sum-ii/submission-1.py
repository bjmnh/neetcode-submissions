class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        resset = set()
        res = []
        def combin(start, clist, csum):
            if csum == target:
                resset.add(tuple(clist.copy()))

            
            
            for x in range(start, len(candidates)):
                if csum + candidates[x] > target:
                    break
                clist.append(candidates[x])
                combin(x + 1, clist, csum + candidates[x])
                clist.pop()
        combin(0, [], 0)
        for entry in resset:
            res.append(list(entry))
        return res
