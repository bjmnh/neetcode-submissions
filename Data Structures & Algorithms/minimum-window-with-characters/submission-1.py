class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        scount = [0] * 52
        tcount = [0] * 52
        matches = 0
        result = [1000000000000,0,0]
        for i in range(len(t)):
            scount[ord(s[i])-ord('a')] += 1
            tcount[ord(t[i])-ord('a')] += 1
        for i in range(52):
            if scount[i] >= tcount[i]:
                matches += 1
        lp, rp = 0, len(t)

        while rp < len(s):
            if matches == 52:
                while scount[ord(s[lp])-ord('a')] > tcount[ord(s[lp])-ord('a')]:
                    scount[ord(s[lp])-ord('a')] -= 1
                    lp += 1
                if rp - lp + 1 < result[0]:
                    result[0],result[1],result[2] = rp -lp + 1,lp, rp
 
            if scount[ord(s[rp])-ord('a')] + 1 == tcount[ord(s[rp])-ord('a')]:
                matches += 1
            scount[ord(s[rp])-ord('a')] += 1
            rp += 1

        if matches == 52:
            while scount[ord(s[lp])-ord('a')] > tcount[ord(s[lp])-ord('a')]:
                scount[ord(s[lp])-ord('a')] -= 1
                lp += 1
            if rp - lp + 1 < result[0]:
                result[0],result[1],result[2] = rp -lp + 1,lp, rp
 

        return s[result[1]:result[2]] 

