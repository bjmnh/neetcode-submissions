class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []

        def makelist(lead, idx):
            clist = lead
            for x in range(idx, len(s)):
                for y in range(x + 1, len(s)):
                    if s[x] == s[y]:
                        print("s[x:y] == s[x:y:-1] \n", s[x:y + 1], "==", s[x:y + 1][::-1])
                        if s[x:y+1] == s[x:y + 1][::-1]:
                            makelist(clist + [str(s[x:y+1])], y+1)
                clist.append(s[x])
            res.append(clist)
            
        makelist([], 0)
        return res