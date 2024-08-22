class Solution:
    def reverse(self, x: int) -> int:
        reverseX = 0
        length = 0
        isNegative = x < 0
        if isNegative:
            x *= -1
        maxTruncatedIntReversed = [8,4,6,3,8,4,7,4,1,2]
        hasIncreased = False
        hasDecreased = False
        digitFlag = False

        while x > 0:
            length += 1
            digit = x % 10
            x //= 10

            # must not increase before decreasing
            if maxTruncatedIntReversed[10-length] < digit:
                hasIncreased = True
                if not hasDecreased:
                    digitFlag = True
            elif maxTruncatedIntReversed[10-length] > digit:
                hasDecreased = True

            #print(hasIncreased, hasDecreased, digitFlag, digit, maxTruncatedIntReversed[10-length], length)
            if length == 10 and digitFlag:
                return 0
            
            reverseX *= 10
            reverseX += digit
        
        return reverseX * (1, -1)[isNegative]