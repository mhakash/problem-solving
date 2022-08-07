class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        maxSoFar = 0
        
        while l < r:
            area = (r - l) * min(height[l], height[r])
            maxSoFar = max(maxSoFar, area)
            
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        
        return maxSoFar
            