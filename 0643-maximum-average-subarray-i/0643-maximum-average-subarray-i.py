class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        s=sum(nums[:k])
        maxi=s
        for i in range(k,len(nums)):
            s+=nums[i]-nums[i-k]
            maxi=max(maxi,s)
        return maxi/k
