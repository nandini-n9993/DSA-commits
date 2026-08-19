class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        k=strs[0]
        l=[]
        for i in range(len(k)):
            for j in range(1,len(strs)):
                # print(k[i],strs[j])
                if i>=len(strs[j]) or k[i]!=strs[j][i]:
                    # print(strs[i][j],l)
                    return "".join(l)
            l.append(k[i])
        return "".join(l)