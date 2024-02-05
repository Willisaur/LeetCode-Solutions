class Solution:
    def search(self, nums: List[int], target: int) -> int:
        i = 0
        j = len(nums) - 1
        k = j // 2

        while i <= j:
            if target == nums[k]:
                return k # found, return index
            elif target < nums[k]:
                j = k-1 # move upper pointer down
            else:
                i = k+1 # move lower pointer up
            k = (i+j)//2
        return -1 # not found, return -1