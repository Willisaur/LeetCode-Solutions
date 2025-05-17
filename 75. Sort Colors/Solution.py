class Solution:
    def sortColors(self, nums: List[int]) -> None:
        c = Counter(nums)
        i = 0
        while i < c[0]:
            nums[i] = 0
            i += 1
        while i < c[0] + c[1]:
            nums[i] = 1
            i += 1
        while i < sum(c.values()):
            nums[i] = 2
            i += 1