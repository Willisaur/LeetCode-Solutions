class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        arr = [0] * len(s)
        out = []
        
        def shiftLetter(ch, amnt):
            # print(ch, amnt)
            if amnt > 0:
                while ord(ch) + amnt > 97 + 25:
                    amnt -= 26
                # print(chr(ord(ch) + amnt))
                return chr(ord(ch) + amnt)
            if amnt < 0:
                while ord(ch) + amnt < 97:
                    amnt += 26
                # print(chr(ord(ch) + amnt))
                return chr(ord(ch) + amnt)
            return ch
        
        for i in range(len(shifts)):
            shift = shifts[i]
            arr[shift[0]] += 1 if shift[-1]==1 else -1
            if shift[1]+1 < len(s):
                arr[shift[1]+1] -= 1 if shift[-1] == 1 else -1
        
        # print(arr)
        for i in range(len(s)):
            if i > 0:
                arr[i] += arr[i-1]
            out.append(shiftLetter(s[i], arr[i]))

        return ''.join(out)