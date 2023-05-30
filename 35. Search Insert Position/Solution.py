class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        i = 0
        isFound = False
        while i < len(nums) and isFound == False:
            if nums[i] < target:
                i += 1
            else:
                isFound = True
                
        return i