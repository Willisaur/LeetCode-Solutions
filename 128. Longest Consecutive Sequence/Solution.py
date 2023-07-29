class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # add each element (as a key) to a dictionary
        # the dictionary's values are the range of numbers that are consecutive 
        # after creating each new key, delete the old neighboring ones if needed
        # iterate through the dict values at the end to find the widest range and return its length

        nums = set(nums) # doesn't work if not a set since points overlap
        lookup = dict() # nums[i]: [lowerBound, upperBound]
        size = 0
        lowerBound, upperBound = 0, 0

        for n in nums:
            if lookup and n-1 in lookup and n+1 in lookup: # n is between two existing ranges
                # get the most lower and upper keys of the ranges
                lowerBound = lookup[n-1][0]
                upperBound = lookup[n+1][1]

                # create new keys or reassign old ones to merge the ranges
                lookup[lowerBound] = [lowerBound, upperBound]
                lookup[upperBound] = [lowerBound, upperBound]

                # check for size update
                if upperBound - lowerBound + 1 > size:
                    size = upperBound - lowerBound + 1

            elif n-1 in lookup: # n is above a range/will be a new high key
                # get the most lower and upper keys of the range
                lowerBound = lookup[n-1][0]
                upperBound = n

                # update old lower bound key
                lookup[lowerBound] = [lowerBound, upperBound]
                # create new upper bound key
                lookup[upperBound] = [lowerBound, upperBound]

                # check for size update
                if n - lowerBound + 1 > size:
                    size = n - lowerBound + 1
                
            elif n+1 in lookup: # n is below a range/will be a new low key
                # get the most lower and upper keys of the range
                lowerBound = n
                upperBound = lookup[n+1][1]

                # update new upper bound key
                lookup[lowerBound] = [lowerBound, upperBound]
                # create new upper bound key
                lookup[upperBound] = [lowerBound, upperBound]

                # check for size update
                if upperBound - n + 1 > size:
                    size = upperBound - n + 1
            else:
                lookup[n] = [n, n]

                # check for size update
                if lookup[n][1] - lookup[n][0] + 1 > size:
                    size = lookup[n][1] - lookup[n][0] + 1

        return size