class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        i = 0
        j = 1

        best = 0

        while j < len(values):
            score = values[i] + values[j] + i - j 
            if score > best:
                best = score
            if values[i] - (j-i) < values[j]:
                i = j
            j += 1
        return best
        
        