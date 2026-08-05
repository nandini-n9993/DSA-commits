class Solution:
    def maxOperations(self, num: List[int], k: int) -> int:
        num.sort()
        c,l,r=0,0,len(num)-1
        while l<r:
            if num[l]+num[r]==k:
                c+=1
                l+=1
                r-=1
            elif num[l]+num[r]<k:
                l+=1
            else:
                r-=1    
        return c