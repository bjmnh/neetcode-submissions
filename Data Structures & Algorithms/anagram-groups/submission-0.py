class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dlist = {}
        for word in strs:
            t = "".join(sorted(word))
            if t not in dlist:
                dlist[t] = []
            dlist[t].append(word)
        return list(dlist.values())