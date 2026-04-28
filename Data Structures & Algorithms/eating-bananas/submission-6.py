class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        maxk = max(piles)
        mink = 1

        while mink <= maxk:
            
            halfway = (maxk + mink)//2
            testh = 0
            for pile in piles:
                testh += math.ceil(pile/halfway)
            if testh > h:
                mink = halfway + 1
            else:
                maxk = halfway - 1
            

        return mink