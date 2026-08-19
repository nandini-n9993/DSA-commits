class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        k=strs[0]
        l=[]
        for i in range(len(k)):
            for j in range(1,len(strs)):
                print(k[i],strs[j])
                if i>=len(strs[j]) or k[i]!=strs[j][i]:
                    return "".join(l)
            l.append(k[i])
        return "".join(l)


# from typing import List

# class Solution:
#     def longestCommonPrefix(self, strs: List[str]) -> str:
#         if not strs:
#             return ""
            
#         # Take the first string as the reference
#         first_str = strs[0]
#         prefix = []
        
#         # Loop through each character index of the first string
#         for i in range(len(first_str)):
#             # Check this character against all other strings
#             for j in range(1, len(strs)):
#                 # Stop if the current string is too short, 
#                 # or if the character does not match exactly at position i
#                 print(first_str[i],strs[j])
#                 if i >= len(strs[j]) or first_str[i] != strs[j][i]:
#                     print(first_str[i],strs[j])
#                     return "".join(prefix)
            
#             # If all strings matched at index i, add it to the prefix
#             prefix.append(first_str[i])
#             print(prefix)
#         return "".join(prefix)
