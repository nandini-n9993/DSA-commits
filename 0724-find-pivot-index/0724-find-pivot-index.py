# class Solution:
#     def pivotIndex(self, nums: list[int]) -> int:
#         lsum=0
#         tot=sum(nums)
#         p=0
#         # while p<len(nums):
#         for i in range(len(nums)):
#             # for i in range(p):
#             #     lsum+=nums[i]
#             # for i in range(p+1,len(nums)):
#             #     rsum+=nums[i]
#             if p==0:
#                 lsum=0
#             lsum+=nums[i-1]
#             rsum=tot-lsum-p
#             print(p,lsum,rsum)
#             if lsum==rsum:
#                 break
#             else:
#                 # lsum=rsum=0
#                 p+=1
#         if p!=len(nums):
#             return p
#         else:
#             return -1


class Solution:
    def pivotIndex(self, nums: list[int]) -> int:
        total_sum = sum(nums)
        lsum = 0
        for p, num in enumerate(nums):
            rsum = total_sum - lsum - num
            if lsum == rsum:
                return p
            lsum += num
        return -1