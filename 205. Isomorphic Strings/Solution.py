class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        # create a dict mapping all characters in s to t
        # if a key exists, ensure its value matches the current letter in t and that the key isn't in values
        # if a key doesn't exist, add it to the dict
        # create a new s var to check for equality in the end; add to it every iteration

        lookup = dict()
        newS = ""
        
        for i in range(len(s)):
            if s[i] not in lookup.keys():
                if t[i] in lookup.values():
                    return False
                lookup[s[i]] = t[i]
            elif lookup[s[i]] != t[i]:
                return False
            newS += lookup[s[i]]

        return newS == t
