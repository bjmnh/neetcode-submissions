class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freqmap = {}
        lp = 0
        highestf = 0
        result = 0
        for rp in range(len(s)):
            freqmap[s[rp]] = 1 + freqmap.get(s[rp], 0)
            highestf = max(highestf, freqmap[s[rp]])

            while rp - lp + 1 - highestf > k:
                freqmap[s[lp]] -= 1
                lp += 1
            result = max(result, rp - lp + 1)
        return result