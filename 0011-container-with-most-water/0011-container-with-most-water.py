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

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna