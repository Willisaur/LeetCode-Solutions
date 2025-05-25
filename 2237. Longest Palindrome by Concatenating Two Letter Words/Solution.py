class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        counts = Counter(words)
        length = 0
        flag = True
        # print(counts)

        for k, v in counts.items():
            # print(k, v)
            k2 = k[::-1]
            
            if k != k2: # ex: ab matches with ba
                v2 = counts.get(k2, 0)
                length += 2 * min(v, v2) # ex: ab counted this time, ba counted later
            else:
                if v % 2 == 0: # symmetric; add as-is
                    length += 2 * v
                elif v > 1: # odd number of symmetric occurences -- just remove the odd one
                    length += 2 * (v-1)
                    
                if flag and v % 2: # single item in center of palindrome
                    flag = False
                    length += 2
        
        return length