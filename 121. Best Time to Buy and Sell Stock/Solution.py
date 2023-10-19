class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 1:
            return 0
        
        lowest = prices[0]
        maxProfit = 0

        for price in prices:
            if price < lowest:
                lowest = price
            else:
                if price - lowest > maxProfit:
                    maxProfit = price - lowest

        return maxProfit