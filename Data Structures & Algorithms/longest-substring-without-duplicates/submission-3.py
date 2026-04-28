class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        elif len(s) == 1:
            return 1
        lp = 0
        rp = 1
        longest = 0
        seen = {}
        seen[s[0]] = lp
        while rp < len(s):
            if s[rp] in seen:
                if seen[s[rp]] >= lp:
                    lp = seen[s[rp]] + 1
            
            seen[s[rp]] = rp
            longest = max(longest, 1 + rp-lp)
            rp += 1
        return longest