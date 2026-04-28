class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        part = []
        def makelist(idx):
            temp = len(part)
            for x in range(idx, len(s)):
                for y in range(x + 1, len(s)):
                    if s[x] == s[y]:
                        if s[x:y+1] == s[x:y + 1][::-1]:
                            part.append(str(s[x:y+1]))
                            makelist(y+1)
                            part.pop()
                part.append(s[x])
            res.append(part.copy())
            while len(part) > temp:
                part.pop()
            
        makelist(0)
        return res