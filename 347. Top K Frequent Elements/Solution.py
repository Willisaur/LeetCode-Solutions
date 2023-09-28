class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        
        for n in nums:
            if n in count:
                count[n] += 1
            else:
                count[n] = 1
        
        count = [(-v, k) for k, v in count.items()] # negative for max heap

        heapq.heapify(count)
        
        arr = []
        for i in range(k):
            arr.append(heapq.heappop(count))
        
        return [k for v, k in arr]



