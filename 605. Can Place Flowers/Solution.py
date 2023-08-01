class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if len(flowerbed) >= 2:
            if flowerbed[0] == 0:
                if flowerbed[1] == 0:
                    n -=1
                    flowerbed[0] = 1

            if flowerbed[-1] == 0:
                if flowerbed[-2] == 0:
                    n -=1
                    flowerbed[-1] = 1
        elif len(flowerbed) == 1:
            if flowerbed[0] == 0:
                return n - 1 < 1
            else:
                return n < 1
        else:
            return n == 0

        z = 0
        for i in flowerbed:
            if i == 0:
                z += 1
            else:
                z = 0
            
            if z == 3:
                z = 1
                n -= 1
        
        return n < 1