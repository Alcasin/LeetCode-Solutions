class Solution:
    def maxArea(self, height: List[int]) -> int:
        l=0
        r = len(height) -1
        maxw = min(height[l],height[r])*(r-l)
        while l<r:
            if(height[l]<height[r]):
                l=l+1
                w=min(height[l],height[r])*(r-l)
                maxw=max(maxw,w)
            else:
                r=r-1
                w=min(height[l],height[r])*(r-l)
                maxw=max(maxw,w)
        return maxw