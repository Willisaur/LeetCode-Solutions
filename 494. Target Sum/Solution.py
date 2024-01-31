class Solution:
    def findSolutions(self, i, accum, nums, target):
        # already calculated
        if (i, accum) in self.dp:
            return self.dp[(i, accum)]

        # solution
        if i == len(nums)-1 and accum == target:
            return 1
        
        # choices
        if i < len(nums)-1:
            self.dp[(i, accum)] = self.findSolutions(i+1, accum+nums[i], nums, target) + self.findSolutions(i+1, accum-nums[i], nums, target)
            return self.dp[(i, accum)]
            
        # out of bounds or no solution
        return 0


    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        self.dp = {} 
        return self.findSolutions(-1, 0, nums, target)

