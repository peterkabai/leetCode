# https://leetcode.com/problems/trapping-rain-water/submissions/
class Solution:
    def trap(self, height: List[int]) -> int: 
        t = 0
        for i in range(1,len(height)):
            b = max(height[0:i])
            a = max(height[i:len(height)])
            v = min(b,a) - height[i]
            if v > 0: t += v
        return t