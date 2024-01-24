class Solution:
    def mySqrt(self, x: int) -> int:
        i, j, k = 0, x, x//2

        while i <= j:
            if k*k == x:
                return k
            if k*k > x:
                j = k-1
            else:
                i = k+1
            k = (i+j)//2

        return j