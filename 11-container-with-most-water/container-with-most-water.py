class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r= 0, len(height) - 1
        max_area = 0
        while l < r:
            if height[l] < height[r]:
                area = (r - l) * height[l]
                l+=1
            else:
                area = (r - l) * height[r]
                r-=1
            if max_area < area:
                max_area = area
        return max_area