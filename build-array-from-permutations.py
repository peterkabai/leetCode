# https://leetcode.com/problems/build-array-from-permutation/submissions/
class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        ans = []
        for i in nums:
            ans.append(nums[i])
        return ans
        