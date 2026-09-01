class Solution:
    def maxArea(self, height: List[int]) -> int:
        l=0
        r=len(height)-1
        maxi=0
        while l<r:
            area=min(height[l],height[r])*(r-l)
            maxi=max(area,maxi)
            print(height[l],height[r],area,maxi,r-l)
            if height[l]<height[r]:
                l+=1
            else:
                r-=1
        return maxi
