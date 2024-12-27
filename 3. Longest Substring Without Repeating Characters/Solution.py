class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) < 2:
            return len(s)
        
        seen = set()
        i, j = 0, 0
        best = 0

        while j < len(s):
            if s[j] not in seen:
                seen.add(s[j])
                best = max(best, j-i+1)
            else:
                while s[i] != s[j]:
                    seen.remove(s[i])
                    i += 1
                i += 1
            j += 1
        return best
                


