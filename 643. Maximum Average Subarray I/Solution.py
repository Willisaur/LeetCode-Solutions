class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        rSum = sum(nums[:k])
        rMax = rSum
        
        for i in range(k, len(nums)):
            rSum += nums[i]
            rSum -= nums[i-k]
            
            if rMax < rSum:
                rMax = rSum
            
        return rMax / k
        

