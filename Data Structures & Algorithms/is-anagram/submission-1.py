class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        td = {}
        sd = {}
        for l in s:
            sd[l] = sd.get(l, 0) + 1
    
        for l in t:
            td[l] = td.get(l, 0) + 1
        return sd == td
        

        