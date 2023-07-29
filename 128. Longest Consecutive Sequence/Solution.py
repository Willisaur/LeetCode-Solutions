class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # add each element (as a key) to a dictionary
        # the dictionary's values are the range of numbers that are consecutive 
        # after creating each new key, delete the old neighboring ones if needed
        # iterate through the dict values at the end to find the widest range and return its length
        nums = set(nums)
        lookup = dict()
        size = 0

        for n in nums:
            if lookup and n-1 in lookup and n+1 in lookup: # n is between two existing ranges
                # get the most lower and upper keys of the ranges
                lowerBound = min(lookup[n-1][0], lookup[n+1][0])
                upperBound = max(lookup[n+1][1], lookup[n-1][1])

                # delete the old keys
                del lookup[n-1]
                del lookup[n+1]

                # create new keys or reassign old ones to merge the ranges
                lookup[lowerBound] = [lowerBound, upperBound]
                lookup[upperBound] = [lowerBound, upperBound]

            elif n-1 in lookup: # n is above a range/will be a new high key
                # get the most lower and upper keys of the range
                lowerBound = min(n, lookup[n-1][0])
                upperBound = max(n, lookup[n-1][1])

                # delete the old key
                del lookup[n-1]

                # update old lower bound key
                lookup[lowerBound] = [lowerBound, upperBound]
                # create new upper bound key
                lookup[upperBound] = [lowerBound, upperBound]
                
            elif n+1 in lookup: # n is below a range/will be a new low key
                # get the most lower and upper keys of the range
                lowerBound = min(n, lookup[n+1][0])
                upperBound = max(n, lookup[n+1][1])

                # delete the old key
                del lookup[n+1]

                # update new upper bound key
                lookup[lowerBound] = [lowerBound, upperBound]
                # create new upper bound key
                lookup[upperBound] = [lowerBound, upperBound]
            else:
                lookup[n] = [n, n]
            
        for v in lookup.values():
            if v[1] - v[0] + 1 > size:
                size = v[1] - v[0] + 1

        return size