class Solution:
    def largestAltitude(self, gain: list[int]) -> int:
        m=0
        l=[m]
        for i in range(len(gain)):
            m=m+gain[i]
            l.append(m)
        return max(l)