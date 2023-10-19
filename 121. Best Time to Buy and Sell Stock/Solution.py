class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # if only one day occurs, we cannot profit
        if len(prices) == 1:
            return 0

        # we will compare the current stock price to the lowest price yet
        maxProfit = 0 # running max profit counter
        lowest = prices[0] 

        for price in prices:
            if price < lowest:
                lowest = price
            else: 
                if maxProfit < price - lowest:
                    maxProfit = price - lowest
        
        return maxProfit
