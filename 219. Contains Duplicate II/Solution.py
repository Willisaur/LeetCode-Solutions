class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # use a hashmap to store previous values (fast lookup time) as keys and indices as values
        # could use math to simplify abs(i-j) <= k for better speed
        # first index should always be stored; second time shouldn't be since i-j would be greater

        history = dict()

        for i in range(len(nums)):
            if nums[i] in history:
                if abs(i-history[nums[i]]) <= k:
                    return True
            
            history[nums[i]] = i
                
        return False