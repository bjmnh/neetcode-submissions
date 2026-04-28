class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        currentmin = prices[0]
        bestp = 0

        for index, val in enumerate(prices):
            currentmin = min(currentmin, val)
            bestp = max(bestp, val - currentmin)
        return bestp

        