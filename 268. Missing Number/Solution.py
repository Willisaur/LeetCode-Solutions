class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        val = 0
        nums = sorted(nums)

        while val < len(nums):
            if val != nums[val]:
                return val
            val += 1
        
        return val