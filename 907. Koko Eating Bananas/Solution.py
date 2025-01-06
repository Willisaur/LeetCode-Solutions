class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # if h == len(piles):
        #     return max(piles)
        
        def eat(arr, amnt):
            # print(amnt, [math.ceil(p / amnt) for p in piles])
            return sum([math.ceil(p / amnt) for p in piles]) <= h
        
        lower, upper = 1, max(piles)
        while lower < upper:
            middle = (lower + upper)//2
            # print(lower, upper, middle)
            if eat(piles, middle): # may be eating too many (k is too large)
                upper = middle
            else: # insufficient time for given problem (k is too small)
                lower = middle + 1
        return lower