class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        counts = Counter(words)
        length = 0
        flag = False
        # print(counts)

        for k, v in counts.items():
            # print(k, v)
            k2 = k[::-1]
            
            if k != k2: # ex: ab matches with ba
                v2 = counts.get(k2, 0)
                length += min(v, v2) # ex: ab counted this time, ba counted later
            else:
                length += v if v % 2 == 0 else v-1 if v > 1 else 0
                    
                if v % 2: # single item in center of palindrome
                    flag = True
        
        return (length + flag) * 2