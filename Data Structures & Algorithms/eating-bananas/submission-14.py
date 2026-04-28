class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        lp = 1
        rp = max(piles)
        best = rp
        while lp <= rp:
            mid = (lp + rp)//2
            test = 0
            for pile in piles:
                    test += -((-pile//mid))
            if test <= h:
                rp = mid - 1
                best = mid
            else:
                lp = mid + 1
        return best
