class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # cannot profit with only 1 day
        if len(prices) == 1:
            return 0
        
        # the lowest value will help calculate the max profit possible
        lowest = prices[0]
        # running highest-profit counter
        maxProfit = 0

        # for-each loop can be used since index is irrelevant
        for price in prices:
            # if there is a new low price, update the lowest price
            if price < lowest:
                lowest = price
            else: # price >= lowest; profit can be made
                # if the amount of profit is the new max, update the new max
                if price - lowest > maxProfit:
                    maxProfit = price - lowest

        return maxProfit # return max profit