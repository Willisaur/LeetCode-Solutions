class NumArray:

    def __init__(self, nums: List[int]):
        # ex: [1, 2, 3, 4, 5]
        # tr: [1, 3, 6, 10, 15]
        # (2, 5) = 15-6 = 9
        # this is accum[right]-accum[left-1] for all left > 0
        # if left == 0, return accum[right]
        self.accum = []
        if nums:
            self.accum.append(nums[0])
        for n in nums[1:]:
            self.accum.append(n+self.accum[-1])

    def sumRange(self, left: int, right: int) -> int:
        if left == 0:
            return self.accum[right]
        return self.accum[right]-self.accum[left-1]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)