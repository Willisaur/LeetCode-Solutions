class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        cStr = s[:k]
        cVowels = 0
        vowels = {"a", "e", "i", "o", "u"}

        for ch in cStr:
            if ch in vowels:
                cVowels += 1
        
        maxVowels = cVowels

        for i in range(k, len(s)):
            if cStr[0] in vowels:
                cVowels -= 1
            
            cStr = cStr[1:] + s[i]
            if s[i] in vowels:
                cVowels += 1
            
            if cVowels >  maxVowels:
                maxVowels = cVowels
            if maxVowels == k:
                return maxVowels

        return maxVowels