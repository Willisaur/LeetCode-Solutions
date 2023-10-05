class Solution:
    def search(self, nums: List[int], target: int) -> int:
        i = 0
        j = len(nums) - 1
        k = j // 2

        while i <= j:
            if target == nums[k]:
                return k
            elif target < nums[k]:
                j = k - 1
            else:
                i = k + 1
            k = (j - i) // 2 + i
        
        return -1