class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        
        maxRevenue = 0
        minStockPrice = prices[0]

        for i in range(1, len(prices)):
            if prices[i] > minStockPrice:
                maxRevenue = max(maxRevenue, prices[i] - minStockPrice)
            
            minStockPrice = min(minStockPrice, prices[i])

        return maxRevenue