class Solution:

    def encode(self, strs: List[str]) -> str:
        res = []
        for string in strs:
            res.append(str(len(string)) + "#" + string)
        return "".join(res)

    def decode(self, s: str) -> List[str]:
        dlist = []
        x = 0
        while x < len(s):
            y = x
            while y < len(s) and s[y] != '#':
                y += 1
            #x = start of number y+1 = #
            ssize = int(s[x:y])
            x = y + 1
            # x = #_
            y = x + ssize
            dlist.append(s[x:y])
            x = y
        return dlist
