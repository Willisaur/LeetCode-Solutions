class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        k2 = float(k)
        rSum = sum(nums[:k])
        rMean = rSum / k2
        rMax = rMean
        
        for i in range(k, len(nums)):
            rSum += nums[i]
            rSum -= nums[i-k]
            rMean = rSum / k2
            
            if rMax < rMean:
                rMax = rMean
            
        return rMax
        

