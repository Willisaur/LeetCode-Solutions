class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # since you know the target, calculate the complement
        # the complement is the key, and the index is the value
        
        lookup = dict()

        for i in range(len(nums)):
            if nums[i] in lookup.keys():
                return [lookup[nums[i]], i]
            lookup[target - nums[i]] = i