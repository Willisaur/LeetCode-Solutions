class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        arr = [0] * (len(nums) + 1)
        for a, b in queries:
            arr[a] += 1
            arr[b+1] -= 1

        curr = 0
        for i in range(len(nums)):
            curr += arr[i]
            if curr < nums[i]:
                return False
        return True