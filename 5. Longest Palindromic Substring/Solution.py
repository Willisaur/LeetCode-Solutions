class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest = s[0]

        for i in range(len(s)):
            for j in range(len(s)-1, i, -1):
                if j-i+1 < len(longest):
                    break

                a = s[i:j+1]
                b = s[j:i-1:-1] if i-1 != -1 else s[j::-1]
                # print(i,j)
                # print(a, '|', b)
                if a == b and len(a) > len(longest):
                    longest = a

        return longest