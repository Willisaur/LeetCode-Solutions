class Solution:
    def reverseVowels(self, s: str) -> str:
        read_vowels = ""
        for ch in s:
            if ch in "aeiouAEIOU":
                read_vowels = ch + read_vowels
        j=0
        for i in range(len(s)):
            if s[i] in "aeiouAEIOU":
                s = s[:i] + read_vowels[j] + s[i+1:]
                j+=1
        return s