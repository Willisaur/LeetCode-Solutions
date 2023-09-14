class Solution:
    def maxArea(self, height: List[int]) -> int:
        def area(i, j, height):
            length = j-i
            width = min(height[i], height[j])
            return length * width
        
        i, j = 0, len(height)-1
        maxArea = area(i, j, height)

        while i < j:
            localArea = area(i, j, height)

            if maxArea < localArea:
                maxArea = localArea
            
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        
        return maxArea
    