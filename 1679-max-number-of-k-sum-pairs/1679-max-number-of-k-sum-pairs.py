class Solution:
    def maxOperations(self, num: List[int], k: int) -> int:
        num.sort()
        c,l,r=0,0,len(num)-1
        while l<r:
            s=num[l]+num[r]
            if s==k:
                # a,b=num[l],num[r]
                # num.remove(a)
                # num.remove(b)
                # print(num)
                c+=1
                l+=1
                r-=1
                # l,r=0,len(num)-1
            elif s<k:
                l+=1
            else:
                # l+=1
                r-=1    
        return c