class Solution:
    def getLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        def getLAS(binaryDigit):
            arr = []
            for w,g in zip(words, groups):
                if g == binaryDigit:
                    arr.append(w)
                    binaryDigit = int(not binaryDigit)
            return arr
        
        zero = getLAS(0)
        one = getLAS(1)
        return [zero, one][len(zero)<len(one)]
        