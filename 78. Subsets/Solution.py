class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        answers = []
        def build(current=[], i=0):
            # solved
            answers.append(current)

            # out of bounds
            if i == len(nums):
                return
            
            # make a choice
            for j in range(i, len(nums)): # iterate through all options
                build(current + [nums[j]], j+1) # future options cannot include previous number in numbers
        
        build()
        return answers