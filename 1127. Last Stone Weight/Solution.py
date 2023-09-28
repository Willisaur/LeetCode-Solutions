class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-i for i in stones] # negate for max heap
        heapq.heapify(stones) 

        while len(stones) > 1:
            y = -heapq.heappop(stones)
            x = -heapq.heappop(stones)

            if x != y:
                heapq.heappush(stones, -(y-x))
            
        if stones:
            return -heapq.heappop(stones)
        
        return 0
