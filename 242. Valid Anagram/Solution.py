class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # use a dict to count all letters in t
        # subtract letters from that dict when iterating through s
        # be careful about keys not existing

        if len(t) != len(s):
            return False 
        
        lookup = dict()

        for ch in t:
            if ch in lookup.keys():
                lookup[ch] += 1
            else:
                lookup[ch] = 1
            
        for ch in s:
            if ch not in lookup.keys():
                return False
            elif lookup[ch] == 0:
                return False
            else:
                lookup[ch] -= 1
            
        return True
                