class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        part = []
        def makelist(idx):
            if idx >= len(s):
                res.append(part.copy())
                return
            for y in range(idx, len(s)):
                if s[idx] == s[y]:
                    if s[idx:y+1] == s[idx:y + 1][::-1]:
                        part.append(str(s[idx:y+1]))
                        makelist(y+1)
                        part.pop()
   
        makelist(0)
        return res