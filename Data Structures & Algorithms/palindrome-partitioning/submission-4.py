class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []

        def makelist(lead, idx):
            for x in range(idx, len(s)):
                for y in range(x + 1, len(s)):
                    if s[x] == s[y]:
                        if s[x:y+1] == s[x:y + 1][::-1]:
                            makelist(lead + [str(s[x:y+1])], y+1)
                lead.append(s[x])
            res.append(lead)
            
        makelist([], 0)
        return res