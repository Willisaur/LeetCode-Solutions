class Solution:
    def compress(self, chars: List[str]) -> int:
        i, j = 0, 0
        endOfArr = 0

        while i < len(chars):
            chars[endOfArr] = chars[i]
            endOfArr += 1

            while j < len(chars)-1 and chars[i] == chars[j+1]: # inclusive range [i,j]
                j += 1

            if i != j:
                diff = str(j-i+1)

                for ch in diff:
                    chars[endOfArr] = ch
                    endOfArr += 1
            
            i = j+1
            j += 1
        
        return endOfArr