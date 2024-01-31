class Solution:
    def findSolutions(self, i, accum, nums, target):
        # already calculated
        if (i, accum) in self.dp:
            return self.dp[(i, accum)]

        # solution
        if i == len(nums)-1 and accum == target:
            return 1
        elif i < len(nums)-1:
            # choices
            self.dp[(i, accum)] = self.findSolutions(i+1, accum+nums[i], nums, target) + self.findSolutions(i+1, accum-nums[i], nums, target)
        else:
            return 0

        # no solution
        return self.dp[(i, accum)]

    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        self.dp = {}
        return self.findSolutions(-1, 0, nums, target)

