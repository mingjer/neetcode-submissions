class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        minn = prices[0]
        maxProfit = 0
        for i in range(1, len(prices)):
            maxProfit = max(maxProfit, prices[i] - minn)
            minn = min(prices[i], minn)
        
        return maxProfit